import requests
import urllib3
import sys
import os

sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from config import config

urllib3.disable_warnings()

proxies = config.cyProxy

def Get_NewAutorizationKey():

    payload=config.jivePayload
    response=requests.post(config.jive_login_url,params=payload, proxies = proxies, verify = False)
    return response.text.strip()

