from uuid import UUID
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum

class SensorType(str, Enum):
    SOIL_MOISTURE = "soil_moisture"
    TEMPERATURE = "temperature"
    HUMIDITY = "humidity"
    LIGHT_INTENSITY = "light_intensity"

class ActuatorType(str, Enum):
    WATER_PUMP = "water_pump"
    LIGHT = "light"

@dataclass
class Plant:
    id: UUID
    user_id: UUID
    name: str
    species: str
    planted_at: datetime = field(default_factory=datetime.utcnow)

@dataclass
class Sensor:
    id: UUID
    plant_id: UUID | None
    name: str
    sensor_type: SensorType

@dataclass
class SensorReading:
    id: UUID
    sensor_id: UUID
    value: float
    timestamp: datetime = field(default_factory=datetime.utcnow)

@dataclass
class Actuator:
    id: UUID
    plant_id: UUID | None
    name: str
    actuator_type: ActuatorType
    is_on: bool = False 