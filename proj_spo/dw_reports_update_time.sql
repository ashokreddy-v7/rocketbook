CREATE TABLE ICS_SPO_VIEWER.DW_REPORTS_UPDATE_TIME
(
  REPORT_ID                NUMBER,
  REPORT_TITLE             VARCHAR2(255 BYTE),
  REPORT_LINK              VARCHAR2(500 BYTE),
  ARCHIVE_LINK             VARCHAR2(500 BYTE),
  REPORT_OWNER             VARCHAR2(255 BYTE),
  EXCEL_UPDATE_TIME        VARCHAR2(80 BYTE),
  JOB_START_TIME           DATE,
  JOB_END_TIME             DATE,
  CSV_UPDATE_TIME          VARCHAR2(80 BYTE),
  COMMENTS                 VARCHAR2(255 BYTE),
  DOCUMENTATION            VARCHAR2(255 BYTE),
  CSV_FILE_NAME            VARCHAR2(255 BYTE),
  CSV_FILE_PATH            VARCHAR2(255 BYTE),
  EXCEL_FILE_NAME          VARCHAR2(255 BYTE),
  EXCEL_FILE_PATH          VARCHAR2(255 BYTE),
  SPO_LIB_PATH             VARCHAR2(255 BYTE),
  LAST_UPDATE_STATUS       VARCHAR2(255 BYTE),
  LAST_UPDATE_STATUS_DESC  VARCHAR2(255 BYTE),
  SPO_LIST_NAME            VARCHAR2(255 BYTE)
);

/* Sample Data - Space seperated

1	sm_sales_backlog_all	/dl_dw_etl_bi/sm_salesall-backlog/sm_sales_backlog_all.xlsx	No	cyne	2019/11/14 12:50:28	11/14/2019 12:49:52 PM	11/14/2019 12:52:19 PM	2019/11/14 12:49:10			sm_sales_backlog_all_csv.csv	\spo\sm_salesall-backlog\	sm_sales_backlog_all.xlsx	\spo\sm_salesall-backlog\	dl_dw_etl_bi/sm_salesall-backlog/	SUCCESS	SUCCESS	OMReports

*/