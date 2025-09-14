@echo off
title Health Administrative Tool - Backend Server
color 0A

echo.
echo ================================================================
echo    🚀 Health Administrative Tool - Backend Server
echo ================================================================
echo.

REM Check if virtual environment exists
if not exist "venv\Scripts\python.exe" (
    echo ❌ Virtual environment not found
    echo.
    echo Please run: install_complete_fix.bat first
    pause
    exit /b 1
)

echo ✅ Virtual environment found
echo.

REM Use virtual environment Python directly
set VENV_PYTHON=venv\Scripts\python.exe

echo 🚀 Starting backend server...
echo 📊 Backend will be available at: http://localhost:8000
echo 📖 API Documentation: http://localhost:8000/api/docs
echo.
echo 💡 Press Ctrl+C to stop the server
echo.

"%VENV_PYTHON%" main.py

echo.
echo 👋 Backend server stopped.
pause