# Author : Ashok Vennapusa
# Date : 02/21/2019
# Purpose: Connects to Infromatica Cloud Rest API and prints all DRS tasks in a given org to console
# Config - Makue sure proxy variable is set. This connects over annonmous proxy login

import requests
import os
import json
import pprint
import csv
import getpass

os.system("cls")

usr = input("Username::")
pwd = getpass.getpass("Password::")
prxy = input("proxy:port::")

proxy = {'https': prxy}

loginEndPoint = 'https://dm-us.informaticacloud.com/ma/api/v2/user/login'
loginHeader = {'content-type': 'application/json', 'Accept': 'application/json'}
loginPayload= {'@type':'login', 'username': usr, 'password': pwd}

# Login into IICS API
res = requests.post(url=loginEndPoint,data=json.dumps(loginPayload),proxies=proxy, headers=loginHeader)
if res.status_code==200:
    print("Connection established suceessfully")
else:
    print("Connection isn't established")
res_json = res.json()
icSessionId=res_json['icSessionId']
serverUrl=res_json['serverUrl']

# Get data from IICS

drsEndPoint = serverUrl+'/api/v2/task?type=DRS'
dataHeader = {'content-type': 'application/json', 'Accept': 'application/json','icSessionId':icSessionId}
res = requests.get(url=drsEndPoint,proxies=proxy, headers=dataHeader)
res_json = res.json()
#pprint.pprint(res_json)

for i in res_json:
    print("orgId = " + i['orgId'] + ", id = " + i['id']+ ", name = " + i['name']+ ", updateTime = " + i['updateTime']+ ", updatedBy = " + i['updatedBy'] )

# Logout from IICS API

logoutEndPoint = 'https://dm-us.informaticacloud.com/ma/api/v2/user/logout'
logoutHeader = {'content-type': 'application/json', 'Accept': 'application/json','icSessionId': icSessionId}
logoutPayload= {'@type':'logout'}
res = requests.post(url=logoutEndPoint,data=json.dumps(logoutPayload),proxies=proxy, headers=logoutHeader)
if res.status_code==200:
    print("Connection closed suceessfully")
else:
    print("Connection isn't closed")
            

