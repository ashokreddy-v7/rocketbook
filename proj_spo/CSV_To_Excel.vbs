'======================================
' Authors 	: Ashok Vennapusa & Srinivasulu Chenna
' Purpose	: Convert CSV to XLSx. For more read memo AHOK-299
' Usage 	: CSV_To_Excel.vbs <report_id>. Report is should be in DW_CSV2EXCEL.DW_CSV_TO_EXCEL data warehouse table
' Debug 	: At command prompt type cscript <CSV_To_Excel.vbs(script name)> <argument>. Need Visual studio for this
'======================================
'Assign arguments to variables (source and target file details)
srccsvfile=Wscript.Arguments(0)
tgtxlsfile=Wscript.Arguments(1)

'Check if source file exists and get filetimestamp.
Set fso = CreateObject("Scripting.FileSystemObject")
If fso.FileExists(srccsvfile) Then
Set csv_file = fso.GetFile(srccsvfile)
csv_last_update_time =csv_file.DateLastModified
Wscript.echo("CSV Update Time :"&csv_last_update_time)
End If

Wscript.echo("Converting CSV to Excel...")

'On Error Resume Next ' Turn on the error handling flag
'Set objExcel = GetObject(,"Excel.Application")

'If not found, create a new instance.
'If Err.Number = 429 Then  '> 0
 Set objExcel = CreateObject("Excel.Application")
 Wscript.echo("Excel Application Object Created")
'End If

'On Error Goto 0

objExcel.Visible = false
objExcel.displayalerts=false

'Import CSV into Spreadsheet
On Error Resume Next
Set objWorkbook = objExcel.Workbooks.open(srccsvfile)
If Err.Number<>0 Then
Wscript.echo(Err.Description)
Wscript.Quit 1
End If
On Error Goto 0
Set objWorksheet = objWorkbook.Worksheets(1)

'Adjust width of columns to autofit
Set objRange = objWorksheet.UsedRange
objRange.EntireColumn.Autofit()

'Make Headings Bold
objExcel.Rows(1).Font.Bold = TRUE

'Freeze header row
With objExcel.ActiveWindow
     .SplitColumn = 0
     .SplitRow = 1
End With
objExcel.ActiveWindow.FreezePanes = True

'Add Data Filters to Heading Row
objExcel.Rows(1).AutoFilter

'set header row gray
objExcel.Rows(1).Interior.ColorIndex = 15

objExcel.Rows(1).Insert()
objExcel.Cells(1, 1).value = "Report Update Date : " & csv_last_update_time

'Save Spreadsheet, 51 = Excel 2007-2010 

Wscript.echo("Saving Excel File to Target location")

On Error Resume Next
objWorksheet.SaveAs tgtxlsfile, 51
If Err.Number <> 0 Then
Wscript.echo(Err.Description)
Wscript.echo("CSV to Excel conversion failed!!!")
Else 
Wscript.echo("CSV to Excel conversion successful")
End If
On Error Goto 0

'Check if excel timestamp is greater than csv timestamp
If fso.FileExists(tgtxlsfile) Then
Set xls_file = fso.GetFile(tgtxlsfile)
xls_last_update_time =xls_file.DateLastModified
End If

If csv_last_update_time > xls_last_update_time Then
    Wscript.Quit 1
End If

objWorkbook.Close

'Release Lock on Spreadsheet
objExcel.Quit
set objExcel=Nothing
set objWorksheet= Nothing
set objWorkbook = Nothing