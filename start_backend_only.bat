@echo off
title Health Administrative Tool - Backend Only
color 0A

echo.
echo ================================================================
echo    🚀 Health Administrative Tool - Backend Server
echo ================================================================
echo.

REM Use virtual environment Python directly
set VENV_PYTHON=venv\Scripts\python.exe

REM Check if virtual environment exists
if not exist "%VENV_PYTHON%" (
    echo ❌ Virtual environment not found
    echo Please run: install_complete_fix.bat first
    pause
    exit /b 1
)

echo ✅ Starting backend server...
echo.
echo 📊 Backend API: http://localhost:8000
echo 📖 API Docs: http://localhost:8000/api/docs
echo 🌐 Web Interface: http://localhost:8000
echo.
echo Press Ctrl+C to stop the server
echo.

"%VENV_PYTHON%" main.py

echo.
echo 👋 Backend server stopped.
pause
