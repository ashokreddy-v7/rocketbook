# Authors 	: Ashok Vennapusa & Srinivasulu Chenna
# Purpose : To Trigger VB Script to update CSV To Excel
# Date : 06/19/2018
# Python 3.6.5

import os
import OracleDBConnection as odbc_conn

def Trigger_VBScript():
    "This triggers Visual Basic Script to convert CSV to Excel"
    print("Execution VB Script...")
    csv_file =str(odbc_conn.csv_file_path)+str(odbc_conn.csv_file_name)
    xls_file =str(odbc_conn.xls_file_path)+str(odbc_conn.xls_file_name)
   # print(csv_file, xls_file)
    command = r"cscript D:\SPOProject_DEV\SPO\CSV_To_Excel.vbs "+csv_file+" "+xls_file
   # print(command)
    exit_code=os.system(command)
    return exit_code