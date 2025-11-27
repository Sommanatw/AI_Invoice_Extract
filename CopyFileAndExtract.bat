@echo off
set source=".\1251027022511-AI_Invoice_Extract\AI_Invoice_Extract.zip"
set destination="D:\AI_Invoice_Extract\AI_Invoice_Extract.zip"

mkdir "D:\AI_Invoice_Extract"

echo กำลังคัดลอกไฟล์...
copy %source% %destination%
echo เสร็จสิ้น!
pause
