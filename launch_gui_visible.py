#!/usr/bin/env python3
"""
Enhanced GUI Launcher with Visibility Fixes
"""

import sys
import os
import time
import subprocess
import requests
from pathlib import Path

def check_backend():
    """Check if backend is running"""
    try:
        response = requests.get("http://localhost:8000/health", timeout=5)
        return response.status_code == 200
    except:
        return False

def start_backend():
    """Start the backend server"""
    print("🚀 Starting backend server...")
    
    try:
        # Start backend in a separate process
        process = subprocess.Popen([
            sys.executable, "main.py"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Wait for backend to start
        for i in range(10):
            time.sleep(1)
            if check_backend():
                print("✅ Backend started successfully!")
                return True
            print(f"⏳ Waiting for backend... ({i+1}/10)")
        
        print("❌ Backend failed to start")
        return False
        
    except Exception as e:
        print(f"❌ Error starting backend: {e}")
        return False

def launch_gui():
    """Launch the GUI with visibility fixes"""
    print("🖥️ Launching GUI application...")
    
    try:
        from gui.main_gui import HealthAdminGUI
        
        # Create the GUI
        app = HealthAdminGUI()
        
        # Ensure window is visible and on top
        root = app.root
        
        # Force window to front
        root.lift()
        root.attributes('-topmost', True)
        root.after_idle(lambda: root.attributes('-topmost', False))
        
        # Center the window
        root.update_idletasks()
        width = root.winfo_width()
        height = root.winfo_height()
        x = (root.winfo_screenwidth() // 2) - (width // 2)
        y = (root.winfo_screenheight() // 2) - (height // 2)
        root.geometry(f"{width}x{height}+{x}+{y}")
        
        # Make sure window is focused
        root.focus_force()
        
        print("✅ GUI window created and positioned")
        print("🖥️ Window should be visible and focused")
        print("💡 If you don't see the window, try Alt+Tab")
        
        # Start the GUI
        app.run()
        
    except Exception as e:
        print(f"❌ Error launching GUI: {e}")
        import traceback
        traceback.print_exc()

def main():
    """Main launcher function"""
    print("=" * 60)
    print("🏥 Health Administrative Tool - Enhanced GUI Launcher")
    print("=" * 60)
    
    # Check if backend is running
    if not check_backend():
        print("⚠️ Backend not detected. Starting backend...")
        if not start_backend():
            print("❌ Cannot start GUI without backend")
            return
    else:
        print("✅ Backend is already running")
    
    print()
    print("🎯 Launching GUI with visibility fixes...")
    print("📊 Backend API: http://localhost:8000")
    print()
    
    # Launch the GUI
    launch_gui()

if __name__ == "__main__":
    main()
