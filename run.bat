@REM run the main file
@REM turn echo off
@echo off
call venv\Scripts\python.exe src\main.py
if %ERRORLEVEL% NEQ 0 (
    echo Return code was not 0, uh oh -_- Please try again.
    exit /b 1
)
echo Successfully ran main.py
goto:EOF
```