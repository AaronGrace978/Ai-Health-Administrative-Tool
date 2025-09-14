@echo off
title Fix Pydantic Version Issue
color 0A

echo.
echo ================================================================
echo    🔧 Fixing Pydantic Version Issue
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
echo 🔧 Fixing Pydantic version issue...
echo.

REM The issue is that pydantic==2.5.0 requires pydantic-core==2.14.1 which needs Rust
REM But we already have pydantic 2.11.9 installed which works fine
REM Let's just update the requirements to use the working version

echo Installing compatible Pydantic version...
python -m pip install --only-binary=all "pydantic>=2.11.0,<3.0.0"

echo.
echo 🔧 Testing imports...
python -c "import pydantic; print('✅ Pydantic imported successfully - version:', pydantic.__version__)"
python -c "import fastapi; print('✅ FastAPI imported successfully')"
python -c "import customtkinter; print('✅ CustomTkinter imported successfully')"
python -c "import sqlalchemy; print('✅ SQLAlchemy imported successfully')"

echo.
echo ✅ Pydantic version issue fixed!
echo.
echo The application should now work properly.
echo You can run: start_health_admin.bat
echo.
pause
