from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel
from random import randint
from datetime import datetime
from typing import List, Optional
import json

app = FastAPI(
    title="MEET02 API",
    description="Aplikasi FastAPI dengan berbagai HTTP method",
    version="1.0.0"
)

# Data storage (dalam praktik nyata gunakan database)
temperature = randint(10, 30)
sensors_data = []
users = []

# Pydantic models untuk validation
class SensorData(BaseModel):
    sensor_id: str
    value: float
    unit: str
    timestamp: Optional[datetime] = None

class User(BaseModel):
    id: Optional[int] = None
    name: str
    email: str
    age: Optional[int] = None

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None

# GET Methods
@app.get("/")
def read_root():
    """Root endpoint - Welcome message"""
    return {"message": "Hello, World!", "api_version": "1.0.0"}

@app.get("/temperature")
def get_temperature():
    """Get current temperature"""
    return {"temperature": temperature, "unit": "celsius", "timestamp": datetime.now().isoformat()}

@app.get("/time")
def get_time():
    """Get current time"""
    return {"time": datetime.now().isoformat(), "timezone": "UTC"}

@app.get("/sensors", response_model=List[SensorData])
def get_sensors():
    """Get all sensor data"""
    return sensors_data

@app.get("/sensors/{sensor_id}")
def get_sensor_by_id(sensor_id: str):
    """Get sensor data by ID"""
    for sensor in sensors_data:
        if sensor["sensor_id"] == sensor_id:
            return sensor
    raise HTTPException(status_code=404, detail="Sensor not found")

@app.get("/users", response_model=List[User])
def get_users():
    """Get all users"""
    return users

@app.get("/users/{user_id}")
def get_user(user_id: int):
    """Get user by ID"""
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

# POST Methods
@app.post("/sensors", response_model=SensorData, status_code=201)
def create_sensor(sensor: SensorData):
    """Create new sensor data"""
    sensor_dict = sensor.dict()
    if not sensor_dict.get("timestamp"):
        sensor_dict["timestamp"] = datetime.now().isoformat()
    sensors_data.append(sensor_dict)
    return sensor_dict

@app.post("/users", response_model=User, status_code=201)
def create_user(user: User):
    """Create new user"""
    user_dict = user.dict()
    user_dict["id"] = len(users) + 1
    users.append(user_dict)
    return user_dict

# PUT Methods (Full Update)
@app.put("/temperature")
def update_temperature(new_temp: int):
    """Update temperature (full update)"""
    global temperature
    if new_temp < -50 or new_temp > 100:
        raise HTTPException(status_code=400, detail="Temperature must be between -50 and 100")
    temperature = new_temp
    return {"temperature": temperature, "unit": "celsius", "updated_at": datetime.now().isoformat()}

@app.put("/users/{user_id}")
def update_user_full(user_id: int, user: User):
    """Update user completely (PUT method)"""
    for i, existing_user in enumerate(users):
        if existing_user["id"] == user_id:
            user_dict = user.dict()
            user_dict["id"] = user_id
            users[i] = user_dict
            return user_dict
    raise HTTPException(status_code=404, detail="User not found")

# PATCH Methods (Partial Update)
@app.patch("/users/{user_id}")
def update_user_partial(user_id: int, user_update: UserUpdate):
    """Update user partially (PATCH method)"""
    for i, existing_user in enumerate(users):
        if existing_user["id"] == user_id:
            update_data = user_update.dict(exclude_unset=True)
            users[i].update(update_data)
            return users[i]
    raise HTTPException(status_code=404, detail="User not found")

# DELETE Methods
@app.delete("/sensors/{sensor_id}")
def delete_sensor(sensor_id: str):
    """Delete sensor data"""
    for i, sensor in enumerate(sensors_data):
        if sensor["sensor_id"] == sensor_id:
            deleted_sensor = sensors_data.pop(i)
            return {"message": "Sensor deleted", "deleted_sensor": deleted_sensor}
    raise HTTPException(status_code=404, detail="Sensor not found")

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    """Delete user"""
    for i, user in enumerate(users):
        if user["id"] == user_id:
            deleted_user = users.pop(i)
            return {"message": "User deleted", "deleted_user": deleted_user}
    raise HTTPException(status_code=404, detail="User not found")

# HEAD Method
@app.head("/")
def head_root():
    """HEAD request to root endpoint"""
    return Response(status_code=200)

@app.head("/temperature")
def head_temperature():
    """HEAD request to temperature endpoint"""
    return Response(status_code=200)

# OPTIONS Method
@app.options("/")
def options_root():
    """OPTIONS request to root endpoint"""
    return Response(
        status_code=200,
        headers={
            "Allow": "GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS",
            "Content-Type": "application/json"
        }
    )

# Additional utility endpoints
@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "sensors_count": len(sensors_data),
        "users_count": len(users)
    }

@app.get("/stats")
def get_stats():
    """Get application statistics"""
    return {
        "total_sensors": len(sensors_data),
        "total_users": len(users),
        "current_temperature": temperature,
        "server_time": datetime.now().isoformat()
    }

# Error handling
@app.exception_handler(404)
async def not_found_handler(request, exc):
    return {"error": "Resource not found", "detail": str(exc)}

@app.exception_handler(500)
async def internal_error_handler(request, exc):
    return {"error": "Internal server error", "detail": str(exc)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)