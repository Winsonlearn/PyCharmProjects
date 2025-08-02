#!/usr/bin/env python3
"""
Simple script to start MEET02 FastAPI Application
"""

import uvicorn
import webbrowser
import time
import threading

def open_browser():
    """Open browser after a delay"""
    time.sleep(2)
    webbrowser.open("http://localhost:8000/docs")
    webbrowser.open("file://" + __file__.replace("start.py", "index.html"))

if __name__ == "__main__":
    print("🚀 Starting MEET02 FastAPI Application...")
    print("📚 API Documentation will open at: http://localhost:8000/docs")
    print("🌐 Frontend will open at: index.html")
    print("🛑 Press Ctrl+C to stop")
    
    # Start browser in background thread
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    # Start FastAPI server
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 