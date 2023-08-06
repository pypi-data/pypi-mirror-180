
from pyspark.sql.functions import *
from pyspark.sql import DataFrame
from pyspark.sql.types import *
from typing import List
from delta.tables import DeltaMergeBuilder, DeltaTable


def deltaLakeMergeForEachBatch(originalDataset: DeltaTable, props):
    def wrapper(batchDF: DataFrame, batchId: int):
        if props.writeMode == "merge":
            dt = originalDataset.alias(props.mergeTargetAlias) \
                .merge(batchDF.alias(props.mergeSourceAlias), props.mergeCondition.column())

            resMatched: DeltaMergeBuilder = dt

            if props.matchedActionDelete == "delete":
                if props.matchedConditionDelete is not None:
                    resMatched = resMatched.whenMatchedDelete(condition=props.matchedConditionDelete.column())
                else:
                    resMatched = resMatched.whenMatchedDelete()

            if props.matchedAction == "update":
                matched_expr = {}
                if len(props.matchedTable) > 0:
                    for scol in props.matchedTable:
                        target_col = scol.target
                        matched_expr[target_col] = scol.expression.column()

                if props.matchedCondition is not None:
                    if len(props.matchedTable) > 0:
                        resMatched = resMatched.whenMatchedUpdate(
                            condition=props.matchedCondition.column(),
                            set=matched_expr)
                    else:
                        resMatched = resMatched.whenMatchedUpdateAll(
                            condition=props.matchedCondition.column())
                else:
                    if len(props.matchedTable) > 0:
                        resMatched = resMatched.whenMatchedUpdate(set=matched_expr)
                    else:
                        resMatched = resMatched.whenMatchedUpdateAll()

            if props.notMatchedAction is not None:
                if props.notMatchedAction == "insert":
                    not_matched_expr = {}
                    if len(props.notMatchedTable) > 0:
                        for scol in props.notMatchedTable:
                            target_col = scol.target
                            not_matched_expr[target_col] = scol.expression.column()

                    if props.notMatchedCondition is not None:
                        if len(props.notMatchedTable) > 0:
                            resMatched = resMatched.whenNotMatchedInsert(
                                condition=props.notMatchedCondition.column(),
                                values=not_matched_expr)
                        else:
                            resMatched = resMatched.whenNotMatchedInsertAll(
                                condition=props.notMatchedCondition.column())
                    else:
                        if len(props.notMatchedTable) > 0:
                            resMatched = resMatched.whenNotMatchedInsert(values=not_matched_expr)
                        else:
                            resMatched = resMatched.whenNotMatchedInsertAll()

            resMatched.execute()
        elif props.writeMode == "merge_scd2":
            keyColumns = props.keyColumns
            scdHistoricColumns = props.historicColumns
            fromTimeColumn = props.fromTimeCol
            toTimeColumn = props.toTimeCol
            minFlagColumn = props.minFlagCol
            maxFlagColumn = props.maxFlagCol
            flagY = "1"
            flagN = "0"
            if props.flagValue == "boolean":
                flagY = "true"
                flagN = "false"

            updatesDF: DataFrame = batchDF.withColumn(minFlagColumn, lit(flagY)).withColumn(maxFlagColumn, lit(flagY))
            updateColumns: List[str] = updatesDF.columns
            existingTable: DeltaTable = originalDataset
            existingDF: DataFrame = existingTable.toDF()

            cond = None
            for scdCol in scdHistoricColumns:
                if cond is None:
                    cond = (existingDF[scdCol] != updatesDF[scdCol])
                else:
                    cond = (cond | (existingDF[scdCol] != updatesDF[scdCol]))

            rowsToUpdate = updatesDF \
                .join(existingDF, keyColumns) \
                .where(
                (existingDF[maxFlagColumn] == lit(flagY)) & (
                    cond
                )) \
                .select(*[updatesDF[val] for val in updateColumns]) \
                .withColumn(minFlagColumn, lit(flagN))

            stagedUpdatesDF: DataFrame = rowsToUpdate \
                .withColumn("mergeKey", lit(None)) \
                .union(updatesDF.withColumn("mergeKey", concat(*keyColumns)))

            updateCond = None
            for scdCol in scdHistoricColumns:
                if updateCond is None:
                    updateCond = (existingDF[scdCol] != stagedUpdatesDF[scdCol])
                else:
                    updateCond = (updateCond | (existingDF[scdCol] != stagedUpdatesDF[scdCol]))

            existingTable \
                .alias("existingTable") \
                .merge(
                stagedUpdatesDF.alias("staged_updates"),
                concat(*[existingDF[key] for key in keyColumns]) == stagedUpdatesDF["mergeKey"]
            ) \
                .whenMatchedUpdate(
                condition=(existingDF[maxFlagColumn] == lit(flagY)) & updateCond,
                set={
                    maxFlagColumn: flagN,
                    toTimeColumn: ("staged_updates." + fromTimeColumn)
                }
            ).whenNotMatchedInsertAll() \
                .execute()

    return wrapper