from pyspark.sql import SparkSession
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
    
    jsonDf=spark.read.json(dataDir+"people.json")
    jsonDf.printSchema()

    peopleDf=jsonDf.createOrReplaceTempView("people")

    dfSql=spark.sql("select * from people") 

    dfSql.show()

    

except Exception as e:
    print(e)

finally:
    spark.stop()