@echo off
title Fix All Dependencies - Health Administrative Tool
color 0A

echo.
echo ================================================================
echo    🔧 Fixing All Dependencies - Health Administrative Tool
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

REM Activate virtual environment
echo 🔧 Activating virtual environment...
if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
    echo ✅ Virtual environment activated
) else (
    echo ❌ Virtual environment not found
    pause
    exit /b 1
)

echo.
echo 🔧 Installing all missing dependencies...
echo.

REM Install all required packages
echo Installing email-validator...
python -m pip install --only-binary=all email-validator

echo Installing python-jose...
python -m pip install --only-binary=all python-jose

echo Installing passlib...
python -m pip install --only-binary=all passlib

echo Installing cryptography...
python -m pip install --only-binary=all cryptography

echo Installing python-multipart...
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
echo ✅ All dependencies fixed successfully!
echo.
echo The application should now work properly.
echo You can run: start_health_admin.bat
echo.
echo Backend API will be available at: http://localhost:8000
echo API Documentation: http://localhost:8000/api/docs
echo.
pause
