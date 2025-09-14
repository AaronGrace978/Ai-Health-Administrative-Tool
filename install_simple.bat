@echo off
title Health Administrative Tool - Simple Installer
color 0A

echo.
echo ================================================================
echo    🔧 Health Administrative Tool - Simple Installer
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

REM Upgrade pip
echo 🔧 Upgrading pip...
python -m pip install --upgrade pip

REM Install core dependencies one by one
echo 🔧 Installing core dependencies...
echo.

echo Installing FastAPI...
python -m pip install fastapi==0.104.1
if errorlevel 1 (
    echo ❌ Failed to install FastAPI
    pause
    exit /b 1
)

echo Installing Uvicorn...
python -m pip install uvicorn==0.24.0

echo Installing SQLAlchemy...
python -m pip install sqlalchemy==2.0.23

echo Installing Pydantic...
python -m pip install pydantic==2.5.0

echo Installing Pydantic Settings...
python -m pip install pydantic-settings==2.1.0

echo Installing Python-JOSE...
python -m pip install "python-jose[cryptography]==3.3.0"

echo Installing Passlib...
python -m pip install "passlib[bcrypt]==1.7.4"

echo Installing Python Multipart...
python -m pip install python-multipart==0.0.6

echo Installing Requests...
python -m pip install requests==2.31.0

echo Installing HTTPX...
python -m pip install httpx==0.25.2

echo Installing CustomTkinter...
python -m pip install customtkinter==5.2.0

echo Installing Pillow...
python -m pip install "pillow>=10.2.0"

echo Installing Cryptography...
python -m pip install "cryptography>=42.0.0"

echo Installing Python Dotenv...
python -m pip install python-dotenv==1.0.0

echo Installing Pytest...
python -m pip install pytest==7.4.3

echo Installing Pytest AsyncIO...
python -m pip install pytest-asyncio==0.21.1

echo.
echo ✅ All core dependencies installed successfully!
echo.

REM Test imports
echo 🧪 Testing imports...
python -c "import fastapi; print('✅ FastAPI imported successfully')"
python -c "import customtkinter; print('✅ CustomTkinter imported successfully')"
python -c "import sqlalchemy; print('✅ SQLAlchemy imported successfully')"
python -c "import requests; print('✅ Requests imported successfully')"

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
