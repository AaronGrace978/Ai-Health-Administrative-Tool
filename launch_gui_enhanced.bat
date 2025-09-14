@echo off
title Health Administrative Tool - Enhanced GUI Launcher
color 0A

echo.
echo ================================================================
echo    🚀 Health Administrative Tool - Enhanced GUI Launcher
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

REM Check if virtual environment exists
if not exist "venv\Scripts\python.exe" (
    echo ❌ Virtual environment not found
    echo.
    echo Please run: install_complete_fix.bat first
    pause
    exit /b 1
)

echo ✅ Virtual environment found
echo.

REM Use virtual environment Python directly
set VENV_PYTHON=venv\Scripts\python.exe

echo 🔧 Testing dependencies...
"%VENV_PYTHON%" -c "import customtkinter; print('✅ CustomTkinter available')"
if errorlevel 1 (
    echo ❌ CustomTkinter not available
    echo Please run: install_complete_fix.bat
    pause
    exit /b 1
)

echo.
echo 🖥️ Launching GUI with enhanced visibility...
echo 💡 The window should appear prominently on your screen
echo 💡 If you don't see it, try Alt+Tab to cycle through windows
echo.

"%VENV_PYTHON%" launch_gui_visible.py

echo.
echo 👋 Application closed.
pause
