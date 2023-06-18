@REM deactivate
@REM turn echo off
@echo off
call venv\Scripts\deactivate.bat
if %ERRORLEVEL% NEQ 0 (
    echo Failed to deactivate virtual environment. Please try again.
    exit /b 1
)
echo Successfully deactivated virtual environment
goto:EOF
```