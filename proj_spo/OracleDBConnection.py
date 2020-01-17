# Authors 	: Ashok Vennapusa & Srinivasulu Chenna
# Purpose : Connection to Oracle table to retrieve rows and also update column values.
# Date : 06/19/2018
# Python 3.6.5

import cx_Oracle
import os
import datetime
import sys
from config import config

spo_base_link= config.spo_base_link
icsw_base_link= config.cyIcsFiler
report_title = None
report_link = None
archive_link = None
report_owner = None
csv_file_name = None
csv_file_path = None
xls_file_name = None
xls_file_path = None
spo_lib_path = None
spo_list_name = None

con_str = config.cyOraConnSpo
try:
    connection = cx_Oracle.connect(con_str)
    cursor = connection.cursor()
    print("Connected to Oracle DB")
except Exception as e:
    print("Cannot connect to Database")
    print(str(e))
    sys.exit(1)


def getReportDetails(ID):
    "This retrieves Report Details from Oracle Table"
    sql_command = u"SELECT * FROM ICS_SPO_VIEWER.DW_REPORTS_UPDATE_TIME WHERE REPORT_ID="+ID
   # print(sql_command)
    sql_result = cursor.execute(sql_command).fetchall()
   # print(sql_result)
    return sql_result

def initializeReportDetails(ID):
    "This initialises Report Details to Variables"
    print("Initialising Report Details")
    report_tuple=getReportDetails(ID)
    for each_item in report_tuple:
        global report_title
        global report_link
        global archive_link
        global report_owner
        global csv_file_name
        global csv_file_path
        global xls_file_name
        global xls_file_path
        global spo_list_name
        global spo_lib_path
        report_title = each_item[1]
        report_link = spo_base_link+str(each_item[2])
        archive_link = each_item[3]
        report_owner = each_item[4]
        csv_file_name = each_item[11]
        csv_file_path = icsw_base_link+str(each_item[12])
        xls_file_name = each_item[13]
        xls_file_path = icsw_base_link+str(each_item[14])
        spo_lib_path = each_item[15]
        spo_list_name = each_item[18]
        print(report_link)
        print(csv_file_path,csv_file_name)
        print(xls_file_path,xls_file_name)


def UpdateDetailsInTable(job_start_time,job_end_time,last_update_status,last_update_status_desc,report_id):
    "This writes back to Oracle table to update column details"
    print("Updating row in table...")
    excel_file = str(xls_file_path)+str(xls_file_name)
    excel_update_time=  str(datetime.datetime.fromtimestamp(os.path.getmtime(excel_file)).strftime('%Y/%m/%d %H:%M:%S'))
    csv_file = str(csv_file_path)+str(csv_file_name)
    csv_update_time = str(datetime.datetime.fromtimestamp(os.path.getmtime(csv_file)).strftime('%Y/%m/%d %H:%M:%S'))
    values = {'excel_update_time':excel_update_time,
              'job_start_time':job_start_time,
              'job_end_time':job_end_time,
              'csv_update_time':csv_update_time,
              'last_update_status':str(last_update_status),
              'last_update_status_desc':str(last_update_status_desc),
              'report_id':int(report_id)}
    sql_query = "UPDATE ICS_SPO_VIEWER.DW_REPORTS_UPDATE_TIME SET EXCEL_UPDATE_TIME = :excel_update_time," \
                "CSV_UPDATE_TIME = :csv_update_time, JOB_START_TIME = :job_start_time, JOB_END_TIME = :job_end_time," \
                "LAST_UPDATE_STATUS =:last_update_status, LAST_UPDATE_STATUS_DESC =:last_update_status_desc WHERE REPORT_ID = :report_id"
    cursor.execute(sql_query,values)
    connection.commit()
    cursor.close()
    connection.close()
