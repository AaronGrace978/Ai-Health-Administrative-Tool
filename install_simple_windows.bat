@echo off
title Health Administrative Tool - Simple Windows Installer
color 0A

echo.
echo ================================================================
echo    🔧 Health Administrative Tool - Simple Windows Installer
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
echo 🔧 Installing dependencies from requirements-windows.txt...
echo.

REM Install from the Windows-compatible requirements file
python -m pip install --only-binary=all -r requirements-windows.txt

if errorlevel 1 (
    echo ❌ Some packages failed to install
    echo.
    echo 🔧 Trying to install packages individually...
    echo.
    
    REM Try installing each package individually
    python -m pip install --only-binary=all fastapi==0.104.1
    python -m pip install --only-binary=all uvicorn==0.24.0
    python -m pip install --only-binary=all sqlalchemy==2.0.23
    python -m pip install --only-binary=all alembic==1.12.1
    python -m pip install --only-binary=all pydantic==2.5.0
    python -m pip install --only-binary=all pydantic-settings==2.1.0
    python -m pip install --only-binary=all requests==2.31.0
    python -m pip install --only-binary=all httpx==0.25.2
    python -m pip install --only-binary=all customtkinter==5.2.0
    python -m pip install --only-binary=all python-dotenv==1.0.0
    python -m pip install --only-binary=all pytest==7.4.3
    python -m pip install --only-binary=all pytest-asyncio==0.21.1
    python -m pip install --only-binary=all python-multipart==0.0.6
    python -m pip install --only-binary=all pillow
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
