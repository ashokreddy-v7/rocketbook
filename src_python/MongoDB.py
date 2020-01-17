import pymongo
import json
import os
import sys
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from config import config
conn = pymongo.MongoClient(config.mongo_connection)
db = conn.mydata
cols=db["qt_surveys"]
print(cols)
