# Temperature API

Simple Flask API for temperature data management, designed for PythonAnywhere deployment.

## Features

- **GET /temperature** - Get current temperature (random)
- **GET /temperature/latest** - Get latest temperature from database
- **GET /temperatures** - Get all temperature history
- **POST /temperature** - Add new temperature reading
- **GET /temperature/<id>** - Get temperature by ID
- **PUT /temperature/<id>** - Update temperature by ID
- **DELETE /temperature/<id>** - Delete temperature by ID
- **GET /health** - Health check
- **GET /stats** - API statistics

## PythonAnywhere Deployment

### 1. Upload Files
Upload these files to your PythonAnywhere account:
- `main.py`
- `requirements.txt`

### 2. Install Dependencies
In PythonAnywhere bash console:
```bash
pip install --user -r requirements.txt
```

### 3. Create Web App
1. Go to Web tab in PythonAnywhere
2. Click "Add a new web app"
3. Choose "Flask" and Python version
4. Set source code to `/home/YOUR_USERNAME/temperature_api`

### 4. Configure WSGI File
Edit the WSGI file to point to your app:
```python
import sys
path = '/home/YOUR_USERNAME/temperature_api'
if path not in sys.path:
    sys.path.append(path)

from main import app as application
```

### 5. Reload Web App
Click "Reload" button in the Web tab.

## Usage

### Local Development
```bash
python main.py
```

### Test Endpoints
```bash
# Get current temperature
curl https://YOUR_USERNAME.pythonanywhere.com/temperature

# Get all temperatures
curl https://YOUR_USERNAME.pythonanywhere.com/temperatures

# Add new temperature
curl -X POST https://YOUR_USERNAME.pythonanywhere.com/temperature \
     -H "Content-Type: application/json" \
     -d '{"temperature": 25.5}'
```

## API Response Examples

### Current Temperature
```json
{
  "temperature": 24.7,
  "unit": "celsius",
  "timestamp": "2024-01-15T10:30:00.123456"
}
```

### Temperature History
```json
[
  {
    "id": 1,
    "temperature": 25.5,
    "timestamp": "2024-01-15T10:30:00.123456"
  },
  {
    "id": 2,
    "temperature": 24.2,
    "timestamp": "2024-01-15T10:25:00.123456"
  }
]
```

## Database

The API uses SQLite database (`temperature.db`) which will be created automatically on first run.

## CORS

CORS is enabled for all origins to allow frontend integration.

## Notes

- Replace `YOUR_USERNAME` with your actual PythonAnywhere username
- The API URL will be: `https://YOUR_USERNAME.pythonanywhere.com`
- Database file will be created in your PythonAnywhere home directory 