#!/usr/bin/env python3
"""
Test GUI save functionality
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("🔍 Testing GUI save functionality...")
print("=" * 60)
print("📋 Instructions:")
print("1. The GUI should open")
print("2. Login with: admin / admin123")
print("3. Click 'Patients' in the sidebar")
print("4. Select Aaron Grace from the patient list")
print("5. Click 'Edit Patient' button")
print("6. In the 'Allergies' field, type: 'Pollen, Dust Mites - GUI TEST'")
print("7. In the 'Medical Conditions' field, type: 'Hypertension - GUI TEST'")
print("8. In the 'Current Medications' field, type: 'Lisinopril 10mg - GUI TEST'")
print("9. Click 'Save Patient' button")
print("10. Watch the console output for debug messages")
print("=" * 60)
print()

try:
    from gui.main_gui import HealthAdminGUI
    app = HealthAdminGUI()
    app.run()
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
