from pyspark.sql import SparkSession
import os
import sys
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from config import config

appName=os.path.basename(__file__)

dataDir=None

if sys.platform=="darwin":
    dataDir=config.macDataDir
else:
    dataDir=config.cyDataDir

try:
    spark=SparkSession \
      .builder \
      .appName(appName) \
      .getOrCreate()

    spark.sparkContext.setLogLevel("ERROR")

    usersDf=spark.read.parquet(dataDir+"users.parquet")
    usersDf.select("name","favorite_color").write.parquet(dataDir+"userscolor.parquet",mode="overwrite")

    peopleDf=spark.read.csv(dataDir+"people.csv",inferSchema=True,sep=":",header=True)
    peopleDf.show()

    usersDf.show()
    usersDf.write.partitionBy("favorite_color").bucketBy(42, "name").saveAsTable("people_partitioned_bucketed")


except Exception as e:
    print(e)

finally:
    if spark:
        spark.stop()

