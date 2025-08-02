# MEET02 - FastAPI + React Application

Aplikasi lengkap yang mendemonstrasikan integrasi antara backend FastAPI dan frontend React dengan berbagai HTTP method.

## 🚀 Fitur Utama

### Backend (FastAPI)
- **GET**: Mengambil data (temperature, time, users, sensors)
- **POST**: Membuat data baru (users, sensors)
- **PUT**: Update lengkap (full update)
- **PATCH**: Update parsial (partial update)
- **DELETE**: Menghapus data
- **HEAD**: Mengambil header saja
- **OPTIONS**: Mengambil method yang tersedia
- **CORS Support**: Untuk integrasi dengan frontend
- **Auto Documentation**: Swagger UI di `/docs`

### Frontend (React-like)
- **Dashboard Responsive**: Tampilan modern dengan gradient design
- **Real-time Data**: Update data secara real-time
- **CRUD Operations**: Create, Read, Update, Delete untuk users dan sensors
- **Interactive UI**: Form validation, loading states, error handling
- **Statistics Display**: Menampilkan statistik aplikasi

## 📁 Struktur Proyek

```
MEET02/
├── main.py              # Backend FastAPI
├── index.html           # Frontend React-like
├── requirements.txt     # Python dependencies
├── README.md           # Dokumentasi
└── app.py              # Backup FastAPI app
```

## 🛠️ Instalasi & Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Jalankan Backend
```bash
python main.py
```
Backend akan berjalan di: http://localhost:8000

### 3. Buka Frontend
Buka file `index.html` di browser atau jalankan:
```bash
open index.html
```

## 🌐 Endpoints API

### GET Methods
- `GET /` - Welcome message
- `GET /temperature` - Get current temperature
- `GET /time` - Get current time
- `GET /sensors` - Get all sensor data
- `GET /sensors/{sensor_id}` - Get sensor by ID
- `GET /users` - Get all users
- `GET /users/{user_id}` - Get user by ID
- `GET /health` - Health check
- `GET /stats` - Application statistics

### POST Methods
- `POST /sensors` - Create new sensor data
- `POST /users` - Create new user

### PUT Methods (Full Update)
- `PUT /temperature` - Update temperature completely
- `PUT /users/{user_id}` - Update user completely

### PATCH Methods (Partial Update)
- `PATCH /users/{user_id}` - Update user partially

### DELETE Methods
- `DELETE /sensors/{sensor_id}` - Delete sensor data
- `DELETE /users/{user_id}` - Delete user

### HEAD Methods
- `HEAD /` - Get headers for root endpoint
- `HEAD /temperature` - Get headers for temperature endpoint

### OPTIONS Methods
- `OPTIONS /` - Get available methods

## 📊 Data Models

### SensorData
```json
{
  "sensor_id": "string",
  "value": "float",
  "unit": "string",
  "timestamp": "datetime (optional)"
}
```

### User
```json
{
  "id": "integer (optional)",
  "name": "string",
  "email": "string",
  "age": "integer (optional)"
}
```

### UserUpdate
```json
{
  "name": "string (optional)",
  "email": "string (optional)",
  "age": "integer (optional)"
}
```

## 🎯 Cara Penggunaan

### 1. Dashboard
- Buka aplikasi di browser
- Dashboard akan menampilkan temperature, waktu, dan statistik
- Navigasi menggunakan menu di atas

### 2. Users Management
- Klik menu "Users"
- Tambah user baru dengan form
- Lihat daftar semua users
- Hapus user yang tidak diperlukan

### 3. Sensors Management
- Klik menu "Sensors"
- Tambah data sensor baru
- Lihat semua data sensor
- Hapus data sensor yang tidak diperlukan

### 4. API Documentation
- Buka http://localhost:8000/docs
- Test semua endpoint secara interaktif
- Lihat schema dan response examples

## 🔧 Testing dengan curl

### Get Temperature
```bash
curl http://localhost:8000/temperature
```

### Create User
```bash
curl -X POST "http://localhost:8000/users" \
     -H "Content-Type: application/json" \
     -d '{"name": "John Doe", "email": "john@example.com", "age": 30}'
```

### Update User (PUT)
```bash
curl -X PUT "http://localhost:8000/users/1" \
     -H "Content-Type: application/json" \
     -d '{"name": "John Updated", "email": "john.updated@example.com", "age": 31}'
```

### Update User (PATCH)
```bash
curl -X PATCH "http://localhost:8000/users/1" \
     -H "Content-Type: application/json" \
     -d '{"age": 32}'
```

### Create Sensor
```bash
curl -X POST "http://localhost:8000/sensors" \
     -H "Content-Type: application/json" \
     -d '{"sensor_id": "temp_001", "value": 25.5, "unit": "celsius"}'
```

## 🎨 Frontend Features

- **Responsive Design**: Bekerja di desktop dan mobile
- **Modern UI**: Gradient backgrounds, card layouts, hover effects
- **Real-time Updates**: Data diperbarui secara otomatis
- **Form Validation**: Validasi input di sisi client
- **Error Handling**: Pesan error yang informatif
- **Loading States**: Indikator loading saat fetch data
- **Success Messages**: Konfirmasi untuk operasi berhasil

## 🔒 Error Handling

Aplikasi memiliki error handling untuk:
- 404 Not Found
- 400 Bad Request
- 500 Internal Server Error
- CORS errors
- Network errors

## 📝 Catatan Penting

- Data disimpan dalam memory (akan hilang saat aplikasi restart)
- Dalam aplikasi produksi, gunakan database untuk penyimpanan data
- Temperature di-generate secara random antara 10-30°C
- CORS diaktifkan untuk semua origin (development only)
- Frontend menggunakan vanilla JavaScript (tidak memerlukan Node.js)

## 🚀 Deployment

### Backend (FastAPI)
- Gunakan uvicorn dengan gunicorn untuk production
- Setup reverse proxy dengan nginx
- Gunakan database seperti PostgreSQL atau MySQL

### Frontend
- Build static files
- Deploy ke CDN atau static hosting
- Update CORS settings untuk production

## 🤝 Contributing

1. Fork repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

## 📄 License

MIT License - lihat file LICENSE untuk detail. 