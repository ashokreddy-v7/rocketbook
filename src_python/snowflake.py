import snowflake.connector
import os
import sys
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from config import config

# Gets the version
ctx = snowflake.connector.connect(
    user=config.snowflakeUser,
    password=config.snowflakePwd,
    account=config.snowflakeAccount,
    region=config.snowflakeRegion
    )
cs = ctx.cursor()
try:
    cs.execute("SELECT current_version()")
    one_row = cs.fetchone()
    print(one_row[0])
finally:
    cs.close()
ctx.close()