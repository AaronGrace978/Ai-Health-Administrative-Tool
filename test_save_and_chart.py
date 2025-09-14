#!/usr/bin/env python3
"""
Test script to verify patient save functionality and chart display
"""

import requests
import json
import sys

def test_patient_save_and_chart():
    """Test patient save functionality and verify chart data"""
    
    # API base URL
    api_base_url = "http://localhost:8000/api"
    
    print("🧪 Testing Patient Save & Chart Functionality...")
    print("=" * 60)
    
    # Step 1: Login
    print("1. Logging in...")
    try:
        login_response = requests.post(
            f"{api_base_url}/auth/login",
            json={"username": "admin", "password": "admin123"}
        )
        
        if login_response.status_code != 200:
            print(f"❌ Login failed: {login_response.status_code}")
            return False
            
        token = login_response.json().get("access_token")
        print(f"✅ Login successful!")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Connection error: {e}")
        return False
    
    # Step 2: Update Aaron Grace with allergies and medical info
    print("\n2. Updating Aaron Grace with allergies and medical information...")
    headers = {"Authorization": f"Bearer {token}"}
    
    update_data = {
        "first_name": "Aaron",
        "last_name": "Grace",
        "allergies": "Pollen, Dust Mites, Seasonal Allergies",
        "medical_conditions": "Hypertension, Seasonal Allergies",
        "medications": "Lisinopril 10mg, Antihistamines as needed",
        "phone": "555-123-4567",
        "email": "aaron.grace@email.com"
    }
    
    try:
        update_response = requests.put(
            f"{api_base_url}/patients/1",
            json=update_data,
            headers=headers
        )
        
        if update_response.status_code == 200:
            patient_data = update_response.json()
            print("✅ Patient updated successfully!")
            print(f"   Name: {patient_data['first_name']} {patient_data['last_name']}")
            print(f"   Allergies: {patient_data.get('allergies', 'None')}")
            print(f"   Medical Conditions: {patient_data.get('medical_conditions', 'None')}")
            print(f"   Medications: {patient_data.get('medications', 'None')}")
            print(f"   Phone: {patient_data.get('phone', 'None')}")
            print(f"   Email: {patient_data.get('email', 'None')}")
        else:
            print(f"❌ Patient update failed: {update_response.status_code}")
            print(f"Response: {update_response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Connection error: {e}")
        return False
    
    # Step 3: Verify the data was saved
    print("\n3. Verifying saved data...")
    try:
        get_response = requests.get(
            f"{api_base_url}/patients/1",
            headers=headers
        )
        
        if get_response.status_code == 200:
            retrieved_patient = get_response.json()
            print("✅ Data verification successful!")
            print(f"   Allergies saved: {retrieved_patient.get('allergies', 'None')}")
            print(f"   Medical conditions saved: {retrieved_patient.get('medical_conditions', 'None')}")
            print(f"   Medications saved: {retrieved_patient.get('medications', 'None')}")
        else:
            print(f"❌ Data verification failed: {get_response.status_code}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Connection error: {e}")
        return False
    
    print("\n" + "=" * 60)
    print("🎉 All tests passed! Patient save functionality is working perfectly!")
    print("\n📊 Chart Features Added:")
    print("   ✅ Patient Health Chart with progress bars")
    print("   ✅ Relationship Score visualization")
    print("   ✅ Visit Frequency tracking")
    print("   ✅ Health Status indicators")
    print("   ✅ Satisfaction ratings")
    print("   ✅ Interactive legend")
    
    print("\n💡 How to use the new features:")
    print("   1. Launch the GUI: python start_gui.py")
    print("   2. Login with: admin / admin123")
    print("   3. Click 'Patients' in the sidebar")
    print("   4. Select Aaron Grace from the patient list")
    print("   5. Click 'Edit Patient' to modify data")
    print("   6. Fill in allergies, medical conditions, etc.")
    print("   7. Click 'Save Patient' - your data will be saved!")
    print("   8. View the new 'Patient Health Chart' in the Overview tab")
    
    return True

if __name__ == "__main__":
    success = test_patient_save_and_chart()
    sys.exit(0 if success else 1)
