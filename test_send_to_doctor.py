#!/usr/bin/env python3
"""
Test script for the Send AI Conversations to Doctor feature
"""

import requests
import json
import time
from datetime import datetime

# Configuration
API_BASE_URL = "http://localhost:8000"
TEST_USER = {
    "username": "admin",
    "password": "admin123"
}

def test_send_to_doctor_feature():
    """Test the complete send to doctor workflow"""
    print("🧪 Testing Send AI Conversations to Doctor Feature")
    print("=" * 60)
    
    # Step 1: Login to get auth token
    print("1. 🔐 Logging in...")
    login_response = requests.post(
        f"{API_BASE_URL}/auth/login",
        data={"username": TEST_USER["username"], "password": TEST_USER["password"]}
    )
    
    if login_response.status_code != 200:
        print(f"❌ Login failed: {login_response.status_code}")
        return False
    
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    print("✅ Login successful")
    
    # Step 2: Send some test chat messages
    print("\n2. 💬 Sending test chat messages...")
    test_messages = [
        "Hello, I have some questions about my health",
        "I've been experiencing headaches lately",
        "What should I do about my medication side effects?",
        "Can you help me understand my lab results?"
    ]
    
    for i, message in enumerate(test_messages):
        chat_response = requests.post(
            f"{API_BASE_URL}/ai/chat",
            json={"message": message},
            headers=headers
        )
        
        if chat_response.status_code == 200:
            print(f"✅ Message {i+1} sent successfully")
        else:
            print(f"❌ Message {i+1} failed: {chat_response.status_code}")
    
    # Step 3: Test conversation export
    print("\n3. 📤 Testing conversation export...")
    export_request = {
        "doctor_name": "Dr. Test Smith",
        "doctor_email": "test.doctor@hospital.com",
        "export_format": "text",
        "include_patient_context": True,
        "message_limit": 10
    }
    
    export_response = requests.post(
        f"{API_BASE_URL}/chat/conversation/export",
        json=export_request,
        headers=headers
    )
    
    if export_response.status_code == 200:
        export_result = export_response.json()
        export_id = export_result["export_id"]
        print(f"✅ Export initiated successfully!")
        print(f"   Export ID: {export_id}")
        print(f"   Status: {export_result['status']}")
        
        # Step 4: Check export status
        print("\n4. 🔍 Checking export status...")
        time.sleep(2)  # Wait a moment for processing
        
        status_response = requests.get(
            f"{API_BASE_URL}/chat/conversation/export/{export_id}",
            headers=headers
        )
        
        if status_response.status_code == 200:
            status_result = status_response.json()
            print(f"✅ Status check successful!")
            print(f"   Status: {status_result['status']}")
            print(f"   Message: {status_result['message']}")
            
            if status_result['status'] == 'completed':
                print(f"   Download URL: {status_result.get('download_url', 'N/A')}")
                
                # Step 5: Test download
                print("\n5. 📥 Testing file download...")
                download_response = requests.get(
                    f"{API_BASE_URL}/chat/conversation/export/{export_id}/download",
                    headers=headers
                )
                
                if download_response.status_code == 200:
                    print("✅ File download successful!")
                    print(f"   Content-Type: {download_response.headers.get('content-type', 'N/A')}")
                    print(f"   Content-Length: {len(download_response.content)} bytes")
                    
                    # Save the file for inspection
                    filename = f"test_export_{export_id[:8]}.txt"
                    with open(filename, 'wb') as f:
                        f.write(download_response.content)
                    print(f"   File saved as: {filename}")
                    
                else:
                    print(f"❌ Download failed: {download_response.status_code}")
            else:
                print("⏳ Export still processing...")
        else:
            print(f"❌ Status check failed: {status_response.status_code}")
            
    else:
        print(f"❌ Export failed: {export_response.status_code}")
        if export_response.content:
            error_data = export_response.json()
            print(f"   Error: {error_data.get('detail', 'Unknown error')}")
    
    print("\n" + "=" * 60)
    print("🎉 Test completed!")
    return True

def test_api_endpoints():
    """Test individual API endpoints"""
    print("\n🔧 Testing API Endpoints")
    print("-" * 30)
    
    # Test login
    login_response = requests.post(
        f"{API_BASE_URL}/auth/login",
        data={"username": TEST_USER["username"], "password": TEST_USER["password"]}
    )
    
    if login_response.status_code != 200:
        print("❌ Cannot test endpoints - login failed")
        return False
    
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    # Test chat history endpoint
    print("Testing chat history endpoint...")
    history_response = requests.get(
        f"{API_BASE_URL}/chat/history",
        headers=headers
    )
    print(f"Chat history: {history_response.status_code}")
    
    # Test patients endpoint
    print("Testing patients endpoint...")
    patients_response = requests.get(
        f"{API_BASE_URL}/patients",
        headers=headers
    )
    print(f"Patients: {patients_response.status_code}")
    
    return True

if __name__ == "__main__":
    print("🚀 Starting Send to Doctor Feature Tests")
    print(f"⏰ Test started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    try:
        # Test API endpoints first
        if test_api_endpoints():
            # Run main test
            test_send_to_doctor_feature()
        else:
            print("❌ API endpoint tests failed - skipping main test")
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Make sure the server is running on http://localhost:8000")
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")
    
    print(f"\n⏰ Test completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
