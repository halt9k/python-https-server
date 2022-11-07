REM set PYTHON_DIR=*
REM OpenSSL fix for Anacodna
REM SET PATH=%PATH%;%PYTHON_DIR%\Library\bin\
REM %PYTHON_DIR%\python.exe" https_server\file_server.py

python.exe https_server\file_server.py

set /p DUMMY=Hit ENTER to continue...