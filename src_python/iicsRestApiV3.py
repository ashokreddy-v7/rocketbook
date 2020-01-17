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

loginEndPoint = 'https://dm-us.informaticacloud.com/saas/public/core/v3/login'
loginHeader = {'content-type': 'application/json', 'Accept': 'application/json'}
loginPayload= {'username': usr, 'password': pwd}

# Login into IICS API
res = requests.post(url=loginEndPoint,data=json.dumps(loginPayload),proxies=proxy, headers=loginHeader)
if res.status_code==200:
    print("Connection established suceessfully")
else:
    print("Connection isn't established")
res_json = res.json()
#pprint.pprint(res_json)

sessionId=res_json['userInfo']['sessionId']
baseApiUrl=res_json['products'][0]['baseApiUrl']
#print(sessionId + " " + baseApiUrl)

# Get data from IICS

dataEndPoint = baseApiUrl+'/public/core/v3/users'
dataHeader = {'content-type': 'application/json', 'Accept': 'application/json','INFA-SESSION-ID': sessionId}
res = requests.get(url=dataEndPoint,proxies=proxy, headers=dataHeader)
res_json = res.json()
#pprint.pprint(res_json)

for i in res_json:
    print("id = " + i['id'] + ", userName = " + i['userName'] + ", email = " + i['email']+ ", state = " + i['state'])


# dataPayLoad= {'id':'gKSKmGorkqydr9HYB5hz2V','state':'Enabled'}
# res = requests.post(url=dataEndPoint,headers=dataHeader,proxies=proxy,data=json.dumps(dataPayLoad))

# Logout from IICS API

logoutEndPoint = 'https://dm-us.informaticacloud.com/saas/public/core/v3/logout'
logoutHeader = {'content-type': 'application/json', 'Accept': 'application/json','INFA-SESSION-ID': sessionId}
res = requests.post(url=logoutEndPoint,proxies=proxy, headers=logoutHeader)
if res.status_code==200:
    print("Connection closed suceessfully")
else:
    print("Connection isn't closed")
            

