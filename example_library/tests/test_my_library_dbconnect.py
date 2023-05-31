import pytest
import os
from pyspark.sql import DataFrame

import sys
currentdir = os.path.dirname(__file__)
parentdir = os.path.dirname(currentdir)
print(parentdir)
sys.path.insert(0,parentdir)

from my_library import pyspark_functions

db_profile = os.getenv("DB_PROFILE", "e2-field-eng")
db_cluster = os.getenv("DB_CLUSTER")

@pytest.fixture(scope="session")
def spark_session():
    # spark_env = True if os.getenv("DATABRICKS_RUNTIME_VERSION") is not None else False

    if os.getenv("DATABRICKS_RUNTIME_VERSION") is not None:
        return spark
    else:
        try:
            from databricks.connect import DatabricksSession
            from databricks.sdk.core import Config
            config = Config(profile=db_profile, cluster_id=db_cluster)
            return DatabricksSession.builder.sdkConfig(config).getOrCreate()
        except ModuleNotFoundError:
            from pyspark.sql import SparkSession
            return SparkSession.builder.getOrCreate()
def test_create_sample_dataframe_valid_df(spark_session):
    return_df = pyspark_functions.create_sample_dataframe(spark_session)
    assert return_df.count() == 2
    # assert isinstance(return_df, DataFrame)
    print("Completed test for create_sample_dataframe")

if __name__ == "__main__":
    # test_create_sample_dataframe_valid_df()
    print(pytest.main(["-p", "no:cacheprovider"]))
    