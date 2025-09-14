#!/usr/bin/env python3
import requests
import json

try:
    response = requests.get('http://localhost:11434/api/tags')
    if response.status_code == 200:
        data = response.json()
        models = data.get('models', [])
        print("🤖 Available Ollama Models:")
        if models:
            for model in models:
                print(f"  ✅ {model['name']}")
        else:
            print("  ❌ No models found")
            print("\n💡 To install models, run:")
            print("  ollama pull llama3:8b")
            print("  ollama pull llama2:8b")
    else:
        print(f"❌ Error connecting to Ollama: {response.status_code}")
except Exception as e:
    print(f"❌ Error: {e}")
    print("\n💡 Make sure Ollama is running:")
    print("  1. Download from: https://ollama.ai/download")
    print("  2. Start Ollama service")
    print("  3. Pull models: ollama pull llama3:8b")
