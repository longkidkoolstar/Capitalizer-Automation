@echo off
cd /d "%~dp0"

REM Check if Python is installed and in PATH
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not found. Please install Python and add it to your PATH.
    echo You can download it from https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Install dependencies if not already installed
pip install -r requirements.txt

REM Run the Python script
python capitalizer.py