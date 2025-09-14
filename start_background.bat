@echo off
title Health Administrative Tool - Background Backend Server
color 0A

echo.
echo ================================================================
echo    🚀 Health Administrative Tool - Background Backend Server
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

echo 🚀 Starting backend server in background...
echo 📊 Backend will be available at: http://localhost:8000
echo 📖 API Documentation: http://localhost:8000/api/docs
echo 🌐 Web Interface: http://localhost:8000
echo.
echo 💡 The server will run in the background
echo 💡 You can now launch the GUI with: launch_gui_simple.bat
echo 💡 To stop the server, close this window or press Ctrl+C
echo.

REM Start the backend server
start "Health Admin Backend" /min "%VENV_PYTHON%" main.py

echo ✅ Backend server started in background!
echo.
echo 🎯 Next steps:
echo    1. Run: launch_gui_simple.bat
echo    2. The GUI will detect the running backend
echo    3. Login and start using the application
echo.
echo 💡 This window will stay open to show server status
echo 💡 Close this window to stop the backend server
echo.

REM Keep the window open and show status
:status_loop
timeout /t 5 /nobreak >nul
echo [%time%] Backend server is running... (Press Ctrl+C to stop)
goto status_loop
