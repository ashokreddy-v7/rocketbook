from sqlalchemy import INTEGER, VARCHAR, DATE, FLOAT
import pymongo
import sqlalchemy as rdb
import pandas
import json
import pprint
import urllib3
import requests
import os
import time
import sys
import io
import zipfile
import glob
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import config

urllib3.disable_warnings()

############### MongoDB Section ########################################

mon_conn=pymongo.MongoClient(config.mongo_connection)
mon_db=mon_conn.qualtrics

# #Load directories to qt_directories of MongoDB/NoSQL
# res=requests.get(url=config.qualtrics_base_url+config.qualtrics_api_dict['dirs'],headers=config.qualtrics_login_header,proxies=config.cyProxy,verify=False)
# resJson=res.json()
# mon_col=mon_db.qt_directories
# mon_col.drop()
# #for d in resJson['result']['elements']:
# mon_col.insert_many(resJson['result']['elements'])
# print(mon_col.name + "-number of documents=",mon_col.count_documents({}))
# list_of_dirs=list(mon_col.find({},{"directoryId" : 1,"_id":0}))
# #print(list_of_dirs)

# #Load directory contacts to qt_dir_contacts of MongoDB/NoSQL. Loop each directory
# mon_col=mon_db.qt_dir_contacts
# mon_col.drop()
# for dr in list_of_dirs:
#     res=requests.get(url=(config.qualtrics_base_url+config.qualtrics_api_dict['contacts']).format(dr['directoryId']),headers=config.qualtrics_login_header,proxies=config.cyProxy,verify=False)
#     resJson=res.json()
#     nextPage=resJson['result']['nextPage']
#     while True:
#         if nextPage==None or nextPage=='None' or len(nextPage)<10:
#             break
#         mon_col.insert_many(resJson['result']['elements'])
#         res=requests.get(url=nextPage,headers=config.qualtrics_login_header,proxies=config.cyProxy,verify=False)
#         resJson=res.json()
#         nextPage=resJson['result']['nextPage']
# print(mon_col.name + "-number of documents=",mon_col.count_documents({}))

# #Load Surveys to qt_surveys of MongoDB/NoSQL
# res=requests.get(url=config.qualtrics_base_url+config.qualtrics_api_dict['surveys'],headers=config.qualtrics_login_header,proxies=config.cyProxy,verify=False)
# resJson=res.json()
# mon_col=mon_db.qt_surveys
# mon_col.drop()
# mon_col.insert_many(list(resJson['result']['elements']))
# print(mon_col.name + "-number of documents=",mon_col.count_documents({}))
# list_of_surveys=list(mon_col.find({},{"id":1,"name":2,"_id":0}))
# #print(list_of_surveys)

# #Load Surveys to qt_surveys of MongoDB/NoSQL. Load Each Survey Header
# mon_col=mon_db.qt_survey_responses
# mon_col.drop()
# print("start looping:")
# for sid in list_of_surveys:
#     print(mon_col.name + "-number of documents=",mon_col.count_documents({}))
#     #print((config.qualtrics_base_url+config.qualtrics_api_dict['survey_response']).format(sid['id']))
#     res=requests.post(url=(config.qualtrics_base_url+config.qualtrics_api_dict['survey_response']).format(sid['id']),headers=config.qualtrics_login_header,data=json.dumps(config.qualtrics_post_body),proxies=config.cyProxy,verify=False)
#     progessId=res.json()["result"]["progressId"]
#     #print((config.qualtrics_base_url+config.qualtrics_api_dict['survey_response']+progessId).format(sid['id']))
#     res=requests.get(url=(config.qualtrics_base_url+config.qualtrics_api_dict['survey_response']+"/"+progessId).format(sid['id']),headers=config.qualtrics_login_header,proxies=config.cyProxy,verify=False)
#     downloadStatus=res.json()["result"]["status"]
#     while downloadStatus!="complete" and downloadStatus!="failed":
#         res=requests.get(url=(config.qualtrics_base_url+config.qualtrics_api_dict['survey_response']+"/"+progessId).format(sid['id']),headers=config.qualtrics_login_header,proxies=config.cyProxy,verify=False)
#         downloadStatus=res.json()["result"]["status"]
#         #print(downloadStatus)
#         time.sleep(5)
#     #pprint.pprint(res.json())

#     fileId=res.json()["result"]["fileId"]
#     # print((config.qualtrics_base_url +
#     #     config.qualtrics_api_dict['survey_response']+fileId+"/file").format(sid['id']))

#     res = requests.get(url=(config.qualtrics_base_url+config.qualtrics_api_dict['survey_response']+fileId+"/file").format(
#         sid['id']), headers=config.qualtrics_login_header, proxies=config.cyProxy, verify=False,stream=True)


#     data_dir=os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))+"\\data\\survey_responses\\"
#     zipfile.ZipFile(io.BytesIO(res.content)).extractall(path=data_dir)
#     unzip_json_file=data_dir+sid['name']+".json"
#     print(unzip_json_file)

#     with open(unzip_json_file,'r',encoding="utf-8") as res_file:
#         resJson=json.load(res_file)
#         mon_col.insert_many(resJson['responses'])
#         print(mon_col.name + "-number of documents=",mon_col.count_documents({}))
#     os.remove(unzip_json_file)
#     time.sleep(5)
# print(mon_col.name + "-number of documents=",mon_col.count_documents({}))

#Get users list

res=requests.get(url=config.qualtrics_base_url+config.qualtrics_api_dict['groups'],headers=config.qualtrics_login_header,proxies=config.cyProxy,verify=False)
print(res.text)

mon_conn.close()

############### OracleDB Section ########################################

# Load Survey Headers to qt_surveys Oracle
# res=requests.get(url=config.qualtrics_base_url+config.qualtrics_survey_api,headers=config.qualtrics_login_header,proxies=config.cyProxy,verify=False)
# resJson=res.json()
# data=list(resJson['result']["elements"])
# df=pandas.DataFrame(data)
# engine=db.create_engine(config.cyOraThinConn,implicit_returning=False)
# ora_conn=engine.connect()
# type_mapping={'creationDate':VARCHAR(255), 'id': VARCHAR(255), 'isActive': VARCHAR(255), 'lastModified': VARCHAR(255), 'name': VARCHAR(255), 'ownerId': VARCHAR(255)}
# df.to_sql(name='qt_surveys',con=ora_conn,if_exists='replace',dtype=type_mapping)
# ora_conn.close()

# Load directories to qt_directories - WORKING
# res=requests.get(url=config.qualtrics_base_url+config.qualtrics_dir_api,headers=config.qualtrics_login_header,proxies=config.cyProxy,verify=False)
# resJson=res.json()
# data=list(resJson['result']['elements'])
# df=pandas.DataFrame(data)[['directoryId','name']]
# engine=db.create_engine(config.cyOraThinConn,implicit_returning=False)
# ora_conn=engine.connect()
# type_mapping={'directoryId':VARCHAR(255),'name':VARCHAR(255)}
# df.to_sql(name='qt_directories',con=ora_conn,if_exists='replace',dtype=type_mapping)
# ora_conn.close()

# Load contacts  from each of the directories pulled - WORKING
# dirs=df['directoryId'].tolist()
# for d in dirs:
#     print(config.qualtrics_base_url+config.qualtrics_dir_api+d+"/contacts/")
#     res=requests.get(url=config.qualtrics_base_url+config.qualtrics_dir_api+d+"/contacts",headers=config.qualtrics_login_header,proxies=config.cyProxy,verify=False)
#     resJson=res.json()
#     nextPage=resJson['result']['nextPage']
#     #df=pandas.DataFrame(data)[['contactId','email','extRef','firstName','lastName','language','phone']]
#     while True:
#         print(nextPage)
#         if nextPage==None:
#             break
#         res=requests.get(url=nextPage,headers=config.qualtrics_login_header,proxies=config.cyProxy,verify=False)
#         resJson=res.json()
#         nextPage=resJson['result']['nextPage']


# Initiate Download. progressId should be in output
# res=requests.post(url=config.qualtrics_post_url,headers=config.qualtrics_post_header,data=json.dumps(config.qualtrics_post_body),proxies=config.cyProxy,verify=False)
# pprint.pprint(res.json())

# Check download status. progressId should be input. fileId and percentComplete should be output
# res=requests.get(url=config.qualtrics_post_url+"/<progressId>",headers=config.qualtrics_get_header,proxies=config.cyProxy,verify=False)
# pprint.pprint(res.json())

# Download the file. fileId should be input.
# print(config.qualtrics_post_url+'/<fileId?'+"/file -o responses.zip")
# res=requests.get(url=config.qualtrics_post_url+'/<fileId>"/file/",headers=config.qualtrics_post1_header,proxies=config.cyProxy,verify=False)
# print(res.text)
