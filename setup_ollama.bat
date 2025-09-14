@echo off
title Health Administrative Tool - Ollama Setup
color 0E

echo.
echo ================================================================
echo    🤖 Health Administrative Tool - Ollama AI Setup
echo ================================================================
echo.

echo This script will help you set up Ollama for AI features.
echo.

REM Check if Ollama is already installed
ollama --version >nul 2>&1
if not errorlevel 1 (
    echo ✅ Ollama is already installed
    ollama --version
    echo.
    goto :check_model
)

echo ❌ Ollama is not installed
echo.
echo Please follow these steps to install Ollama:
echo.
echo 1. Go to: https://ollama.ai/download
echo 2. Download the Windows installer
echo 3. Run the installer
echo 4. Restart your command prompt/terminal
echo 5. Run this script again
echo.
echo Press any key to open the Ollama download page...
pause >nul

start https://ollama.ai/download

echo.
echo After installing Ollama, please run this script again.
pause
exit /b 1

:check_model
echo 🔍 Checking for AI models...
echo.

REM List installed models
ollama list
echo.

REM Check if llama2:8b is installed
ollama list | findstr "llama2:8b" >nul
if not errorlevel 1 (
    echo ✅ llama2:8b model is already installed
    goto :start_ollama
)

echo ❌ llama2:8b model not found
echo.
echo Installing llama2:8b model...
echo This will download approximately 4.7GB and may take 10-30 minutes depending on your internet speed.
echo.

set /p confirm="Do you want to continue? (y/n): "
if /i not "%confirm%"=="y" (
    echo Installation cancelled.
    pause
    exit /b 1
)

echo.
echo 📥 Downloading llama2:8b model...
echo Please wait, this may take a while...
echo.

ollama pull llama2:8b
if errorlevel 1 (
    echo ❌ Failed to download llama2:8b model
    echo.
    echo Please check your internet connection and try again.
    pause
    exit /b 1
)

echo.
echo ✅ llama2:8b model installed successfully!

:start_ollama
echo.
echo 🚀 Starting Ollama service...
echo.

REM Check if Ollama is already running
curl -s http://localhost:11434/api/tags >nul 2>&1
if not errorlevel 1 (
    echo ✅ Ollama service is already running
    goto :test_model
)

echo Starting Ollama in background...
start /b ollama serve

REM Wait a moment for Ollama to start
echo Waiting for Ollama to start...
timeout /t 5 /nobreak >nul

:test_model
echo.
echo 🧪 Testing AI model...
echo.

REM Test the model
echo Testing llama2:8b model with a simple prompt...
ollama run llama2:8b "Hello, this is a test. Please respond with 'AI model is working correctly.'" --verbose
if errorlevel 1 (
    echo ❌ AI model test failed
    echo.
    echo Please check the Ollama installation and try again.
    pause
    exit /b 1
)

echo.
echo ✅ AI model is working correctly!
echo.

echo 🎉 Ollama setup completed successfully!
echo.
echo Your Health Administrative Tool is now ready to use AI features:
echo • Patient relationship analysis
echo • Health trend identification  
echo • Risk assessment
echo • Medication reviews
echo • General health insights
echo.
echo You can now run: start_health_admin.bat
echo.
pause
