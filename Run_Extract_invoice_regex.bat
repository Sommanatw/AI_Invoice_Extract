@echo off
REM Activate Virtual Environment
call "D:\GIT\AI_Invoice_Extract\env\Scripts\activate.bat"

REM รันไฟล์ Python
python "D:\GIT\AI_Invoice_Extract\Extract_invoice_regex.py"

REM หยุดหน้าต่างไว้หลังรันเสร็จ
pause
