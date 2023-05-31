# from databricks.sdk.runtime import *
from pyspark.sql.functions import concat

def create_sample_dataframe(spark):
    df = spark.createDataFrame([["test1", 1],["test2", 2]])
    df = df.withColumn("combined_val", concat("_1", "_2"))
    
    return df

def databricks_list_files(dbutils):
    files = dbutils.fs.ls("dbfs:/Users/dustin.vannoy@databricks.com/field_demos")
    for f in files:
        print(f)
