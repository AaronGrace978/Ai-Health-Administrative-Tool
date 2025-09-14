#!/usr/bin/env python3
"""
Health Administrative Tool - GUI Launcher
AI-Powered Patient Management System

This script launches the desktop GUI application for the Health Administrative Tool.
Make sure the FastAPI backend is running before starting the GUI.
"""

import sys
import os
import subprocess
import time
import requests
from pathlib import Path

def check_backend_running():
    """Check if the FastAPI backend is running"""
    try:
        response = requests.get("http://localhost:8000/health", timeout=5)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def start_backend():
    """Start the FastAPI backend server"""
    print("🚀 Starting FastAPI backend server...")
    
    # Check if we're in the right directory
    if not Path("main.py").exists():
        print("❌ Error: main.py not found. Please run this script from the project root directory.")
        return False
    
    try:
        # Start the backend server
        process = subprocess.Popen([
            sys.executable, "main.py"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Wait a moment for the server to start
        time.sleep(3)
        
        # Check if the server is running
        if check_backend_running():
            print("✅ Backend server started successfully!")
            return True
        else:
            print("❌ Failed to start backend server")
            return False
            
    except Exception as e:
        print(f"❌ Error starting backend: {str(e)}")
        return False

def start_gui():
    """Start the GUI application"""
    print("🖥️ Starting GUI application...")
    
    try:
        # Import and start the GUI
        from gui.main_gui import HealthAdminGUI
        
        print("✅ GUI application starting...")
        app = HealthAdminGUI()
        app.run()
        
    except ImportError as e:
        print(f"❌ Import error: {str(e)}")
        print("Make sure all required packages are installed:")
        print("pip install -r requirements.txt")
        return False
    except Exception as e:
        print(f"❌ Error starting GUI: {str(e)}")
        return False

def main():
    """Main function"""
    print("=" * 60)
    print("🏥 Health Administrative Tool - AI-Powered Patient Management")
    print("=" * 60)
    print()
    
    # Check if backend is already running
    if check_backend_running():
        print("✅ Backend server is already running!")
    else:
        print("⚠️ Backend server not detected. Starting backend...")
        if not start_backend():
            print("❌ Cannot start GUI without backend server.")
            print("Please start the backend manually: python main.py")
            return
    
    print()
    print("🎯 Starting GUI application...")
    print("📊 Backend API: http://localhost:8000")
    print("📖 API Docs: http://localhost:8000/api/docs")
    print()
    
    # Start the GUI
    start_gui()

if __name__ == "__main__":
    main()
