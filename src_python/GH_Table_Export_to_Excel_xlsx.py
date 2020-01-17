#C:\Users\ahok\PycharmProjects\Python\GH_Table_Export_to_Excel_xlsx.py
# Script to connect to Oracle DB, runs a query and post results to excel 2007+ (xlsx) file.
# April 3, 2017
# Python - 3.5.4

import cx_Oracle
import xlsxwriter
import datetime

select_clause = "select * from "
table_name = "calendar"
where_clause = ""#where col1 ='xvz'"
order_clause = ""#order by col1 asc"

# Prepare SQl statement
sqlCommand = select_clause + " " + table_name + " " + where_clause + " " + order_clause
print("sqlCommand = ", sqlCommand)

# Connection to Oracle DB

dbcon = cx_Oracle.connect("username/password@tns_file_entry")

cursor = dbcon.cursor()
printHeader = True
# Execute SQL command and extract results
sqlResult = cursor.execute(sqlCommand)

# Create excel workbook
workbook = xlsxwriter.Workbook("C:\\Users\\ahok\\Desktop\\Temp\\"+table_name+".xlsx")
# Add excel sheet to above workbook
worksheet = workbook.add_worksheet(table_name)
# Setting formats
num_format = workbook.add_format({'num_format': '###0.####'})
date_format = workbook.add_format({'num_format': 'm/d/yyyy h:mm:ss'})

row = 0
col = 0
# Add column headers if requested
start_time = (datetime.datetime.now())
print("Export started at = ", start_time)
print("Exporting Header...")
if printHeader:
    header = []
    for header in cursor.description:
        worksheet.write(row, col, header[0])
        col = col+1
print("Header Exported")
print("Exporting Rows...")
# Add data
row = 1
col = 0
for tupple_row in sqlResult:
    col = 0
    for list_item in tupple_row:
        tab_desc = []
        tab_desc = cursor.description[col]
        # Get column data type
        col_data_type = str(tab_desc[1])
        #print(list_item)
        # If cell value is blank then insert blank. Can add more
        if list_item is None:
            worksheet.write_blank(row, col, None)
        # If cell value is data then format date time
        elif col_data_type.find("DATETIME") > 0:
            worksheet.write_datetime(row, col, list_item, date_format)
        # If cell value is Number then format date time
        elif col_data_type.find("NUMBER") > 0:
            worksheet.write_number(row, col, list_item)
        # String
        else:
            worksheet.write(row, col, list_item)
        col = col + 1
    row = row + 1
workbook.close()
print("Rows Exported. Total rows = ", row-1)
end_time = (datetime.datetime.now())
print("Export completed at = ", end_time)
print("Export duration = ", end_time-start_time)
cursor.close()


