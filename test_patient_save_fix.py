#!/usr/bin/env python3
"""
Test the patient save fix
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import and run the GUI
from gui.main_gui import HealthAdminGUI

if __name__ == "__main__":
    print("🚀 Testing Patient Save Fix...")
    print("=" * 60)
    print("📋 Instructions:")
    print("1. Login with: admin / admin123")
    print("2. Click 'Patients' in the sidebar")
    print("3. Select Aaron Grace from the patient list")
    print("4. Click 'Edit Patient' button")
    print("5. Type something in the 'Allergies' field")
    print("6. Click 'Save Patient' button")
    print("7. After saving, click on the 'Medical' tab")
    print("8. You should now see your saved data!")
    print("=" * 60)
    print()
    
    try:
        app = HealthAdminGUI()
        app.run()
    except Exception as e:
        print(f"❌ Error starting GUI: {e}")
        import traceback
        traceback.print_exc()
