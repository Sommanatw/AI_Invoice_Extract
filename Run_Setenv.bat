@echo off

echo Python Virtual Environment...
python -m venv env
echo Python Virtual Environment... Created.
echo Activating Virtual Environment...
call env\Scripts\activate.bat
echo Virtual Environment Activated.
echo Installing Required Packages...
pip install -r requirements.txt
echo Required Packages Installed.


pause
