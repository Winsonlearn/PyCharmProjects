# 🚀 MEET02 - Quick Start Guide

Aplikasi FastAPI + React yang mendemonstrasikan semua HTTP methods.

## ⚡ Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Application
```bash
python start.py
```

**Atau manual:**
```bash
# Terminal 1: Start backend
python main.py

# Terminal 2: Open frontend
open index.html
```

## 🌐 Access Points

- **Frontend**: `index.html` (buka di browser)
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

## 🧪 Test API

```bash
python test_api.py
```

## 📋 HTTP Methods Demo

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/temperature` | Get current temperature |
| GET | `/users` | Get all users |
| GET | `/sensors` | Get all sensors |
| POST | `/users` | Create new user |
| POST | `/sensors` | Create new sensor |
| PUT | `/temperature` | Update temperature |
| PUT | `/users/{id}` | Full update user |
| PATCH | `/users/{id}` | Partial update user |
| DELETE | `/users/{id}` | Delete user |
| DELETE | `/sensors/{id}` | Delete sensor |
| HEAD | `/` | Get headers |
| OPTIONS | `/` | Get available methods |

## 🎯 Features

✅ **Backend (FastAPI)**
- All HTTP methods (GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS)
- CORS enabled for frontend
- Auto-generated API documentation
- Data validation with Pydantic
- Error handling

✅ **Frontend (React-like)**
- Modern responsive design
- Real-time data updates
- CRUD operations for users & sensors
- Interactive forms
- Statistics dashboard

## 🔧 Troubleshooting

**Port 8000 already in use:**
```bash
lsof -ti:8000 | xargs kill -9
```

**Dependencies not found:**
```bash
pip install -r requirements.txt
```

**Frontend not loading:**
- Make sure backend is running
- Check browser console for errors
- Try opening `index.html` directly

## 📁 Project Structure

```
MEET02/
├── main.py          # FastAPI backend
├── index.html       # React-like frontend
├── start.py         # Quick start script
├── test_api.py      # API testing
├── requirements.txt # Python dependencies
└── README.md        # Full documentation
```

## 🎉 Success!

If you see:
- ✅ Backend running on port 8000
- ✅ Frontend opened in browser
- ✅ API docs accessible
- ✅ All tests passing

Then your application is working perfectly! 🚀 