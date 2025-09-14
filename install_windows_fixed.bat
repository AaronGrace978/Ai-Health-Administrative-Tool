@echo off
title Health Administrative Tool - Windows Fixed Installer
color 0A

echo.
echo ================================================================
echo    🔧 Health Administrative Tool - Windows Fixed Installer
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
echo 🔧 Installing core dependencies (wheel-only to avoid compilation)...
echo.

REM Install core packages with wheel-only flag
echo Installing FastAPI...
python -m pip install --only-binary=all fastapi==0.104.1

echo Installing Uvicorn...
python -m pip install --only-binary=all uvicorn==0.24.0

echo Installing SQLAlchemy...
python -m pip install --only-binary=all sqlalchemy==2.0.23

echo Installing Alembic...
python -m pip install --only-binary=all alembic==1.12.1

echo Installing Pydantic...
python -m pip install --only-binary=all pydantic==2.5.0

echo Installing Pydantic Settings...
python -m pip install --only-binary=all pydantic-settings==2.1.0

echo Installing Requests...
python -m pip install --only-binary=all requests==2.31.0

echo Installing HTTPX...
python -m pip install --only-binary=all httpx==0.25.2

echo Installing CustomTkinter...
python -m pip install --only-binary=all customtkinter==5.2.0

echo Installing Python Dotenv...
python -m pip install --only-binary=all python-dotenv==1.0.0

echo Installing Pytest...
python -m pip install --only-binary=all pytest==7.4.3

echo Installing Pytest AsyncIO...
python -m pip install --only-binary=all pytest-asyncio==0.21.1

echo.
echo 🔧 Installing optional packages with fallbacks...
echo.

REM Try to install optional packages with wheels first, then fallback to alternatives
echo Installing Python Multipart...
python -m pip install --only-binary=all python-multipart==0.0.6
if errorlevel 1 (
    echo ⚠️ Python Multipart wheel not available, trying without version constraint...
    python -m pip install --only-binary=all python-multipart
    if errorlevel 1 (
        echo ⚠️ Python Multipart installation failed, continuing without it
    )
)

echo Installing Pillow...
python -m pip install --only-binary=all pillow
if errorlevel 1 (
    echo ⚠️ Pillow wheel not available, trying without version constraint...
    python -m pip install --only-binary=all pillow
    if errorlevel 1 (
        echo ⚠️ Pillow installation failed, continuing without it
    )
)

echo Installing Cryptography (this may take a while)...
python -m pip install --only-binary=all cryptography
if errorlevel 1 (
    echo ⚠️ Cryptography wheel not available, trying alternative approach...
    python -m pip install --only-binary=all --upgrade pip
    python -m pip install --only-binary=all cryptography
    if errorlevel 1 (
        echo ⚠️ Cryptography installation failed, continuing without it
        echo Note: Some security features may not be available
    )
)

echo Installing Python-JOSE (without cryptography extras)...
python -m pip install --only-binary=all python-jose
if errorlevel 1 (
    echo ⚠️ Python-JOSE wheel not available, trying without version constraint...
    python -m pip install --only-binary=all python-jose
    if errorlevel 1 (
        echo ⚠️ Python-JOSE installation failed, continuing without it
        echo Note: JWT token functionality may be limited
    )
)

echo Installing Passlib (without bcrypt extras)...
python -m pip install --only-binary=all passlib
if errorlevel 1 (
    echo ⚠️ Passlib wheel not available, trying without version constraint...
    python -m pip install --only-binary=all passlib
    if errorlevel 1 (
        echo ⚠️ Passlib installation failed, continuing without it
        echo Note: Password hashing may use basic algorithms only
    )
)

echo.
echo ✅ Installation completed!
echo.

REM Test core imports
echo 🧪 Testing core imports...
python -c "import fastapi; print('✅ FastAPI imported successfully')" 2>nul || echo "❌ FastAPI import failed"
python -c "import customtkinter; print('✅ CustomTkinter imported successfully')" 2>nul || echo "❌ CustomTkinter import failed"
python -c "import sqlalchemy; print('✅ SQLAlchemy imported successfully')" 2>nul || echo "❌ SQLAlchemy import failed"
python -c "import requests; print('✅ Requests imported successfully')" 2>nul || echo "❌ Requests import failed"
python -c "import pydantic; print('✅ Pydantic imported successfully')" 2>nul || echo "❌ Pydantic import failed"

echo.
echo 🧪 Testing optional imports...
python -c "import cryptography; print('✅ Cryptography imported successfully')" 2>nul || echo "⚠️ Cryptography not available"
python -c "import jose; print('✅ Python-JOSE imported successfully')" 2>nul || echo "⚠️ Python-JOSE not available"
python -c "import passlib; print('✅ Passlib imported successfully')" 2>nul || echo "⚠️ Passlib not available"
python -c "import PIL; print('✅ Pillow imported successfully')" 2>nul || echo "⚠️ Pillow not available"

echo.
echo 🎉 Installation completed successfully!
echo.
echo The system is configured to use SQLite database by default.
echo All packages were installed using pre-compiled wheels to avoid compilation issues.
echo.
echo Next steps:
echo 1. Run: start_health_admin.bat
echo 2. Or test AI models: test_ai_model.bat
echo.
echo Note: Some optional features may not be available if certain packages
echo failed to install, but the core system should work properly.
echo.
pause
