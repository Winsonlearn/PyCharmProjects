#!/usr/bin/env python3
"""
Script untuk menjalankan MEET02 FastAPI Application
"""

import subprocess
import sys
import time
import webbrowser
import os
from pathlib import Path

def check_dependencies():
    """Check if required dependencies are installed"""
    try:
        import fastapi
        import uvicorn
        import pydantic
        print("✅ All dependencies are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Please run: pip install -r requirements.txt")
        return False

def start_server():
    """Start the FastAPI server"""
    print("🚀 Starting FastAPI server...")
    try:
        # Start server in background
        process = subprocess.Popen([
            sys.executable, "main.py"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Wait a bit for server to start
        time.sleep(3)
        
        # Check if server is running
        import requests
        try:
            response = requests.get("http://localhost:8000/health", timeout=5)
            if response.status_code == 200:
                print("✅ Server is running successfully!")
                return process
            else:
                print("❌ Server is not responding correctly")
                return None
        except requests.exceptions.RequestException:
            print("❌ Server failed to start")
            return None
            
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        return None

def open_browser():
    """Open browser with the application"""
    print("🌐 Opening browser...")
    
    # Get the absolute path to index.html
    current_dir = Path(__file__).parent
    index_path = current_dir / "index.html"
    
    if index_path.exists():
        # Open index.html in default browser
        webbrowser.open(f"file://{index_path.absolute()}")
        print("✅ Browser opened with frontend application")
    else:
        print("❌ index.html not found")
        print("Opening API documentation instead...")
        webbrowser.open("http://localhost:8000/docs")

def main():
    """Main function"""
    print("🎯 MEET02 FastAPI + React Application")
    print("=" * 50)
    
    # Check dependencies
    if not check_dependencies():
        return
    
    # Start server
    server_process = start_server()
    if not server_process:
        return
    
    try:
        # Open browser
        open_browser()
        
        print("\n" + "=" * 50)
        print("🎉 Application is ready!")
        print("📱 Frontend: index.html (opened in browser)")
        print("🔧 Backend: http://localhost:8000")
        print("📚 API Docs: http://localhost:8000/docs")
        print("🏥 Health Check: http://localhost:8000/health")
        print("\nPress Ctrl+C to stop the server")
        
        # Keep the server running
        server_process.wait()
        
    except KeyboardInterrupt:
        print("\n🛑 Stopping server...")
        server_process.terminate()
        print("✅ Server stopped")
    except Exception as e:
        print(f"❌ Error: {e}")
        server_process.terminate()

if __name__ == "__main__":
    main() 