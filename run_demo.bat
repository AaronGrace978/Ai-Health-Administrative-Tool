@echo off
title Health Administrative Tool - Demo
color 0D

echo.
echo ================================================================
echo    🎮 Health Administrative Tool - System Demo
echo ================================================================
echo.

REM Set Python path
set PYTHON_PATH=C:\Users\AGrac\AppData\Local\Programs\Python\Python313\python.exe

REM Check if Python exists
if not exist "%PYTHON_PATH%" (
    echo ❌ Python not found at: %PYTHON_PATH%
    pause
    exit /b 1
)

echo ✅ Python found at: %PYTHON_PATH%
echo.

REM Check if we're in the right directory
if not exist "demo.py" (
    echo ❌ demo.py not found in current directory
    echo Please run this from the Health Administrative Tool directory.
    pause
    exit /b 1
)

echo ✅ Demo script found
echo.

REM Check if virtual environment exists and activate it
if exist "venv\Scripts\activate.bat" (
    echo 🔧 Activating virtual environment...
    call venv\Scripts\activate.bat
)

echo.
echo 🎯 This demo will showcase the Health Administrative Tool features:
echo.
echo • User registration and authentication
echo • Patient management with encrypted data
echo • Patient interaction tracking
echo • AI-powered insights and analysis
echo • Dashboard statistics and monitoring
echo • Document management capabilities
echo.
echo ⚠️ Make sure the backend server is running first!
echo.
echo Press any key to start the demo...
pause >nul

echo.
echo 🚀 Starting demo...
echo.

"%PYTHON_PATH%" demo.py

echo.
echo 🎉 Demo completed!
echo.
echo To start the full application, run: start_health_admin.bat
echo.
pause
