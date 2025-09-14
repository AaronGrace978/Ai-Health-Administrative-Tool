@echo off
title Health Administrative Tool - Simple Launcher
color 0A

echo.
echo ================================================================
echo    🚀 Health Administrative Tool - Simple Launcher
echo ================================================================
echo.

REM Change to the script directory
cd /d "%~dp0"

REM Set Python path
set PYTHON_PATH=C:\Users\AGrac\AppData\Local\Programs\Python\Python313\python.exe

echo 🔍 Checking Python...
if not exist "%PYTHON_PATH%" (
    echo ❌ Python not found at: %PYTHON_PATH%
    echo.
    echo 💡 Please check your Python installation.
    pause
    exit /b 1
)

echo ✅ Python found
echo.

REM Check if virtual environment exists
if exist "venv\Scripts\python.exe" (
    echo ✅ Using virtual environment
    set PYTHON_CMD=venv\Scripts\python.exe
) else (
    echo ⚠️ No virtual environment, using system Python
    set PYTHON_CMD=%PYTHON_PATH%
)

echo.
echo 🚀 Starting Health Administrative Tool...
echo.

REM Try to start the application
"%PYTHON_CMD%" launch_gui_visible.py

echo.
echo 👋 Application closed.
pause
