#!/usr/bin/env python3
"""
Demo script for the new AI Chat feature in Health Administrative Tool
"""

import asyncio
import httpx
import json
from datetime import datetime

async def test_chat_feature():
    """Test the chat API endpoints"""
    base_url = "http://localhost:8000/api"
    
    print("🤖 Health Administrative Tool - AI Chat Feature Demo")
    print("=" * 60)
    
    # Test data
    test_user = {
        "username": "demo_user",
        "password": "demo_password"
    }
    
    test_messages = [
        "Hello! Can you help me with patient management?",
        "What features are available in this system?",
        "How can I improve patient relationships?",
        "Tell me about the AI insights feature"
    ]
    
    async with httpx.AsyncClient() as client:
        try:
            # Test login
            print("🔐 Testing authentication...")
            login_response = await client.post(
                f"{base_url}/auth/login",
                json=test_user
            )
            
            if login_response.status_code == 200:
                token_data = login_response.json()
                token = token_data["access_token"]
                print("✅ Authentication successful!")
                
                headers = {"Authorization": f"Bearer {token}"}
                
                # Test chat history endpoint
                print("\n📜 Testing chat history endpoint...")
                history_response = await client.get(
                    f"{base_url}/chat/history",
                    headers=headers
                )
                
                if history_response.status_code == 200:
                    history = history_response.json()
                    print(f"✅ Chat history retrieved: {len(history)} messages")
                else:
                    print(f"❌ Chat history failed: {history_response.status_code}")
                
                # Test sending messages
                print("\n💬 Testing chat message sending...")
                for i, message in enumerate(test_messages, 1):
                    print(f"\n📤 Sending message {i}: {message}")
                    
                    chat_response = await client.post(
                        f"{base_url}/chat/send",
                        json={"message": message},
                        headers=headers
                    )
                    
                    if chat_response.status_code == 200:
                        ai_response = chat_response.json()
                        print(f"🤖 AI Response: {ai_response['message'][:100]}...")
                    else:
                        print(f"❌ Chat send failed: {chat_response.status_code}")
                        print(f"Error: {chat_response.text}")
                
                # Test clear chat history
                print("\n🗑️ Testing clear chat history...")
                clear_response = await client.delete(
                    f"{base_url}/chat/clear",
                    headers=headers
                )
                
                if clear_response.status_code == 200:
                    print("✅ Chat history cleared successfully!")
                else:
                    print(f"❌ Clear chat failed: {clear_response.status_code}")
                
            else:
                print(f"❌ Authentication failed: {login_response.status_code}")
                print("Note: Make sure the server is running and you have valid credentials")
                
        except httpx.ConnectError:
            print("❌ Connection failed!")
            print("Make sure the server is running on http://localhost:8000")
            print("Start the server with: python main.py")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

def print_feature_summary():
    """Print a summary of the chat feature"""
    print("\n" + "=" * 60)
    print("🎉 AI Chat Feature Successfully Added!")
    print("=" * 60)
    print("\n✨ Features Added:")
    print("  • 🤖 AI-powered chat interface")
    print("  • 💬 Real-time messaging with typing indicators")
    print("  • 📜 Chat history persistence")
    print("  • 🎨 Beautiful, modern UI design")
    print("  • 📱 Mobile-responsive interface")
    print("  • 🔐 Secure authentication integration")
    print("  • 🗑️ Clear chat history functionality")
    print("  • ⌨️ Keyboard shortcuts (Enter to send)")
    
    print("\n🚀 How to Use:")
    print("  1. Start the server: python main.py")
    print("  2. Open browser: http://localhost:8000")
    print("  3. Login with your credentials")
    print("  4. Click 'AI Chat' in the navigation")
    print("  5. Start chatting with the AI assistant!")
    
    print("\n🔧 API Endpoints:")
    print("  • POST /api/chat/send - Send a message")
    print("  • GET /api/chat/history - Get chat history")
    print("  • DELETE /api/chat/clear - Clear chat history")
    
    print("\n💡 The AI assistant can help with:")
    print("  • Patient management questions")
    print("  • System feature explanations")
    print("  • Healthcare administration guidance")
    print("  • General inquiries about the platform")

if __name__ == "__main__":
    print_feature_summary()
    
    # Ask if user wants to run the test
    print("\n" + "=" * 60)
    response = input("Would you like to test the chat API? (y/n): ").lower().strip()
    
    if response in ['y', 'yes']:
        print("\n🧪 Running chat API tests...")
        asyncio.run(test_chat_feature())
    else:
        print("\n👋 Demo complete! Start the server to try the chat feature.")

