import pymongo
import json
import os
import sys
import urllib3
import requests
import pprint
import datetime
import bson
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from config import config

def getApiKey():
    res=requests.post(url=config.pardot_api_base_url+config.pardot_api_resources["login"], data=config.pardot_login_payload,proxies=config.cyProxy,verify=False)
    resJson=res.json()
    return resJson['api_key']

def loadPardotObj(apiResource,colName,monDb,resArray):
    #Connect to mongodb
    monCon=pymongo.MongoClient(config.mongo_connection)
    monDb=monCon[monDb]       
    monCol=monDb[colName]
    monCol.drop()
    #Disable SSL warnings
    urllib3.disable_warnings()
    #Get api key
    pardot_login_header=config.pardot_login_header
    pardot_login_header["api_key"]=getApiKey()
    offset=0
    res=requests.post(url=config.pardot_api_base_url+config.pardot_api_resources[apiResource]+"&offset="+str(offset),data=pardot_login_header,proxies=config.cyProxy,verify=False)
    resJson=res.json()
    try:
        
        while resJson['result'] is not None:
            try:
                res=requests.post(url=config.pardot_api_base_url+config.pardot_api_resources[apiResource]+"&offset="+str(offset),data=pardot_login_header,proxies=config.cyProxy,verify=False)
                resJson=res.json()
                monCol.insert_many(resJson['result'][resArray])
                print("# of rows - try=",monCol.count_documents({}),pardot_login_header['api_key'],res.status_code, offset,datetime.datetime.now().strftime('%H:%M') )
            except:
                pardot_login_header["api_key"]=getApiKey()
                res=requests.post(url=config.pardot_api_base_url+config.pardot_api_resources[apiResource]+"&offset="+str(offset),data=pardot_login_header,proxies=config.cyProxy,verify=False)
                resJson=res.json()
                monCol.insert_many(resJson['result'][resArray])
                print("# of rows - except=",monCol.count_documents({}),pardot_login_header['api_key'],res.status_code, offset,datetime.datetime.now().strftime('%H:%M') )
            offset=offset+200
    except Exception as e:
        print(res.text)
        #print("Exception Found",e)
    finally:
        #Close mongo connection
        monCon.close()


if __name__ == "__main__":
    loadPardotObj('opportunity','pd_opportunities','pardot','opportunity')
       
    
# #Load compaigns from pardot.
# res=requests.post(url=config.pardot_api_base_url+config.pardot_api_resources['campaign'],data=pardot_login_header,proxies=config.cyProxy,verify=False)
# resJson=res.json()
# #pprint.pprint(resJson)
# monCol=monDb.pd_campaigns
# monCol.drop()
# monCol.insert_many(resJson['result']['campaign'])
# print("# of rows=",monCol.count_documents({}))

# #Load prospects from pardot.
# monCol=monDb.pd_prospects
# monCol.drop()
# offset=0
# res=requests.post(url=config.pardot_api_base_url+config.pardot_api_resources['prospect']+"&offset="+str(offset),data=pardot_login_header,proxies=config.cyProxy,verify=False)
# resJson=res.json()
# while resJson['result'] is not None:
#     try:
#         res=requests.post(url=config.pardot_api_base_url+config.pardot_api_resources['prospect']+"&offset="+str(offset),data=pardot_login_header,proxies=config.cyProxy,verify=False)
#         resJson=res.json()
#         monCol.insert_many(resJson['result']['prospect'])
#         print("# of rows - try=",monCol.count_documents({}),pardot_login_header['api_key'],res.status_code, offset,datetime.datetime.now().strftime('%H:%M') )
#     except:
#         pardot_login_header["api_key"]=getApiKey()
#         res=requests.post(url=config.pardot_api_base_url+config.pardot_api_resources['prospect']+"&offset="+str(offset),data=pardot_login_header,proxies=config.cyProxy,verify=False)
#         resJson=res.json()
#         monCol.insert_many(resJson['result']['prospect'])
#         print("# of rows - except=",monCol.count_documents({}),pardot_login_header['api_key'],res.status_code, offset,datetime.datetime.now().strftime('%H:%M') )
#     offset=offset+200

# #Load visitors from pardot
# monCol=monDb.pd_visitors
# monCol.drop()
# offset=0
# res=requests.post(url=config.pardot_api_base_url+config.pardot_api_resources['visitor']+"&offset="+str(offset),data=pardot_login_header,proxies=config.cyProxy,verify=False)
# resJson=res.json()
# while resJson['result'] is not None:
#     try:
#         res=requests.post(url=config.pardot_api_base_url+config.pardot_api_resources['visitor']+"&offset="+str(offset),data=pardot_login_header,proxies=config.cyProxy,verify=False)
#         resJson=res.json()
#         monCol.insert_many(resJson['result']['visitor'])
#         print("# of rows - try=",monCol.count_documents({}),pardot_login_header['api_key'],res.status_code, offset,datetime.datetime.now().strftime('%H:%M') )
#     except:
#         pardot_login_header["api_key"]=getApiKey()
#         res=requests.post(url=config.pardot_api_base_url+config.pardot_api_resources['visitor']+"&offset="+str(offset),data=pardot_login_header,proxies=config.cyProxy,verify=False)
#         resJson=res.json()
#         monCol.insert_many(resJson['result']['visitor'])
#         print("# of rows - except=",monCol.count_documents({}),pardot_login_header['api_key'],res.status_code, offset,datetime.datetime.now().strftime('%H:%M') )
#     offset=offset+200


#Load prospectAccount from pardot
# monCol=monDb.pd_prospect_accounts
# monCol.drop()
# offset=0
# res=requests.post(url=config.pardot_api_base_url+config.pardot_api_resources['prospectAccount']+"&offset="+str(offset),data=pardot_login_header,proxies=config.cyProxy,verify=False)
# resJson=res.json()
# try:
#     while resJson['result'] is not None:
#         try:
#             res=requests.post(url=config.pardot_api_base_url+config.pardot_api_resources['prospectAccount']+"&offset="+str(offset),data=pardot_login_header,proxies=config.cyProxy,verify=False)
#             resJson=res.json()
#             monCol.insert_many(resJson['result']['prospectAccount'])
#             print("# of rows - try=",monCol.count_documents({}),pardot_login_header['api_key'],res.status_code, offset,datetime.datetime.now().strftime('%H:%M') )
#         except:
#             pardot_login_header["api_key"]=getApiKey()
#             res=requests.post(url=config.pardot_api_base_url+config.pardot_api_resources['prospectAccount']+"&offset="+str(offset),data=pardot_login_header,proxies=config.cyProxy,verify=False)
#             resJson=res.json()
#             monCol.insert_many(resJson['result']['prospectAccount'])
#             print("# of rows - except=",monCol.count_documents({}),pardot_login_header['api_key'],res.status_code, offset,datetime.datetime.now().strftime('%H:%M') )
#         offset=offset+200
# except:
#     print(res.text)
