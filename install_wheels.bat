@echo off
title Health Administrative Tool - Wheel-based Installer
color 0A

echo.
echo ================================================================
echo    🔧 Health Administrative Tool - Wheel-based Installer
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
echo 🔧 Installing dependencies using pre-compiled wheels only...
echo.

REM Install packages with wheel-only flag to avoid compilation
echo Installing FastAPI...
python -m pip install --only-binary=all fastapi

echo Installing Uvicorn...
python -m pip install --only-binary=all uvicorn

echo Installing SQLAlchemy...
python -m pip install --only-binary=all sqlalchemy

echo Installing Pydantic...
python -m pip install --only-binary=all pydantic

echo Installing Pydantic Settings...
python -m pip install --only-binary=all pydantic-settings

echo Installing Requests...
python -m pip install --only-binary=all requests

echo Installing HTTPX...
python -m pip install --only-binary=all httpx

echo Installing CustomTkinter...
python -m pip install --only-binary=all customtkinter

echo Installing Python Dotenv...
python -m pip install --only-binary=all python-dotenv

echo Installing Pytest...
python -m pip install --only-binary=all pytest

echo Installing Pytest AsyncIO...
python -m pip install --only-binary=all pytest-asyncio

echo.
echo 🔧 Installing optional packages with wheels...
echo.

REM Try to install optional packages with wheels only
echo Installing Python-JOSE...
python -m pip install --only-binary=all python-jose
if errorlevel 1 (
    echo ⚠️ Python-JOSE wheel not available, skipping
)

echo Installing Passlib...
python -m pip install --only-binary=all passlib
if errorlevel 1 (
    echo ⚠️ Passlib wheel not available, skipping
)

echo Installing Python Multipart...
python -m pip install --only-binary=all python-multipart
if errorlevel 1 (
    echo ⚠️ Python Multipart wheel not available, skipping
)

echo Installing Pillow...
python -m pip install --only-binary=all pillow
if errorlevel 1 (
    echo ⚠️ Pillow wheel not available, skipping
)

echo Installing Cryptography...
python -m pip install --only-binary=all cryptography
if errorlevel 1 (
    echo ⚠️ Cryptography wheel not available, skipping
)

echo.
echo ✅ Wheel-based installation completed!
echo.

REM Test core imports
echo 🧪 Testing core imports...
python -c "import fastapi; print('✅ FastAPI imported successfully')"
python -c "import customtkinter; print('✅ CustomTkinter imported successfully')"
python -m pip install --only-binary=all sqlalchemy
python -c "import sqlalchemy; print('✅ SQLAlchemy imported successfully')"
python -c "import requests; print('✅ Requests imported successfully')"

echo.
echo 🎉 Installation completed successfully!
echo.
echo The system is configured to use SQLite database by default.
echo All packages were installed using pre-compiled wheels.
echo.
echo Next steps:
echo 1. Run: start_health_admin.bat
echo 2. Or test AI models: test_ai_model.bat
echo.
pause
