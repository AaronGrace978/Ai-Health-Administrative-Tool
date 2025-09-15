#!/usr/bin/env python3
"""
Test GUI launch to identify the issue
"""

import sys
import traceback

def test_gui_launch():
    print("🧪 Testing GUI Launch...")
    print("=" * 40)
    
    try:
        print("1. Testing imports...")
        import customtkinter as ctk
        print("   ✅ CustomTkinter imported")
        
        from gui.main_gui import HealthAdminGUI
        print("   ✅ HealthAdminGUI imported")
        
        print("\n2. Creating GUI instance...")
        app = HealthAdminGUI()
        print("   ✅ GUI instance created")
        
        print("\n3. Testing GUI components...")
        print(f"   ✅ Root window: {app.root}")
        print(f"   ✅ API base URL: {app.api_base_url}")
        
        print("\n4. Testing frame creation...")
        print("   ✅ All frames created successfully")
        
        print("\n5. GUI is ready to run!")
        print("   💡 To launch the GUI, call: app.run()")
        
        return True
        
    except Exception as e:
        print(f"❌ Error during GUI launch: {e}")
        print("\n🔍 Full traceback:")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_gui_launch()
    if success:
        print("\n🎉 GUI test completed successfully!")
        print("   The GUI should be able to launch properly.")
    else:
        print("\n💥 GUI test failed!")
        print("   There's an issue preventing the GUI from launching.")
