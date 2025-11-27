@echo off
REM Activate Virtual Environment
call "D:\AI_Invoice_Extract\env\Scripts\activate.bat"

REM รันไฟล์ Python
python "D:\AI_Invoice_Extract\Extract_invoice_LLM.py"

REM หยุดหน้าต่างไว้หลังรันเสร็จ
pause
