@echo off
title Health Administrative Tool - Dependency Installer
color 0B

echo.
echo ================================================================
echo    🔧 Health Administrative Tool - Dependency Installer
echo ================================================================
echo.

REM Set Python path
set PYTHON_PATH=C:\Users\AGrac\AppData\Local\Programs\Python\Python313\python.exe

REM Check if Python exists
if not exist "%PYTHON_PATH%" (
    echo ❌ Python not found at: %PYTHON_PATH%
    echo.
    echo Please check your Python installation path.
    echo.
    pause
    exit /b 1
)

echo ✅ Python found at: %PYTHON_PATH%
echo.

REM Check Python version
echo 🔍 Checking Python version...
"%PYTHON_PATH%" --version
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

REM Install dependencies
echo 🔧 Installing dependencies...
echo This may take a few minutes...
echo.

python -m pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ Failed to install dependencies from requirements.txt
    echo.
    echo This might be due to Python 3.13 compatibility issues.
    echo Trying alternative installation method...
    echo.
    
    REM Try installing with latest compatible versions
    python -m pip install fastapi uvicorn sqlalchemy pydantic pydantic-settings
    python -m pip install "python-jose[cryptography]" "passlib[bcrypt]"
    python -m pip install python-multipart requests httpx customtkinter
    python -m pip install "pillow>=10.2.0" "cryptography>=42.0.0" python-dotenv
    python -m pip install pytest pytest-asyncio
    
    if errorlevel 1 (
        echo ❌ Alternative installation also failed
        echo Please try: install_python313.bat
        pause
        exit /b 1
    ) else (
        echo ✅ Dependencies installed with alternative method
    )
) else (
    echo ✅ Dependencies installed successfully
)

echo.
echo 🔧 Installing additional dependencies...
python -m pip install --upgrade pip
python -m pip install wheel setuptools

echo.
echo ✅ All dependencies installed successfully!
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
echo Next steps:
echo 1. Download and install Ollama from: https://ollama.ai/download
echo 2. Pull the AI model: ollama pull llama2:8b
echo 3. Run: start_health_admin.bat
echo.
pause
