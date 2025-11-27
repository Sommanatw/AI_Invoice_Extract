@echo off

echo Python Virtual Environment...
cd D:\AI_Invoice_Extract
call python -m venv env
echo Python Virtual Environment... Created.
echo Activating Virtual Environment...
call D:\AI_Invoice_Extract\env\Scripts\activate.bat
echo Virtual Environment Activated.
echo Installing Required Packages...
call python -m pip install -r D:\AI_Invoice_Extract\requirements.txt
echo Required Packages Installed.


pause
