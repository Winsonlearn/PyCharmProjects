# 🚀 Deployment Guide - SmartHome Projects

Panduan lengkap untuk deploy kedua proyek: Temperature API (PythonAnywhere) dan React Landing Page.

## 📋 Daftar Isi

1. [Temperature API (PythonAnywhere)](#temperature-api-pythonanywhere)
2. [React Landing Page](#react-landing-page)
3. [Testing & Troubleshooting](#testing--troubleshooting)

---

## 🔥 Temperature API (PythonAnywhere)

### Langkah 1: Siapkan PythonAnywhere

1. **Daftar di PythonAnywhere**
   - Kunjungi [pythonanywhere.com](https://www.pythonanywhere.com)
   - Buat akun gratis
   - Catat username Anda

2. **Upload Files**
   - Buka Files tab di PythonAnywhere
   - Upload file dari folder `temperature_api/`:
     - `main.py`
     - `requirements.txt`

### Langkah 2: Install Dependencies

1. **Buka Bash Console**
   - Klik "Bash" di tab Consoles
   - Navigasi ke folder proyek:
   ```bash
   cd temperature_api
   ```

2. **Install Dependencies**
   ```bash
   pip install --user -r requirements.txt
   ```

### Langkah 3: Setup Web App

1. **Buat Web App**
   - Klik tab "Web"
   - Klik "Add a new web app"
   - Pilih "Flask"
   - Pilih Python version (3.9 atau 3.10)

2. **Configure Source Code**
   - Set source code ke: `/home/YOUR_USERNAME/temperature_api`

3. **Edit WSGI File**
   - Klik link WSGI file
   - Ganti isi file dengan:
   ```python
   import sys
   path = '/home/YOUR_USERNAME/temperature_api'
   if path not in sys.path:
       sys.path.append(path)

   from main import app as application
   ```

### Langkah 4: Reload & Test

1. **Reload Web App**
   - Klik tombol "Reload" di tab Web

2. **Test API**
   - Buka: `https://YOUR_USERNAME.pythonanywhere.com`
   - Test endpoint: `https://YOUR_USERNAME.pythonanywhere.com/temperature`

### ✅ API Endpoints yang Tersedia

- `GET /` - API info
- `GET /temperature` - Current temperature
- `GET /temperatures` - All temperature history
- `POST /temperature` - Add new temperature
- `GET /health` - Health check
- `GET /stats` - Statistics

---

## ⚛️ React Landing Page

### Langkah 1: Setup Local Development

1. **Install Dependencies**
   ```bash
   cd smart-home-landing
   npm install
   ```

2. **Configure API URL**
   - Edit `src/components/Temperature.js`
   - Ganti `YOUR_USERNAME` dengan username PythonAnywhere Anda:
   ```javascript
   const API_BASE_URL = 'https://YOUR_USERNAME.pythonanywhere.com';
   ```

3. **Test Local**
   ```bash
   npm start
   ```
   - Buka: `http://localhost:3000`

### Langkah 2: Deploy ke Netlify (Recommended)

1. **Push ke GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/smart-home-landing.git
   git push -u origin main
   ```

2. **Deploy di Netlify**
   - Kunjungi [netlify.com](https://netlify.com)
   - Klik "New site from Git"
   - Pilih GitHub repository
   - Set build settings:
     - Build command: `npm run build`
     - Publish directory: `build`
   - Klik "Deploy site"

### Langkah 3: Deploy ke Vercel (Alternative)

1. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Deploy**
   ```bash
   vercel
   ```
   - Ikuti prompt yang muncul

### Langkah 4: Deploy ke GitHub Pages

1. **Update package.json**
   ```json
   {
     "homepage": "https://YOUR_USERNAME.github.io/REPO_NAME",
     "scripts": {
       "predeploy": "npm run build",
       "deploy": "gh-pages -d build"
     }
   }
   ```

2. **Install gh-pages**
   ```bash
   npm install --save-dev gh-pages
   ```

3. **Deploy**
   ```bash
   npm run deploy
   ```

---

## 🧪 Testing & Troubleshooting

### Test API Endpoints

```bash
# Test current temperature
curl https://YOUR_USERNAME.pythonanywhere.com/temperature

# Test temperature history
curl https://YOUR_USERNAME.pythonanywhere.com/temperatures

# Add new temperature
curl -X POST https://YOUR_USERNAME.pythonanywhere.com/temperature \
     -H "Content-Type: application/json" \
     -d '{"temperature": 25.5}'
```

### Common Issues

#### API Issues
1. **500 Error**
   - Check PythonAnywhere error logs
   - Verify WSGI file configuration
   - Check if all dependencies installed

2. **CORS Error**
   - API sudah include CORS headers
   - Check browser console for details

3. **Database Error**
   - SQLite file akan dibuat otomatis
   - Check file permissions di PythonAnywhere

#### React Issues
1. **Build Error**
   ```bash
   rm -rf node_modules
   npm install
   npm run build
   ```

2. **API Connection Error**
   - Verify API URL in Temperature.js
   - Check if PythonAnywhere API is running
   - Test API endpoints manually

3. **Routing Issues**
   - Ensure React Router is configured correctly
   - Check for 404 errors on refresh

### Debug Steps

1. **Check API Status**
   - Visit: `https://YOUR_USERNAME.pythonanywhere.com/health`

2. **Check Browser Console**
   - Open Developer Tools (F12)
   - Look for errors in Console tab

3. **Test API Manually**
   - Use Postman or curl to test endpoints
   - Verify JSON responses

4. **Check Network Tab**
   - Look for failed requests
   - Check response status codes

---

## 🎯 Final Checklist

### Temperature API ✅
- [ ] Files uploaded to PythonAnywhere
- [ ] Dependencies installed
- [ ] Web app configured
- [ ] WSGI file updated
- [ ] API responding at: `https://YOUR_USERNAME.pythonanywhere.com/temperature`

### React Landing Page ✅
- [ ] Dependencies installed
- [ ] API URL configured
- [ ] Local development working
- [ ] Deployed to hosting platform
- [ ] Temperature page fetching data from API

### Integration ✅
- [ ] React app can fetch temperature data
- [ ] Temperature history displays correctly
- [ ] Add/delete temperature functions work
- [ ] No CORS errors in browser console

---

## 🔗 Links

- **Temperature API**: `https://YOUR_USERNAME.pythonanywhere.com`
- **React Landing Page**: `https://your-app.netlify.app` (or your deployed URL)
- **API Documentation**: `https://YOUR_USERNAME.pythonanywhere.com` (visit root endpoint)

---

## 📞 Support

Jika mengalami masalah:
1. Check error logs di PythonAnywhere
2. Verify API endpoints dengan curl
3. Check browser console untuk React errors
4. Ensure semua dependencies terinstall

**Happy Deploying! 🚀** 