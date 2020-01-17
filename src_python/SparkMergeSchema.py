from pyspark.sql import SparkSession, Row
import os
import sys
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from config import config

dataDir=None
appName=os.path.basename(__file__)

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
    
    sc=spark.sparkContext
    squaresDf=spark.createDataFrame(sc.parallelize(range(1,6)).map(lambda i: Row(single=i,double=i**2)))
    squaresDf.write.parquet(dataDir+"test_table/key=1",mode="overwrite")

    cubesDf=spark.createDataFrame(sc.parallelize(range(6,11)).map(lambda i: Row(single=i,triple=i**3)))
    cubesDf.show()
    cubesDf.write.parquet(dataDir+"test_table/key=2",mode="overwrite")

    mergedDf=spark.read.option("mergeSchema","true").parquet(dataDir+"test_table")
    mergedDf.printSchema()
    mergedDf.show()

except Exception as e:
    print(e)

finally:
    if sc:
        sc.stop()
    if spark:
        spark.stop()
