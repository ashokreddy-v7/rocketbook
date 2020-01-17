# Authors 	: Ashok Vennapusa & Srinivasulu Chenna
# Purpose : To Post file to Sharepoint Online and also Update List using REST API
# Date : 06/19/2018
# Python 3.6.5
#--------------------------------------
# !!!This will post file to SPO Dev site
#--------------------------------------

import SharepointSession as sp_sess
import OracleDBConnection as odbc_conn
import CSVToExcel as csvxls_conv
import json
import datetime
import sys
import os
job_start_time = datetime.datetime.now()

sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from config import config

def postfile():
    "This Posts file to Sharepoint"
    print("Posting File to Sharepoint")
    srcfile = odbc_conn.xls_file_path+odbc_conn.xls_file_name
    file_obj = open(srcfile, "rb")
    file_content = file_obj.read()
    base_url = config.spo_base_url
    folder_url = r"('"+odbc_conn.spo_lib_path+"')/Files/add(url='"+odbc_conn.xls_file_name+"',overwrite=true)"
    post_url = base_url+folder_url
    file_obj.close()
    try:
        sess.post(post_url, data=file_content, proxies=sp_sess.proxies)
        print("File posted to Sharepoint successfully")
    except Exception as e:
        print("Failed to post the file to Sharepoint")
        print(e)
        sys.exit(1)

def updateList():
    "This updates List Item in Sharepoint"
    print("Updating Sharepoint List")
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    excel_file = str(odbc_conn.xls_file_path) + str(odbc_conn.xls_file_name)
   # excel_update_time = datetime.datetime.fromtimestamp(os.path.getmtime(excel_file)).strftime('%Y/%m/%d %H:%M:%S')
    excel_file_size = round((os.path.getsize(excel_file) / 1024) / 1024,1)
    csv_file = str(odbc_conn.csv_file_path) + str(odbc_conn.csv_file_name)
    csv_update_time = str(datetime.datetime.fromtimestamp(os.path.getmtime(csv_file)).strftime('%Y/%m/%d %H:%M:%S'))
    body = json.dumps({"__metadata": {"type": "SP.Data."+odbc_conn.spo_list_name+"ListItem"}, "ReportOwner": odbc_conn.report_owner,"FileSize":str(excel_file_size)+"MB",
                       "Title": odbc_conn.report_title, "ReportID": report_ID,'ReportTimeZone':'CST-Austin,TX', 'ReportUpdateTime':csv_update_time,"LastUpdateStatus":"Success","Modified": current_time, 'DownloadLink': {
            '__metadata': {
                'type': 'SP.FieldUrlValue'
            },
            'Description': 'Download',
            'Url': odbc_conn.report_link,
        }})
    #print(body)
    try:
        get_listitem_url = config.spo_get_listitem_url+odbc_conn.spo_list_name+"')/items?$Filter=ReportID eq "+report_ID
        get_listitem_res = sess.get(get_listitem_url, proxies=sp_sess.proxies)
        data = get_listitem_res.json()
        if not data['d']['results']:
            insert_post_url = config.spo_get_listitem_url + odbc_conn.spo_list_name + "')/items"
            insert_post_res = sess.post(insert_post_url, data=body, proxies=sp_sess.proxies)
            # print(insert_post_res.text)
            return insert_post_res.status_code
        else:
            for each_item in data['d']['results']:
                SPO_ListItem_ID=str(each_item['Id'])
                update_post_url = config.spo_get_listitem_url + odbc_conn.spo_list_name + "')/items('" + SPO_ListItem_ID + "')"
                update_post_res = sess.post(update_post_url, data=body,
                                            headers={'X-HTTP-Method': 'MERGE', "IF-MATCH": "*"},
                                            proxies=sp_sess.proxies)
                # print(update_post_res.text)
                break
            return update_post_res.status_code
    except Exception as e:
        print("Failed to update Sharepoint list")
        print (e)
        sys.exit(1)

try:
    report_ID = sys.argv[1]
    odbc_conn.initializeReportDetails(report_ID)
except Exception as e:
    print(str(e))
    sys.exit(1)
try:
    status_code = csvxls_conv.Trigger_VBScript()
    if status_code != 0:
        sys.exit(1)
except Exception as e:
    print(str(e))
    sys.exit(1)
try:
    sess = sp_sess.getSharepointSession()
    postfile()
    if odbc_conn.archive_link!='Yes':
        status_code = updateList()
    if status_code == 201 or 204:
        last_update_status = "SUCCESS"
        last_update_status_desc = "SUCCESS"
    else:
        last_update_status = "FAILED"
        last_update_status_desc = "FAILED"
    job_end_time=datetime.datetime.now()
    print(status_code)
    odbc_conn.UpdateDetailsInTable(job_start_time,job_end_time,last_update_status,last_update_status_desc,report_ID)
except Exception as e:
    print(str(e))
    sys.exit(1)





