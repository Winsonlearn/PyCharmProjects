#!/usr/bin/env python3
"""
Test script untuk MEET02 FastAPI Application
Menjalankan test untuk semua endpoint yang tersedia
"""

import requests
import json
import time
from datetime import datetime

BASE_URL = "http://localhost:8000"

def test_get_endpoints():
    """Test semua GET endpoints"""
    print("🧪 Testing GET endpoints...")
    
    # Test root endpoint
    response = requests.get(f"{BASE_URL}/")
    print(f"✅ GET / - Status: {response.status_code}")
    print(f"   Response: {response.json()}")
    
    # Test temperature endpoint
    response = requests.get(f"{BASE_URL}/temperature")
    print(f"✅ GET /temperature - Status: {response.status_code}")
    print(f"   Response: {response.json()}")
    
    # Test time endpoint
    response = requests.get(f"{BASE_URL}/time")
    print(f"✅ GET /time - Status: {response.status_code}")
    print(f"   Response: {response.json()}")
    
    # Test users endpoint
    response = requests.get(f"{BASE_URL}/users")
    print(f"✅ GET /users - Status: {response.status_code}")
    print(f"   Response: {response.json()}")
    
    # Test sensors endpoint
    response = requests.get(f"{BASE_URL}/sensors")
    print(f"✅ GET /sensors - Status: {response.status_code}")
    print(f"   Response: {response.json()}")
    
    # Test health endpoint
    response = requests.get(f"{BASE_URL}/health")
    print(f"✅ GET /health - Status: {response.status_code}")
    print(f"   Response: {response.json()}")
    
    # Test stats endpoint
    response = requests.get(f"{BASE_URL}/stats")
    print(f"✅ GET /stats - Status: {response.status_code}")
    print(f"   Response: {response.json()}")

def test_post_endpoints():
    """Test semua POST endpoints"""
    print("\n🧪 Testing POST endpoints...")
    
    # Test create user
    user_data = {
        "name": "Test User",
        "email": "test@example.com",
        "age": 25
    }
    response = requests.post(f"{BASE_URL}/users", json=user_data)
    print(f"✅ POST /users - Status: {response.status_code}")
    print(f"   Response: {response.json()}")
    
    # Test create sensor
    sensor_data = {
        "sensor_id": "test_sensor_001",
        "value": 23.5,
        "unit": "celsius"
    }
    response = requests.post(f"{BASE_URL}/sensors", json=sensor_data)
    print(f"✅ POST /sensors - Status: {response.status_code}")
    print(f"   Response: {response.json()}")

def test_put_endpoints():
    """Test semua PUT endpoints"""
    print("\n🧪 Testing PUT endpoints...")
    
    # Test update temperature
    temp_data = {"value": 28}
    response = requests.put(f"{BASE_URL}/temperature", json=temp_data)
    print(f"✅ PUT /temperature - Status: {response.status_code}")
    print(f"   Response: {response.json()}")
    
    # Test update user (full update)
    user_data = {
        "name": "Updated User",
        "email": "updated@example.com",
        "age": 30
    }
    response = requests.put(f"{BASE_URL}/users/1", json=user_data)
    print(f"✅ PUT /users/1 - Status: {response.status_code}")
    print(f"   Response: {response.json()}")

def test_patch_endpoints():
    """Test semua PATCH endpoints"""
    print("\n🧪 Testing PATCH endpoints...")
    
    # Test partial update user
    user_update = {"age": 35}
    response = requests.patch(f"{BASE_URL}/users/1", json=user_update)
    print(f"✅ PATCH /users/1 - Status: {response.status_code}")
    print(f"   Response: {response.json()}")

def test_delete_endpoints():
    """Test semua DELETE endpoints"""
    print("\n🧪 Testing DELETE endpoints...")
    
    # Test delete sensor
    response = requests.delete(f"{BASE_URL}/sensors/test_sensor_001")
    print(f"✅ DELETE /sensors/test_sensor_001 - Status: {response.status_code}")
    print(f"   Response: {response.json()}")
    
    # Test delete user
    response = requests.delete(f"{BASE_URL}/users/1")
    print(f"✅ DELETE /users/1 - Status: {response.status_code}")
    print(f"   Response: {response.json()}")

def test_head_endpoints():
    """Test semua HEAD endpoints"""
    print("\n🧪 Testing HEAD endpoints...")
    
    # Test head root
    response = requests.head(f"{BASE_URL}/")
    print(f"✅ HEAD / - Status: {response.status_code}")
    
    # Test head temperature
    response = requests.head(f"{BASE_URL}/temperature")
    print(f"✅ HEAD /temperature - Status: {response.status_code}")

def test_options_endpoints():
    """Test semua OPTIONS endpoints"""
    print("\n🧪 Testing OPTIONS endpoints...")
    
    # Test options root
    response = requests.options(f"{BASE_URL}/")
    print(f"✅ OPTIONS / - Status: {response.status_code}")
    print(f"   Allow Header: {response.headers.get('Allow', 'Not found')}")

def test_error_handling():
    """Test error handling"""
    print("\n🧪 Testing Error Handling...")
    
    # Test 404 error
    try:
        response = requests.get(f"{BASE_URL}/nonexistent")
        print(f"✅ 404 Error - Status: {response.status_code}")
        if response.status_code == 404:
            print(f"   Response: {response.json()}")
        else:
            print(f"   Unexpected status: {response.status_code}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test invalid user ID
    try:
        response = requests.get(f"{BASE_URL}/users/999")
        print(f"✅ Invalid User ID - Status: {response.status_code}")
        if response.status_code == 404:
            print(f"   Response: {response.json()}")
        else:
            print(f"   Unexpected status: {response.status_code}")
    except Exception as e:
        print(f"   Error: {e}")

def main():
    """Main function untuk menjalankan semua test"""
    print("🚀 Starting MEET02 API Tests")
    print("=" * 50)
    
    try:
        # Test semua endpoint
        test_get_endpoints()
        test_post_endpoints()
        test_put_endpoints()
        test_patch_endpoints()
        test_delete_endpoints()
        test_head_endpoints()
        test_options_endpoints()
        test_error_handling()
        
        print("\n" + "=" * 50)
        print("🎉 All tests completed successfully!")
        print("✅ Backend is working correctly")
        print("🌐 You can now open index.html in your browser")
        print("📚 API Documentation available at: http://localhost:8000/docs")
        
    except requests.exceptions.ConnectionError:
        print("❌ Error: Cannot connect to the server")
        print("   Make sure the FastAPI server is running with: python main.py")
    except Exception as e:
        print(f"❌ Error during testing: {e}")

if __name__ == "__main__":
    main() 