@echo off
title Fix SQLAlchemy Compatibility Issue
color 0A

echo.
echo ================================================================
echo    🔧 Fixing SQLAlchemy Compatibility Issue
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
echo 🔧 Fixing SQLAlchemy compatibility issue...
echo.

REM The issue is that SQLAlchemy 2.0.23 has compatibility issues with Python 3.13
REM Let's upgrade to a newer version that supports Python 3.13

echo Uninstalling old SQLAlchemy version...
python -m pip uninstall -y sqlalchemy alembic

echo.
echo Installing SQLAlchemy compatible with Python 3.13...
python -m pip install --only-binary=all "sqlalchemy>=2.0.25"

echo.
echo Installing compatible Alembic version...
python -m pip install --only-binary=all "alembic>=1.13.0"

echo.
echo 🔧 Testing imports...
python -c "import sqlalchemy; print('✅ SQLAlchemy imported successfully - version:', sqlalchemy.__version__)"
python -c "import alembic; print('✅ Alembic imported successfully - version:', alembic.__version__)"
python -c "import fastapi; print('✅ FastAPI imported successfully')"
python -c "import customtkinter; print('✅ CustomTkinter imported successfully')"
python -c "import pydantic; print('✅ Pydantic imported successfully - version:', pydantic.__version__)"

echo.
echo ✅ SQLAlchemy compatibility issue fixed!
echo.
echo The application should now work properly.
echo You can run: start_health_admin.bat
echo.
pause
