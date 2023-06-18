@REM turn echo off
@echo off

@REM === MAIN SCRIPT ===
call:activate_virtualenv
goto:EOF

@REM === FUNCTIONS ===
@REM this function activates the virtual environment
:activate_virtualenv
call venv\Scripts\activate.bat
if %ERRORLEVEL% NEQ 0 (
    echo Failed to activate virtual environment. Please try again.
    exit /b 1
)
goto:EOF
```