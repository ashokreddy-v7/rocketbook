from pyspark.sql import SparkSession
import os
import sys

sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from config import config

sparekWarehouse=os.path.abspath("spark-warehouse")
appName=os.path.basename(__file__)
dataDir=None

if sys.platform=="darwin":
    dataDir=config.macDataDir
else:
    dataDir=config.cyDataDir

spark=SparkSession\
      .builder \
      .appName(appName) \
      .config("spark.sql.warehouse.dir",sparekWarehouse) \
      .enableHiveSupport() \
      .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

spark.sql("drop table if exists src")
spark.sql("create table if not exists src(key int, value string) using hive")
spark.sql("load data local inpath '"+dataDir+"\\kv1.txt' into table src")

spark.sql("select * from src").show()