from pyspark.sql import Row, SparkSession
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
            .appName("SparkScratchPad.py") \
            .master("spark://10.198.129.113:7077") \
            .getOrCreate()
    
    sc=spark.sparkContext
    spark.sparkContext.setLogLevel("ERROR")

    linesRdd=sc.textFile(dataDir+"people.txt")
    partsRdd=linesRdd.map(lambda l:l.split(","))
    peopleRdd=partsRdd.map(lambda r:Row(name=r[0],age=int(r[1])))

    peopleDf=spark.createDataFrame(peopleRdd)

    peopleDf.createOrReplaceTempView("people")

    teensDf=spark.sql("select * from people where age<=19")

    peopleDf.show()
    teensDf.show()

    print(linesRdd.take(10))
    print(partsRdd.take(10))
    print(peopleRdd.take(10))

except Exception as e:
    print(e)

finally:
    print("Spark is using following config:")
    print(spark.sparkContext.getConf().getAll())
    if sc:
        sc.stop()
        print("sc object is stopped")
    if spark:
        spark.stop()
        print("spark object is stopped")

