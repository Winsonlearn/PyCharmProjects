# MEET02-PROJECT

This project contains two main components as per teacher's requirements:

1. **Temperature API** - Flask API deployed on PythonAnywhere
2. **Smart-Home Landing Page** - React application with temperature monitoring

## Project Structure

```
MEET02-PROJECT/
├── temperature_api/           # Flask API for temperature data
│   ├── main.py               # Main Flask application
│   ├── requirements.txt      # Python dependencies
│   └── README.md            # API documentation
└── smart-home-landing/       # React landing page
    ├── public/               # Public assets
    ├── src/                  # React source code
    │   ├── components/       # React components
    │   ├── App.js           # Main app component
    │   └── index.js         # Entry point
    ├── package.json         # Node.js dependencies
    └── README.md            # React app documentation
```

## 1. Temperature API

A Flask-based REST API for managing temperature readings.

### Features:
- GET `/temperatures` - Retrieve all temperature readings
- POST `/temperatures` - Add new temperature reading
- GET `/temperatures/latest` - Get the latest temperature reading
- SQLite database for data persistence
- CORS enabled for cross-origin requests

### Deployment:
- **Platform**: PythonAnywhere
- **URL**: https://huang12345.pythonanywhere.com
- **Status**: ✅ Deployed and accessible

### Local Development:
```bash
cd temperature_api
pip install -r requirements.txt
python main.py
```

## 2. Smart-Home Landing Page

A modern React application for a smart home company.

### Features:
- **Responsive Design**: Mobile-friendly interface
- **Multiple Pages**: Home, About, Contact, Temperature
- **Real-time Temperature Monitoring**: Fetches data from PythonAnywhere API
- **Interactive Components**: Contact form, temperature controls
- **Modern UI**: Beautiful gradients and animations

### Pages:
1. **Home** - Company introduction and features
2. **About** - Company story, mission, and team
3. **Contact** - Contact form and company information
4. **Temperature** - Real-time temperature monitoring

### Local Development:
```bash
cd smart-home-landing
npm install
npm start
```

## API Integration

The React app connects to the PythonAnywhere API:
- **Base URL**: `https://huang12345.pythonanywhere.com`
- **Endpoints**:
  - `GET /temperatures` - Fetch temperature data
  - `POST /temperatures` - Add new temperature reading

## Technologies Used

### Backend (Temperature API):
- **Flask** - Web framework
- **SQLite** - Database
- **Flask-CORS** - Cross-origin resource sharing

### Frontend (React App):
- **React 18** - Frontend framework
- **React Router** - Client-side routing
- **CSS3** - Styling
- **Fetch API** - HTTP requests

## Deployment Status

- ✅ **Temperature API**: Deployed on PythonAnywhere
- 🔄 **React App**: Ready for deployment (can be deployed to Netlify, Vercel, etc.)

## Teacher's Requirements Fulfilled

1. ✅ **Temperature API deployed on PythonAnywhere** - Accessible at https://huang12345.pythonanywhere.com
2. ✅ **React landing page with multiple pages** - Home, About, Contact, Temperature
3. ✅ **Temperature page fetches from PythonAnywhere** - Real-time data integration
4. ✅ **Modern, responsive design** - Professional smart-home company landing page

## Quick Start

1. **Test the API**:
   ```bash
   curl https://huang12345.pythonanywhere.com/temperatures
   ```

2. **Run the React app**:
   ```bash
   cd smart-home-landing
   npm install
   npm start
   ```

3. **Visit the Temperature page** to see real-time data from the API

## Notes

- The API is already deployed and accessible
- The React app is ready for deployment
- All components are fully functional and responsive
- CORS is properly configured for cross-origin requests 