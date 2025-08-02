from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import random
import sqlite3

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Database setup
DATABASE = 'temperature.db'

def init_db():
    """Initialize the database"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS temperatures (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            value REAL NOT NULL,
            timestamp TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def get_db_connection():
    """Get database connection"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Initialize database on startup
init_db()

@app.route('/')
def home():
    """Home endpoint"""
    return jsonify({
        "message": "Temperature API is running!",
        "endpoints": {
            "GET /temperature": "Get current temperature",
            "GET /temperatures": "Get all temperature history",
            "POST /temperature": "Add new temperature reading",
            "GET /temperature/latest": "Get latest temperature"
        }
    })

@app.route('/temperature', methods=['GET'])
def get_current_temperature():
    """Get current temperature (random)"""
    current_temp = round(random.uniform(20, 30), 1)
    timestamp = datetime.now().isoformat()
    
    return jsonify({
        "temperature": current_temp,
        "unit": "celsius",
        "timestamp": timestamp
    })

@app.route('/temperature/latest', methods=['GET'])
def get_latest_temperature():
    """Get latest temperature from database"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM temperatures ORDER BY id DESC LIMIT 1')
    row = cursor.fetchone()
    conn.close()
    
    if row:
        return jsonify({
            "id": row['id'],
            "temperature": row['value'],
            "timestamp": row['timestamp']
        })
    else:
        return jsonify({
            "message": "No temperature data available",
            "temperature": None,
            "timestamp": None
        }), 404

@app.route('/temperatures', methods=['GET'])
def get_all_temperatures():
    """Get all temperature history"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM temperatures ORDER BY id DESC LIMIT 100')
    rows = cursor.fetchall()
    conn.close()
    
    temperatures = []
    for row in rows:
        temperatures.append({
            "id": row['id'],
            "temperature": row['value'],
            "timestamp": row['timestamp']
        })
    
    return jsonify(temperatures)

@app.route('/temperature', methods=['POST'])
def add_temperature():
    """Add new temperature reading"""
    if not request.json or 'temperature' not in request.json:
        return jsonify({"error": "Temperature value is required"}), 400
    
    temp_value = request.json['temperature']
    timestamp = datetime.now().isoformat()
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO temperatures (value, timestamp) VALUES (?, ?)', 
                  (temp_value, timestamp))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    
    return jsonify({
        "message": "Temperature added successfully",
        "id": new_id,
        "temperature": temp_value,
        "timestamp": timestamp
    }), 201

@app.route('/temperature/<int:temp_id>', methods=['GET'])
def get_temperature_by_id(temp_id):
    """Get temperature by ID"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM temperatures WHERE id = ?', (temp_id,))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        return jsonify({
            "id": row['id'],
            "temperature": row['value'],
            "timestamp": row['timestamp']
        })
    else:
        return jsonify({"error": "Temperature not found"}), 404

@app.route('/temperature/<int:temp_id>', methods=['PUT'])
def update_temperature(temp_id):
    """Update temperature by ID"""
    if not request.json or 'temperature' not in request.json:
        return jsonify({"error": "Temperature value is required"}), 400
    
    new_temp = request.json['temperature']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE temperatures SET value = ? WHERE id = ?', (new_temp, temp_id))
    conn.commit()
    conn.close()
    
    if cursor.rowcount > 0:
        return jsonify({
            "message": f"Temperature {temp_id} updated successfully",
            "temperature": new_temp
        })
    else:
        return jsonify({"error": "Temperature not found"}), 404

@app.route('/temperature/<int:temp_id>', methods=['DELETE'])
def delete_temperature(temp_id):
    """Delete temperature by ID"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM temperatures WHERE id = ?', (temp_id,))
    conn.commit()
    conn.close()
    
    if cursor.rowcount > 0:
        return jsonify({"message": f"Temperature {temp_id} deleted successfully"})
    else:
        return jsonify({"error": "Temperature not found"}), 404

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "Temperature API"
    })

@app.route('/stats')
def get_stats():
    """Get API statistics"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) as count, AVG(value) as avg_temp FROM temperatures')
    row = cursor.fetchone()
    conn.close()
    
    return jsonify({
        "total_readings": row['count'] if row['count'] else 0,
        "average_temperature": round(row['avg_temp'], 2) if row['avg_temp'] else 0,
        "timestamp": datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 