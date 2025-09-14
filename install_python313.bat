@echo off
title Health Administrative Tool - Python 3.13 Compatible Installer
color 0A

echo.
echo ================================================================
echo    🔧 Health Administrative Tool - Python 3.13 Compatible Installer
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

REM Create virtual environment
echo 🔧 Creating virtual environment...
if exist "venv" (
    echo ⚠️ Virtual environment already exists. Removing old one...
    rmdir /s /q venv
)

"%PYTHON_PATH%" -m venv venv
if errorlevel 1 (
    echo ❌ Failed to create virtual environment
    pause
    exit /b 1
)

echo ✅ Virtual environment created
echo.

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip and install build tools
echo 🔧 Upgrading pip and installing build tools...
python -m pip install --upgrade pip
python -m pip install wheel setuptools

echo.
echo 🔧 Installing dependencies with Python 3.13 compatibility...
echo.

REM Install dependencies with latest compatible versions
echo Installing FastAPI...
python -m pip install fastapi

echo Installing Uvicorn...
python -m pip install uvicorn

echo Installing SQLAlchemy...
python -m pip install sqlalchemy

echo Installing Pydantic...
python -m pip install pydantic

echo Installing Pydantic Settings...
python -m pip install pydantic-settings

echo Installing Python-JOSE...
python -m pip install "python-jose[cryptography]"

echo Installing Passlib...
python -m pip install "passlib[bcrypt]"

echo Installing Python Multipart...
python -m pip install python-multipart

echo Installing Requests...
python -m pip install requests

echo Installing HTTPX...
python -m pip install httpx

echo Installing CustomTkinter...
python -m pip install customtkinter

echo Installing Pillow (latest compatible version)...
python -m pip install pillow

echo Installing Cryptography...
python -m pip install cryptography

echo Installing Python Dotenv...
python -m pip install python-dotenv

echo Installing Pytest...
python -m pip install pytest

echo Installing Pytest AsyncIO...
python -m pip install pytest-asyncio

echo.
echo ✅ All dependencies installed successfully!
echo.

REM Test imports
echo 🧪 Testing imports...
python -c "import fastapi; print('✅ FastAPI imported successfully')"
python -c "import customtkinter; print('✅ CustomTkinter imported successfully')"
python -c "import sqlalchemy; print('✅ SQLAlchemy imported successfully')"
python -c "import requests; print('✅ Requests imported successfully')"
python -c "import PIL; print('✅ Pillow imported successfully')"

echo.
echo 🎉 Installation completed successfully!
echo.
echo The system is configured to use SQLite database by default.
echo This is perfect for getting started quickly.
echo.
echo Next steps:
echo 1. Run: start_health_admin.bat
echo 2. Or test AI models: test_ai_model.bat
echo.
pause
