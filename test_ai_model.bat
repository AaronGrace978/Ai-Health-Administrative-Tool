@echo off
title Health Administrative Tool - AI Model Test
color 0A

echo.
echo ================================================================
echo    🤖 Health Administrative Tool - AI Model Test
echo ================================================================
echo.

echo Testing your available AI models...
echo.

REM Test llama3:8b (recommended)
echo 🧪 Testing llama3:8b model...
ollama run llama3:8b "Hello, this is a test for the Health Administrative Tool. Please respond with 'AI model is working correctly for healthcare applications.'" --verbose
if not errorlevel 1 (
    echo.
    echo ✅ llama3:8b is working perfectly!
    echo This model is recommended for the Health Administrative Tool.
    goto :test_other_models
) else (
    echo ❌ llama3:8b test failed
)

:test_other_models
echo.
echo 🔍 Testing other available models...

REM Test mistral:7b-instruct
echo.
echo 🧪 Testing mistral:7b-instruct model...
ollama run mistral:7b-instruct "Hello, this is a test. Please respond with 'AI model is working correctly.'" --verbose
if not errorlevel 1 (
    echo ✅ mistral:7b-instruct is working!
) else (
    echo ❌ mistral:7b-instruct test failed
)

REM Test qwen2.5:7b
echo.
echo 🧪 Testing qwen2.5:7b model...
ollama run qwen2.5:7b "Hello, this is a test. Please respond with 'AI model is working correctly.'" --verbose
if not errorlevel 1 (
    echo ✅ qwen2.5:7b is working!
) else (
    echo ❌ qwen2.5:7b test failed
)

echo.
echo 🎯 Model Recommendations for Health Administrative Tool:
echo.
echo 1. llama3:8b - RECOMMENDED (Best overall performance)
echo 2. mistral:7b-instruct - Good alternative (Faster, smaller)
echo 3. qwen2.5:7b - Good alternative (Multilingual support)
echo.
echo The system is configured to use llama3:8b by default.
echo You can change this in the .env file if needed.
echo.
echo 🚀 Your AI setup is ready! You can now run: start_health_admin.bat
echo.
pause
