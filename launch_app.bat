@echo off
title Health Administrative Tool - Launch Application
color 0A

echo.
echo ================================================================
echo    🚀 Health Administrative Tool - Launch Application
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

echo 🔧 Testing dependencies in virtual environment...
"%VENV_PYTHON%" -c "import fastapi; print('✅ FastAPI imported successfully')"
if errorlevel 1 (
    echo ❌ FastAPI not available in virtual environment
    echo Please run: install_complete_fix.bat
    pause
    exit /b 1
)

"%VENV_PYTHON%" -c "import customtkinter; print('✅ CustomTkinter imported successfully')"
if errorlevel 1 (
    echo ❌ CustomTkinter not available in virtual environment
    echo Please run: install_complete_fix.bat
    pause
    exit /b 1
)

"%VENV_PYTHON%" -c "import main; print('✅ Main module imported successfully')"
if errorlevel 1 (
    echo ❌ Main module not available in virtual environment
    echo Please run: install_complete_fix.bat
    pause
    exit /b 1
)

echo.
echo 🔧 Starting backend server...
start "Health Admin Backend" cmd /k "%VENV_PYTHON%" main.py

echo.
echo ⏳ Waiting for backend to start...
timeout /t 5 /nobreak >nul

echo.
echo 🔧 Testing backend connection...
"%VENV_PYTHON%" -c "import requests; response = requests.get('http://localhost:8000/health', timeout=5); print('✅ Backend is running - Status:', response.status_code)"
if errorlevel 1 (
    echo ⚠️ Backend may still be starting, continuing anyway...
)

echo.
echo 🖥️ Starting GUI application...
"%VENV_PYTHON%" start_gui.py

echo.
echo 👋 Application closed.
pause
