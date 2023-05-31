# Databricks notebook source
# from databricks.sdk.runtime import *
from my_library import pyspark_functions, misc_functions

spark = pyspark_functions.get_spark_session()

# COMMAND ----------

import os
os.getenv("DATABRICKS_RUNTIME_VERSION")

# COMMAND ----------

spark.sql("""
CREATE EXTERNAL TABLE hive_metastore.default.nyctaxi_yellow_trips_external
USING delta
LOCATION "dbfs:/databricks-datasets/nyctaxi/tables/nyctaxi_yellow/"
""")

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE hive_metastore.default.nyctaxi_yellow_trip_agg AS
# MAGIC SELECT
# MAGIC   date(pickup_datetime) as pickup_date,
# MAGIC   trip_distance,
# MAGIC   count(1) as record_count,
# MAGIC   count(vendor_id) as vendor_count,
# MAGIC   count(distinct rate_code_id) as rate_count,
# MAGIC   sum(total_amount) as total
# MAGIC FROM hive_metastore.default.nyctaxi_yellow_trips_external
# MAGIC GROUP BY date(pickup_datetime), trip_distance

# COMMAND ----------

# Use id_lookup just as example
person_id = misc_functions.id_lookup("person2")
print(person_id)
