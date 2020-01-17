#connect to oracle
import cx_Oracle
import sys
import os
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from config import config

#set oracle connection based on platform
oraTNS = None
if sys.platform=="darwin":
    oraTNS = config.macOraConn
    os.system("clear")
else:
    oraTNS = config.cyOraConn
    os.system("cls")

#connect to oracle
try:
    conn=cx_Oracle.connect(oraTNS)
    cur=conn.cursor()
    cur.execute("select * from emp")
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