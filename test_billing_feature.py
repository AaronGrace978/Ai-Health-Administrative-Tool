#!/usr/bin/env python3
"""
Test script for the billing feature
This script tests the billing API endpoints and functionality
"""

import requests
import json
import sys
from datetime import datetime, timedelta

# Configuration
API_BASE_URL = "http://localhost:8000/api"
TEST_USER = {
    "username": "testuser",
    "password": "testpass123"
}

def test_billing_feature():
    """Test the complete billing feature"""
    print("🧪 Testing Billing Feature...")
    print("=" * 50)
    
    # Step 1: Login
    print("1. Testing user login...")
    login_response = requests.post(f"{API_BASE_URL}/auth/login", json=TEST_USER)
    if login_response.status_code != 200:
        print("❌ Login failed. Please ensure the server is running and test user exists.")
        print("   You can create a test user through the GUI or API.")
        return False
    
    auth_token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {auth_token}"}
    print("✅ Login successful")
    
    # Step 2: Get user info
    print("\n2. Getting user information...")
    user_response = requests.get(f"{API_BASE_URL}/auth/me", headers=headers)
    if user_response.status_code == 200:
        user_info = user_response.json()
        print(f"✅ User: {user_info['full_name']} ({user_info['role']})")
    else:
        print("❌ Failed to get user information")
        return False
    
    # Step 3: Get patients
    print("\n3. Getting patients...")
    patients_response = requests.get(f"{API_BASE_URL}/patients/", headers=headers)
    if patients_response.status_code != 200:
        print("❌ Failed to get patients")
        return False
    
    patients = patients_response.json()
    if not patients:
        print("⚠️  No patients found. Please create a patient first through the GUI.")
        return False
    
    patient = patients[0]
    print(f"✅ Found patient: {patient['first_name']} {patient['last_name']}")
    
    # Step 4: Create a test bill
    print("\n4. Creating a test bill...")
    due_date = (datetime.now() + timedelta(days=30)).isoformat()
    bill_data = {
        "patient_id": patient["id"],
        "total_amount": 50000,  # $500.00 in cents
        "due_date": due_date,
        "description": "Test consultation bill",
        "service_type": "Consultation",
        "insurance_covered": 20000,  # $200.00 in cents
        "patient_responsibility": 30000  # $300.00 in cents
    }
    
    bill_response = requests.post(f"{API_BASE_URL}/billing/bills", json=bill_data, headers=headers)
    if bill_response.status_code != 200:
        print(f"❌ Failed to create bill: {bill_response.text}")
        return False
    
    bill = bill_response.json()
    print(f"✅ Bill created: {bill['bill_number']} - ${bill['patient_responsibility']/100:.2f}")
    
    # Step 5: Get bills
    print("\n5. Getting bills...")
    bills_response = requests.get(f"{API_BASE_URL}/billing/bills?patient_id={patient['id']}", headers=headers)
    if bills_response.status_code != 200:
        print("❌ Failed to get bills")
        return False
    
    bills = bills_response.json()
    print(f"✅ Found {len(bills)} bill(s)")
    
    # Step 6: Test payment processing
    print("\n6. Testing payment processing...")
    payment_data = {
        "bill_id": bill["id"],
        "amount": 30000,  # $300.00 in cents
        "card_number": "4111111111111111",
        "card_holder_name": "Test User",
        "expiry_month": "12",
        "expiry_year": "2025",
        "cvv": "123",
        "save_payment_method": True
    }
    
    payment_response = requests.post(f"{API_BASE_URL}/billing/bills/{bill['id']}/pay", json=payment_data, headers=headers)
    if payment_response.status_code != 200:
        print(f"❌ Payment failed: {payment_response.text}")
        return False
    
    payment_result = payment_response.json()
    if payment_result["success"]:
        print(f"✅ Payment successful: {payment_result['transaction_id']}")
    else:
        print(f"❌ Payment failed: {payment_result['message']}")
        return False
    
    # Step 7: Get payment methods
    print("\n7. Getting payment methods...")
    methods_response = requests.get(f"{API_BASE_URL}/billing/payment-methods?patient_id={patient['id']}", headers=headers)
    if methods_response.status_code == 200:
        methods = methods_response.json()
        print(f"✅ Found {len(methods)} payment method(s)")
    else:
        print("❌ Failed to get payment methods")
    
    # Step 8: Get billing dashboard
    print("\n8. Getting billing dashboard...")
    dashboard_response = requests.get(f"{API_BASE_URL}/billing/dashboard?patient_id={patient['id']}", headers=headers)
    if dashboard_response.status_code == 200:
        dashboard = dashboard_response.json()
        outstanding = dashboard["total_outstanding"] / 100
        print(f"✅ Dashboard loaded - Outstanding: ${outstanding:.2f}")
    else:
        print("❌ Failed to get billing dashboard")
    
    print("\n" + "=" * 50)
    print("🎉 Billing feature test completed successfully!")
    print("\n📋 Summary:")
    print(f"   • Created bill: {bill['bill_number']}")
    print(f"   • Processed payment: {payment_result['transaction_id']}")
    print(f"   • Outstanding amount: ${outstanding:.2f}")
    print("\n💡 You can now test the billing feature in both:")
    print("   • GUI: Run 'python gui/main_gui.py' and navigate to Billing")
    print("   • Web: Open http://localhost:8000 and navigate to Billing")
    
    return True

def create_test_user():
    """Create a test user if it doesn't exist"""
    print("🔧 Creating test user...")
    
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "full_name": "Test User",
        "password": "testpass123",
        "role": "provider"
    }
    
    try:
        response = requests.post(f"{API_BASE_URL}/auth/register", json=user_data)
        if response.status_code == 200:
            print("✅ Test user created successfully")
            return True
        else:
            print(f"⚠️  Test user creation failed: {response.text}")
            return False
    except requests.exceptions.RequestException:
        print("❌ Cannot connect to server. Please ensure the server is running.")
        return False

if __name__ == "__main__":
    print("🏥 Health Administrative Tool - Billing Feature Test")
    print("=" * 60)
    
    # Check if server is running
    try:
        response = requests.get("http://localhost:8000/health", timeout=5)
        if response.status_code != 200:
            print("❌ Server is not responding properly")
            sys.exit(1)
    except requests.exceptions.RequestException:
        print("❌ Cannot connect to server. Please start the server first:")
        print("   python main.py")
        sys.exit(1)
    
    print("✅ Server is running")
    
    # Try to test billing feature
    if not test_billing_feature():
        print("\n🔧 Attempting to create test user...")
        if create_test_user():
            print("\n🔄 Retrying billing test...")
            test_billing_feature()
        else:
            print("\n❌ Please create a user manually through the GUI or API")
            sys.exit(1)
