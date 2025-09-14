@echo off
title Health Administrative Tool - Batch File Fix
color 0A

echo.
echo ================================================================
echo    🔧 Health Administrative Tool - Batch File Diagnostic & Fix
echo ================================================================
echo.

REM Set Python path
set PYTHON_PATH=C:\Users\AGrac\AppData\Local\Programs\Python\Python313\python.exe

echo 🔍 Diagnostic Information:
echo.

REM Check if Python exists
if exist "%PYTHON_PATH%" (
    echo ✅ Python found at: %PYTHON_PATH%
    "%PYTHON_PATH%" --version
) else (
    echo ❌ Python not found at: %PYTHON_PATH%
    echo.
    echo 💡 Please check your Python installation path.
    echo Current expected path: %PYTHON_PATH%
    pause
    exit /b 1
)

echo.

REM Check if virtual environment exists
if exist "venv\Scripts\python.exe" (
    echo ✅ Virtual environment found
    echo Virtual environment Python: venv\Scripts\python.exe
) else (
    echo ❌ Virtual environment not found
    echo.
    echo 💡 Please run: install_complete_fix.bat first
    pause
    exit /b 1
)

echo.

REM Check if main.py exists
if exist "main.py" (
    echo ✅ Project files found
) else (
    echo ❌ main.py not found in current directory
    echo Current directory: %CD%
    pause
    exit /b 1
)

echo.
echo 🚀 Testing Python execution...
echo.

REM Test if we can run Python from the virtual environment
echo Testing virtual environment Python...
"venv\Scripts\python.exe" --version
if errorlevel 1 (
    echo ❌ Virtual environment Python failed
    pause
    exit /b 1
)

echo.
echo Testing Python imports...
"venv\Scripts\python.exe" -c "import sys; print('✅ Python import test successful')"
if errorlevel 1 (
    echo ❌ Python import test failed
    pause
    exit /b 1
)

echo.
echo 🎯 All checks passed! Your batch files should work now.
echo.
echo 💡 To launch the application, try one of these:
echo    - launch_gui_enhanced.bat (Recommended)
echo    - start_health_admin.bat
echo    - Launchers\launch_app.bat
echo.
echo 🔧 If you still have issues, try running:
echo    - install_complete_fix.bat (to fix dependencies)
echo    - setup_ollama.bat (to set up AI features)
echo.
pause
