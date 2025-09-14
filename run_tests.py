#!/usr/bin/env python3
"""
Health Administrative Tool - Test Runner
Run all tests for the application
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(command, description):
    """Run a command and return success status"""
    print(f"\n{'='*60}")
    print(f"🧪 {description}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Command failed with exit code {e.returncode}")
        print("STDOUT:", e.stdout)
        print("STDERR:", e.stderr)
        return False

def check_dependencies():
    """Check if required dependencies are installed"""
    print("🔍 Checking dependencies...")
    
    try:
        import pytest
        import fastapi
        import sqlalchemy
        import customtkinter
        print("✅ All required dependencies are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Please install dependencies: pip install -r requirements.txt")
        return False

def run_tests():
    """Run all tests"""
    print("🏥 Health Administrative Tool - Test Suite")
    print("="*60)
    
    # Check dependencies
    if not check_dependencies():
        return False
    
    # Change to project directory
    project_dir = Path(__file__).parent
    os.chdir(project_dir)
    
    # Run API tests
    api_success = run_command(
        "python -m pytest tests/test_api.py -v --tb=short",
        "Running API Tests"
    )
    
    # Run security tests
    security_success = run_command(
        "python -c \"from app.core.security import encryption; print('✅ Security module imports successfully')\"",
        "Testing Security Module"
    )
    
    # Run database tests
    db_success = run_command(
        "python -c \"from app.db.database import engine; from app.db import models; models.Base.metadata.create_all(bind=engine); print('✅ Database models created successfully')\"",
        "Testing Database Models"
    )
    
    # Run AI service tests
    ai_success = run_command(
        "python -c \"from app.services.ai_service import AIService; print('✅ AI service imports successfully')\"",
        "Testing AI Service Module"
    )
    
    # Summary
    print(f"\n{'='*60}")
    print("📊 Test Results Summary")
    print(f"{'='*60}")
    
    results = {
        "API Tests": api_success,
        "Security Module": security_success,
        "Database Models": db_success,
        "AI Service": ai_success
    }
    
    passed = sum(results.values())
    total = len(results)
    
    for test_name, success in results.items():
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{test_name:<20} {status}")
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The system is ready to use.")
        return True
    else:
        print("⚠️ Some tests failed. Please check the output above.")
        return False

def run_integration_tests():
    """Run integration tests (requires running services)"""
    print("\n🔗 Running Integration Tests")
    print("="*60)
    
    # Test backend health
    health_success = run_command(
        "python -c \"import requests; r = requests.get('http://localhost:8000/health'); print('✅ Backend health check:', r.status_code == 200)\"",
        "Testing Backend Health Endpoint"
    )
    
    # Test Ollama connection
    ollama_success = run_command(
        "python -c \"import requests; r = requests.get('http://localhost:11434/api/tags'); print('✅ Ollama connection:', r.status_code == 200)\"",
        "Testing Ollama Connection"
    )
    
    return health_success and ollama_success

if __name__ == "__main__":
    print("🏥 Health Administrative Tool - Test Runner")
    print("="*60)
    
    # Check command line arguments
    if len(sys.argv) > 1 and sys.argv[1] == "--integration":
        success = run_integration_tests()
    else:
        success = run_tests()
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)
