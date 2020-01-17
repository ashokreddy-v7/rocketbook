import snowflake.connector
import os
import sys
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from config import config

con=snowflake.connector.connect(user=config.snowflakeUser,password=config.snowflakePwd,account=config.snowflakeAccount,region=)
print(con)