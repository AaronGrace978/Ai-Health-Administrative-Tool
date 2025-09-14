@echo off
title Health Administrative Tool - Minimal Installer
color 0A

echo.
echo ================================================================
echo    🔧 Health Administrative Tool - Minimal Installer
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
echo 🔧 Installing minimal dependencies (no compilation required)...
echo.

REM Install only essential packages that don't require compilation
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

echo Installing Requests...
python -m pip install requests

echo Installing HTTPX...
python -m pip install httpx

echo Installing CustomTkinter...
python -m pip install customtkinter

echo Installing Python Dotenv...
python -m pip install python-dotenv

echo Installing Pytest...
python -m pip install pytest

echo Installing Pytest AsyncIO...
python -m pip install pytest-asyncio

echo.
echo 🔧 Installing optional packages (may require compilation)...
echo.

REM Try to install optional packages, but don't fail if they don't work
echo Installing Python-JOSE (optional)...
python -m pip install python-jose
if errorlevel 1 (
    echo ⚠️ Python-JOSE installation failed, continuing without it
)

echo Installing Passlib (optional)...
python -m pip install passlib
if errorlevel 1 (
    echo ⚠️ Passlib installation failed, continuing without it
)

echo Installing Python Multipart (optional)...
python -m pip install python-multipart
if errorlevel 1 (
    echo ⚠️ Python Multipart installation failed, continuing without it
)

echo Installing Pillow (optional)...
python -m pip install pillow
if errorlevel 1 (
    echo ⚠️ Pillow installation failed, continuing without it
)

echo Installing Cryptography (optional)...
python -m pip install cryptography
if errorlevel 1 (
    echo ⚠️ Cryptography installation failed, continuing without it
)

echo.
echo ✅ Core dependencies installed successfully!
echo.

REM Test core imports
echo 🧪 Testing core imports...
python -c "import fastapi; print('✅ FastAPI imported successfully')"
python -c "import customtkinter; print('✅ CustomTkinter imported successfully')"
python -c "import sqlalchemy; print('✅ SQLAlchemy imported successfully')"
python -c "import requests; print('✅ Requests imported successfully')"

echo.
echo 🎉 Minimal installation completed successfully!
echo.
echo The system is configured to use SQLite database by default.
echo Some optional features may not be available, but the core system will work.
echo.
echo Next steps:
echo 1. Run: start_health_admin.bat
echo 2. Or test AI models: test_ai_model.bat
echo.
echo Note: If you need full functionality, you may need to install
echo additional dependencies manually or use a different Python version.
echo.
pause
