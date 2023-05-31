# import pytest
# from pyspark.sql import DataFrame
# from databricks.connect import DatabricksSession
# import os

from my_library import pyspark_functions

# spark = DatabricksSession.builder.getOrCreate()

def vscodetst_create_sample_dataframe_valid_df():
    return_df = pyspark_functions.create_sample_dataframe(spark)
    assert return_df.count() == 2
    assert isinstance(return_df, DataFrame), "Returned variable is not a DataFrame"
    print("Completed test for create_sample_dataframe")

if __name__ == "__main__":
    vscodetst_create_sample_dataframe_valid_df(spark)
