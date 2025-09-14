#!/usr/bin/env python3
"""
Test database connection and data persistence
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.db.database import SessionLocal, engine
from app.db.models import Patient, User
from app.core.security import get_password_hash
from app.core.security import DataEncryption
import requests
import json

def test_database_connection():
    """Test database connection and basic operations"""
    print("🔍 Testing Database Connection...")
    
    try:
        # Test database connection
        db = SessionLocal()
        print("✅ Database connection successful")
        
        # Test if tables exist
        from sqlalchemy import inspect
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        print(f"✅ Tables found: {tables}")
        
        # Test if we can query patients
        patients = db.query(Patient).all()
        print(f"✅ Found {len(patients)} patients in database")
        
        # Test if we can query users
        users = db.query(User).all()
        print(f"✅ Found {len(users)} users in database")
        
        db.close()
        return True
        
    except Exception as e:
        print(f"❌ Database connection failed: {str(e)}")
        return False

def test_api_connection():
    """Test API connection and patient data"""
    print("\n🔍 Testing API Connection...")
    
    try:
        # Test if API is running
        response = requests.get("http://localhost:8000/health", timeout=5)
        if response.status_code == 200:
            print("✅ API is running")
        else:
            print(f"❌ API health check failed: {response.status_code}")
            return False
            
        # Test authentication
        login_data = {
            "username": "admin",
            "password": "admin123"
        }
        
        login_response = requests.post(
            "http://localhost:8000/api/login",
            data=login_data,
            timeout=10
        )
        
        if login_response.status_code == 200:
            token = login_response.json()["access_token"]
            headers = {"Authorization": f"Bearer {token}"}
            print("✅ Authentication successful")
        else:
            print(f"❌ Authentication failed: {login_response.status_code}")
            return False
            
        # Test patient API
        patients_response = requests.get(
            "http://localhost:8000/api/patients/",
            headers=headers,
            timeout=10
        )
        
        if patients_response.status_code == 200:
            patients = patients_response.json()
            print(f"✅ Patient API working - found {len(patients)} patients")
            
            # Test individual patient data
            if patients:
                patient_id = patients[0]['id']
                patient_detail_response = requests.get(
                    f"http://localhost:8000/api/patients/{patient_id}",
                    headers=headers,
                    timeout=10
                )
                
                if patient_detail_response.status_code == 200:
                    patient_detail = patient_detail_response.json()
                    print(f"✅ Patient detail API working")
                    print(f"   Patient: {patient_detail.get('first_name', 'N/A')} {patient_detail.get('last_name', 'N/A')}")
                    print(f"   Allergies: {patient_detail.get('allergies', 'None')}")
                    print(f"   Medical Conditions: {patient_detail.get('medical_conditions', 'None')}")
                    print(f"   Medications: {patient_detail.get('medications', 'None')}")
                else:
                    print(f"❌ Patient detail API failed: {patient_detail_response.status_code}")
                    return False
            else:
                print("⚠️ No patients found in database")
        else:
            print(f"❌ Patient API failed: {patients_response.status_code}")
            return False
            
        return True
        
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to API - make sure the server is running")
        return False
    except Exception as e:
        print(f"❌ API test failed: {str(e)}")
        return False

def create_test_patient():
    """Create a test patient with medical data"""
    print("\n🔍 Creating Test Patient...")
    
    try:
        # Login
        login_data = {
            "username": "admin",
            "password": "admin123"
        }
        
        login_response = requests.post(
            "http://localhost:8000/api/login",
            data=login_data,
            timeout=10
        )
        
        if login_response.status_code != 200:
            print(f"❌ Login failed: {login_response.status_code}")
            return False
            
        token = login_response.json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}
        
        # Create test patient
        test_patient = {
            "patient_id": "TEST001",
            "first_name": "Test",
            "last_name": "Patient",
            "date_of_birth": "1990-01-01T00:00:00Z",
            "gender": "Other",
            "blood_type": "O+",
            "allergies": "Penicillin, Shellfish",
            "medical_conditions": "Hypertension, Diabetes Type 2",
            "medications": "Lisinopril 10mg daily, Metformin 500mg twice daily",
            "insurance_provider": "Test Insurance",
            "insurance_number": "TEST123456"
        }
        
        create_response = requests.post(
            "http://localhost:8000/api/patients/",
            json=test_patient,
            headers=headers,
            timeout=10
        )
        
        if create_response.status_code == 201:
            created_patient = create_response.json()
            print("✅ Test patient created successfully")
            print(f"   Patient ID: {created_patient['id']}")
            print(f"   Name: {created_patient['first_name']} {created_patient['last_name']}")
            print(f"   Allergies: {created_patient.get('allergies', 'None')}")
            print(f"   Medical Conditions: {created_patient.get('medical_conditions', 'None')}")
            print(f"   Medications: {created_patient.get('medications', 'None')}")
            return True
        else:
            print(f"❌ Failed to create test patient: {create_response.status_code}")
            print(f"   Response: {create_response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Test patient creation failed: {str(e)}")
        return False

def main():
    """Run all tests"""
    print("🧪 Health Administrative Tool - Database & API Tests")
    print("=" * 60)
    
    # Test database
    db_ok = test_database_connection()
    
    # Test API
    api_ok = test_api_connection()
    
    # Create test patient if both tests pass
    if db_ok and api_ok:
        create_test_patient()
    
    print("\n" + "=" * 60)
    if db_ok and api_ok:
        print("🎉 All tests passed! Database and API are working correctly.")
        print("\n💡 If you're still seeing 'None' values in the GUI:")
        print("   1. Make sure you're running the latest version of the GUI")
        print("   2. Try refreshing the patient list")
        print("   3. Check that the backend server is running")
    else:
        print("❌ Some tests failed. Please check the errors above.")
        print("\n💡 Troubleshooting:")
        print("   1. Make sure the backend server is running: python main.py")
        print("   2. Check database file exists: health_admin.db")
        print("   3. Verify authentication credentials")

if __name__ == "__main__":
    main()
