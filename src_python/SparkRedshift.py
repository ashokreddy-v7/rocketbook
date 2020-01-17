# To run spark-submit --master spark://localhost:7077 --jars ./jars/RedshiftJDBC42-no-awssdk-1.2.32.1056.jar SparkRedshift.py

from config import config
from pyspark.sql import SparkSession
import os
import sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

appName = os.path.basename(__file__)

spark = SparkSession \
    .builder \
    .appName(appName) \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

dfRs = spark.read.format("jdbc") \
    .option("driver", "com.amazon.redshift.jdbc42.Driver") \
    .option("url", config.redshiftJdbcUrl) \
    .option("dbtable", "information_schema.columns") \
    .option("user", config.rsUser) \
    .option("password", config.rsPwd) \
    .load()

dfRs.createOrReplaceTempView("columns")

spark.sql(
    "select table_catalog,table_schema,table_name,column_name from columns").show()
