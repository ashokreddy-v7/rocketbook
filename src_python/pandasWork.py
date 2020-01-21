import pandas as pd
import os

dfReviews=pd.read_csv('C:\\Users\\ahok\\Desktop\\GitHub\\rocketbook\\data\\ign.csv')
print(dfReviews.head())
print(dfReviews[['score_phrase','score']])


