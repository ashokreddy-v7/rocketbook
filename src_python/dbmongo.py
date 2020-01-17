import pymongo
import sys
import os
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from config import config

host=None
database=None

if sys.platform=="darwin":
    os.system("clear")
    host=config.macMongoClient["host"]
    database=config.macMongoClient["database"]
    print(host,database)
else:
    os.system("cls")
try:
    conn=pymongo.MongoClient(host)
    db=conn[database]
    coll=db.list_collection_names()
    print(coll)
except Exception as e:
    print(e)
finally:
    conn.close()