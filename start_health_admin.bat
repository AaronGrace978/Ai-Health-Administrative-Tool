@echo off
title Health Administrative Tool - AI-Powered Patient Management
color 0A

echo.
echo ================================================================
echo    🏥 Health Administrative Tool - AI-Powered Patient Management
echo ================================================================
echo.

REM Set Python path
set PYTHON_PATH=C:\Users\AGrac\AppData\Local\Programs\Python\Python313\python.exe

REM Check if Python exists
if not exist "%PYTHON_PATH%" (
    echo ❌ Python not found at: %PYTHON_PATH%
    echo.
    echo Please check your Python installation path.
    echo Current path: %PYTHON_PATH%
    echo.
    pause
    exit /b 1
)

echo ✅ Python found at: %PYTHON_PATH%
echo.

REM Check if we're in the right directory
if not exist "main.py" (
    echo ❌ main.py not found in current directory
    echo.
    echo Please run this batch file from the Health Administrative Tool directory.
    echo Current directory: %CD%
    echo.
    pause
    exit /b 1
)

echo ✅ Project files found
echo.

REM Check if virtual environment exists
if exist "venv\Scripts\activate.bat" (
    echo 🔧 Activating virtual environment...
    call venv\Scripts\activate.bat
    echo ✅ Virtual environment activated
) else (
    echo ⚠️ No virtual environment found, using system Python
)

echo.

REM Check if requirements are installed
echo 🔍 Checking dependencies...
"%PYTHON_PATH%" -c "import fastapi, customtkinter, sqlalchemy" 2>nul
if errorlevel 1 (
    echo ❌ Dependencies not installed
    echo.
    echo Installing dependencies...
    REM Try Windows-compatible requirements first, then fallback to original
    if exist "requirements-windows.txt" (
        echo 🔧 Using Windows-compatible requirements...
        "%PYTHON_PATH%" -m pip install --only-binary=all -r requirements-windows.txt
    ) else (
        echo 🔧 Using standard requirements...
        "%PYTHON_PATH%" -m pip install -r requirements.txt
    )
    if errorlevel 1 (
        echo ❌ Failed to install dependencies
        echo.
        echo 💡 Try running: install_windows_fixed.bat
        echo This will install dependencies using pre-compiled wheels.
        pause
        exit /b 1
    )
    echo ✅ Dependencies installed successfully
) else (
    echo ✅ Dependencies are installed
)

echo.

REM Check if Ollama is running
echo 🤖 Checking Ollama AI service...
python -c "import requests; requests.get('http://localhost:11434/api/tags', timeout=2)" >nul 2>&1
if errorlevel 1 (
    echo ⚠️ Ollama not detected. Please start Ollama first:
    echo.
    echo 1. Download Ollama from: https://ollama.ai/download
    echo 2. Install and start Ollama
    echo 3. Pull the AI model: ollama pull llama2:8b
    echo.
    echo Press any key to continue anyway (AI features will be limited)...
    pause >nul
) else (
    echo ✅ Ollama AI service is running
)

echo.

REM Create .env file if it doesn't exist
if not exist ".env" (
    echo 🔧 Creating environment configuration...
    copy "env.example" ".env" >nul
    echo ✅ Environment file created (.env)
    echo.
    echo ⚠️ Please edit .env file to configure your settings
)

echo.

REM Start the application
echo 🚀 Starting Health Administrative Tool...
echo.
echo 📊 Backend API: http://localhost:8000
echo 📖 API Docs: http://localhost:8000/api/docs
echo 🌐 Web Interface: http://localhost:8000
echo 🖥️ Desktop GUI: Starting automatically...
echo.

REM Start the GUI application
"%PYTHON_PATH%" start_gui.py

echo.
echo 👋 Health Administrative Tool has been closed.
echo Thank you for using our AI-powered patient management system!
echo.
pause
