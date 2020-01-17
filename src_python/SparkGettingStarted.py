from pyspark.sql import SparkSession
import os
import sys
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from config import config

dataDir=None

if sys.platform=="darwin":
    dataDir=config.macDataDir
else:
    dataDir=config.cyDataDir
try:
    spark=SparkSession \
        .builder \
        .appName(__file__) \
        .master("spark://10.198.129.113:7077") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("INFO")

# using dataframe api

    df=spark.read.json(dataDir+"people.json",multiLine=False)
    df.show()
    df.printSchema()
    df.select("name").show()
    df.select(df["name"],df["age"]+1).show()
    df.filter(df["age"]>18).show()
    df.groupBy(df["age"]).count().show()

# using sql api
    df.createOrReplaceTempView("people")
    sqlDf=spark.sql("select * from people")
    sqlDf.show()
    df.createOrReplaceGlobalTempView("people")
    spark.sql("select * from global_temp.people").show()
    spark.newSession().sql("select * from global_temp.people").show()

except Exception as e:
    print(e)

finally:
    conf = spark.sparkContext.getConf().getAll()
    print("Above app used following config:")
    for t in conf:
        print(t[0]+"="+t[1])
    spark.stop()