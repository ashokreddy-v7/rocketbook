from pyspark.sql import SparkSession
import os
import sys
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from config import config

# Clear console
if sys.platform=="darwin":
    os.system("clear")
else:
    os.system("cls")
    print("This script works with Unix like systems")
    sys.exit(1)

try:
    # Get sample data files from data directory
    dataDir="./data/search-engine-results-flights-tickets-keywords/"
    getAllFiles=os.listdir(dataDir)
    getCsvFiles=[]
    for f in getAllFiles:
        if f.endswith(".csv"):
            getCsvFiles.append(dataDir+f)


    # Create spark block
    spark=SparkSession.builder.appName("search-engine-results-flights-analysis").getOrCreate()
    spark.sparkContext.setLogLevel("WARN")
    csvDf=spark.read.text(getCsvFiles[0])
    # Count number of lines contains london
    cntLondonRows=csvDf.filter(csvDf.value.contains("london")).count()
    print("###########-----Output-------#########")
    # Print spark config
    print(spark.sparkContext.getConf().getAll())
    # Print number of lines contains london
    print(cntLondonRows)
    
except Exception as e:
    print("There are application errors. Please check logs for more")
    print(e)

finally:
    spark.stop()