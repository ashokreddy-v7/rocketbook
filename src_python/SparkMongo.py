from pyspark.sql import SparkSession
import os
import sys
import socket
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from config import config

# Start spark master and get master Url: spark-class org.apache.spark.deploy.master.Master
# Start spark worker 1 on available port: spark-class org.apache.spark.deploy.worker.Worker spark://10.20.40.143:7077 --cores 1 --memory 1G --port 63374
# Start spark worker 2 on available port : spark-class org.apache.spark.deploy.worker.Worker spark://10.20.40.143:7077 --cores 1 --memory 1G --port 63375
# Submit spark code : spark-submit --master spark://10.20.40.143:7077  src_python/SparkMongo.py


dataDir=None

if sys.platform=="darwin":
    dataDir=config.macDataDir
else:
    dataDir=config.cyDataDir
print(socket.gethostbyname(socket.gethostname()))
sparkMasterUrl="spark://"+str(socket.gethostbyname(socket.gethostname()))+":7077"

try:
    spark=SparkSession \
        .builder \
        .appName(__file__) \
        .master(sparkMasterUrl) \
        .getOrCreate()

    spark.sparkContext.setLogLevel("ERROR") # Try INFO

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