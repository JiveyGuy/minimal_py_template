@REM turn echo off
@echo off

@REM === MAIN SCRIPT ===
echo Installing python virtual environment
call:check_requirements
call:create_virtualenv
@REM create virtual environment
goto:EOF

@REM === FUNCTIONS ===
@REM this function creates a virtual environment
:create_virtualenv

@REM check if venv folder exists
if exist venv (
    @REM ask if user wants to install over old local venv using choice
    @REM if they do then rmdir that folder and continue, else exit
    choice /M "venv folder already exists. Do you want to install over it?"
    if %ERRORLEVEL% NEQ 1 (
        echo removing old venv folder
        @REM let user know if successful or not
        rmdir venv /s /q >nul 2>&1 && (
            echo Successfully removed old venv folder
        ) || (
            echo Failed to remove old venv folder. Please try again.
            exit /b 1
        )
    ) else (
        echo Exiting due to no choice
        exit /b 1
    )
)

echo Creating virtual environment

@echo on
python -m venv venv 2>&1
@echo off
if %ERRORLEVEL% NEQ 0 (
    echo Failed to create virtual environment. Please try again.
    exit /b 1
)
echo Successfully created virtual environment

@REM install requirements.txt
echo Installing requirements.txt
@echo on
pip install -r requirements.txt 2>&1
@echo off
if %ERRORLEVEL% NEQ 0 (
    echo Failed to install requirements. Please try again.
    exit /b 1
)
echo Successfully installed requirements.txt
goto:EOF

@REM this function checks if we have our requirements
:check_requirements
@REM check if python is installed
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install python and try again.
    exit /b 1
)
echo Python is installed

@REM check if pip is installed
pip --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Pip is not installed. Please install pip and try again.
    exit /b 1
)
echo Pip is installed
goto:EOF
