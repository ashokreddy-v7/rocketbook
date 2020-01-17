# Authors 	: Ashok Vennapusa & Srinivasulu Chenna
# Purpose : To initiate a session with Sharepoint Online.
# Date : 06/19/2018
# Python 3.6.5

import sharepy
import urllib3
urllib3.disable_warnings()
import sys
import os
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from config import config

proxies = config.cyProxy

def getSharepointSession():
  "This creates session with sharepoint using SAML authentication"
  sess = sharepy.connect(config.spo_link,config.spo_user,config.spo_pwd)
  return sess