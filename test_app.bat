@echo off
title Test Health Administrative Tool
color 0A

echo.
echo ================================================================
echo    🧪 Testing Health Administrative Tool
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

echo 🔧 Testing all imports...
echo.

echo Testing FastAPI...
"%VENV_PYTHON%" -c "import fastapi; print('✅ FastAPI imported successfully')"
if errorlevel 1 (
    echo ❌ FastAPI import failed
    pause
    exit /b 1
)

echo Testing CustomTkinter...
"%VENV_PYTHON%" -c "import customtkinter; print('✅ CustomTkinter imported successfully')"
if errorlevel 1 (
    echo ❌ CustomTkinter import failed
    pause
    exit /b 1
)

echo Testing SQLAlchemy...
"%VENV_PYTHON%" -c "import sqlalchemy; print('✅ SQLAlchemy imported successfully')"
if errorlevel 1 (
    echo ❌ SQLAlchemy import failed
    pause
    exit /b 1
)

echo Testing Pydantic...
"%VENV_PYTHON%" -c "import pydantic; print('✅ Pydantic imported successfully')"
if errorlevel 1 (
    echo ❌ Pydantic import failed
    pause
    exit /b 1
)

echo Testing email-validator...
"%VENV_PYTHON%" -c "import email_validator; print('✅ Email-validator imported successfully')"
if errorlevel 1 (
    echo ❌ Email-validator import failed
    pause
    exit /b 1
)

echo Testing python-jose...
"%VENV_PYTHON%" -c "import jose; print('✅ Python-JOSE imported successfully')"
if errorlevel 1 (
    echo ❌ Python-JOSE import failed
    pause
    exit /b 1
)

echo Testing passlib...
"%VENV_PYTHON%" -c "import passlib; print('✅ Passlib imported successfully')"
if errorlevel 1 (
    echo ❌ Passlib import failed
    pause
    exit /b 1
)

echo Testing cryptography...
"%VENV_PYTHON%" -c "import cryptography; print('✅ Cryptography imported successfully')"
if errorlevel 1 (
    echo ❌ Cryptography import failed
    pause
    exit /b 1
)

echo.
echo 🔧 Testing main module...
"%VENV_PYTHON%" -c "import main; print('✅ Main module imported successfully')"
if errorlevel 1 (
    echo ❌ Main module import failed
    pause
    exit /b 1
)

echo.
echo 🔧 Testing GUI imports...
"%VENV_PYTHON%" -c "from gui.main_gui import HealthAdminGUI; print('✅ GUI module imported successfully')"
if errorlevel 1 (
    echo ❌ GUI module import failed
    pause
    exit /b 1
)

echo.
echo ✅ All tests passed! The application is ready to use.
echo.
echo You can now run:
echo 1. launch_app.bat - to start the complete application
echo 2. Or manually: venv\Scripts\python.exe main.py (backend)
echo 3. Then: venv\Scripts\python.exe start_gui.py (GUI)
echo.
pause
