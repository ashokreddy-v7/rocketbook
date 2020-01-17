import requests
import json
import os
import sys

sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from config import config
import pprint


# Put this in your config.py file

# avApiKey="your api key"
# avEndPoint="https://www.alphavantage.co/query?apikey="+avApiKey
# mySymbols=["msft","cy","aapl","enph"]
# avStockTimeSeries={"intraday":"&function=TIME_SERIES_INTRADAY&datatype=json&symbol=",\
#                    "daily":"&function=TIME_SERIES_DAILY&datatype=json&symbol=",\
#                      "dailyAdjusted":"&function=TIME_SERIES_DAILY_ADJUSTED&datatype=json&symbol=",\
#                          "weekly":"&function=TIME_SERIES_WEEKLY&datatype=json&symbol=",\
#                              "weeklyAdjusted":"&function=TIME_SERIES_WEEKLY_ADJUSTED&datatype=json&symbol=",\
#                                  "monthly":"&function=TIME_SERIES_MONTHLY&datatype=json&symbol=",\
#                                      "monthlyAdjusted":"&function=TIME_SERIES_MONTHLY_ADJUSTED&datatype=json&symbol=",\
#                                          "quoteEndPoint":"&function=GLOBAL_QUOTE&datatype=json&symbol="}

proxy=None

if sys.platform=="darwin":
    os.system("clear")
else:
    os.system("cls")
    proxy=config.cyProxy

reqUrl=config.avEndPoint+config.avStockTimeSeries["quoteEndPoint"]+"aapl"
res=requests.get(url=reqUrl,proxies=proxy)
resDict=res.json()
print(resDict)
pprint.pprint(res.json())
