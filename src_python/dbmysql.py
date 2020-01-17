import mysql.connector
import sys
import os
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from config import config

hostName = None
userName = None
userPwd  = None
userDb=None

if sys.platform=="darwin":
    os.system("clear")
    hostName=config.macMysql["host"]
    userName=config.macMysql["user"]
    userPwd=config.macMysql["pwd"]
    userDb=config.macMysql["database"]
else:
    os.system("cls")
    print("This script currently works with Mac OS only")

try:
    conn=mysql.connector.connect(host=hostName,user=userName,passwd=userPwd,database=userDb)
    cur=conn.cursor()
    cur.execute("select * from hr.countries")
    res = cur.fetchall()
    print(cur.description)
    print(res)
except Exception as e:
    print(e)
finally:
    if cur:
        cur.close()
    if conn:
        conn.close()