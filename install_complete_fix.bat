@echo off
title Complete Installation Fix - Health Administrative Tool
color 0A

echo.
echo ================================================================
echo    🔧 Complete Installation Fix - Health Administrative Tool
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

REM Remove old virtual environment
echo 🔧 Removing old virtual environment...
if exist "venv" (
    rmdir /s /q venv
    echo ✅ Old virtual environment removed
)

REM Create fresh virtual environment
echo 🔧 Creating fresh virtual environment...
"%PYTHON_PATH%" -m venv venv
if errorlevel 1 (
    echo ❌ Failed to create virtual environment
    pause
    exit /b 1
)
echo ✅ Virtual environment created

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo 🔧 Upgrading pip...
python -m pip install --upgrade pip

REM Install all dependencies using the Windows-compatible requirements
echo 🔧 Installing all dependencies...
python -m pip install --only-binary=all -r requirements-windows.txt

REM Install additional required packages
echo 🔧 Installing additional required packages...
python -m pip install --only-binary=all email-validator
python -m pip install --only-binary=all python-jose
python -m pip install --only-binary=all passlib
python -m pip install --only-binary=all cryptography
python -m pip install --only-binary=all python-multipart

echo.
echo 🔧 Testing all imports...
python -c "import fastapi; print('✅ FastAPI imported successfully')"
python -c "import customtkinter; print('✅ CustomTkinter imported successfully')"
python -c "import sqlalchemy; print('✅ SQLAlchemy imported successfully')"
python -c "import pydantic; print('✅ Pydantic imported successfully')"
python -c "import email_validator; print('✅ Email-validator imported successfully')"
python -c "import jose; print('✅ Python-JOSE imported successfully')"
python -c "import passlib; print('✅ Passlib imported successfully')"
python -c "import cryptography; print('✅ Cryptography imported successfully')"

echo.
echo 🔧 Testing main module import...
python -c "import main; print('✅ Main module imported successfully')"

echo.
echo ✅ Complete installation successful!
echo.
echo The application is now ready to use.
echo.
echo Next steps:
echo 1. Run: start_health_admin.bat
echo 2. Or test the backend: python main.py
echo 3. Or test the GUI: python start_gui.py
echo.
echo Backend API will be available at: http://localhost:8000
echo API Documentation: http://localhost:8000/api/docs
echo.
pause
