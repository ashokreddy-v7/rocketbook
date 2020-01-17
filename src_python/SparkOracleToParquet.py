# to run code : spark-submit --master spark://172.24.28.73:7077 --jars .\jars\ojdbc7.jar SparkOracleToParquet.py
from pyspark.sql import SparkSession
import sys
import os

sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from config import config

oraConnJdbcThin=None
dataDir=None

if sys.platform=="darwin":
    os.system("clear")
    oraConnJdbcThin=config.macOraConnJdbcThin
    dataDir=config.macDataDir
else:
    os.system("cls")
    oraConnJdbcThin=config.cyOraConnJdbcThin
    dataDir=config.cyDataDir

spark = SparkSession \
    .builder \
    .appName("SparkOracleToParquet") \
    .getOrCreate()

print("########### read jdbc data ##############")
dfJdbc = spark \
    .read \
    .format("jdbc") \
    .options(url=oraConnJdbcThin,dbtable="emp", driver="oracle.jdbc.OracleDriver") \
    .load()
print("########### print jdbc data ##############")
print(dfJdbc.show())

print("########### convert dataframe to parquet ##############")
dfJdbc.write.parquet(dataDir+"emp.parquet",mode="overwrite")

print("########### read parquet data ##############")
dfParquet=spark.read.parquet(dataDir+"emp.parquet")
print("########### print jdbc data ##############")
print(dfParquet.show())

