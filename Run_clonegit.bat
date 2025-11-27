@echo off
set repo=https://github.com/Sommanatw/AI_Invoice_Extract.git
mkdir "D:\AI_Invoice_Extract"
set target="D:\AI_Invoice_Extract"

echo Pulling repository from %repo% to %target%
git clone %repo% %target%
echo Repository cloned successfully.



pause
