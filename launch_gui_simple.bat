@echo off
title Health Administrative Tool - Simple GUI Launcher
color 0A

echo.
echo ================================================================
echo    🖥️ Health Administrative Tool - Simple GUI Launcher
echo ================================================================
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

echo 🖥️ Launching GUI application...
echo 💡 Use the "Start Backend Server" button in the GUI if needed
echo.

"%VENV_PYTHON%" -c "from gui.main_gui import HealthAdminGUI; app = HealthAdminGUI(); app.run()"

echo.
echo 👋 Application closed.
pause
