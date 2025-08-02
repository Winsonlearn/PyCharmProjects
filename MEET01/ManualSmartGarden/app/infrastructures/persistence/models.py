from sqlalchemy import (
    Column, String, Boolean, DateTime, ForeignKey, Float, Enum, TypeDecorator
)
from sqlalchemy.orm import relationship
from sqlalchemy.types import CHAR
import uuid
from datetime import datetime

from app.domains.entities.garden import SensorType, ActuatorType
from app.infrastructures.database import Base


class UUIDType(TypeDecorator):
    """
    Platform-independent UUID type.

    Uses CHAR(32) on database that don't have a native UUID type.
    """
    impl = CHAR(32)
    cache_ok = True

    def load_dialect_impl(self, dialect):
        # Use PostgreSQL's UUID type if available
        if dialect.name == 'postgresql':
            from sqlalchemy.dialects.postgresql import UUID
            return dialect.type_descriptor(UUID())
        else:
            return dialect.type_descriptor(CHAR(32))

    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        return str(value)

    def process_result_value(self, value, dialect):
        if value is None:
            return value
        if not isinstance(value, uuid.UUID):
            return uuid.UUID(value)
        return value


class User(Base):
    __tablename__ = "users"
    id = Column(UUIDType, primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    plants = relationship("Plant", back_populates="owner")


class Plant(Base):
    __tablename__ = "plants"
    id = Column(UUIDType, primary_key=True, default=uuid.uuid4)
    name = Column(String, index=True)
    species = Column(String)
    planted_at = Column(DateTime, default=datetime.utcnow)
    owner_id = Column(UUIDType, ForeignKey("users.id"))

    owner = relationship("User", back_populates="plants")
    sensors = relationship("Sensor", back_populates="plant")
    actuators = relationship("Actuator", back_populates="plant")


class Sensor(Base):
    __tablename__ = "sensors"
    id = Column(UUIDType, primary_key=True, default=uuid.uuid4)
    name = Column(String, index=True)
    sensor_type = Column(Enum(SensorType), nullable=False)
    plant_id = Column(UUIDType, ForeignKey("plants.id"))

    plant = relationship("Plant", back_populates="sensors")
    readings = relationship("SensorReading", back_populates="sensor")


class SensorReading(Base):
    __tablename__ = "sensor_readings"
    id = Column(UUIDType, primary_key=True, default=uuid.uuid4)
    value = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    sensor_id = Column(UUIDType, ForeignKey("sensors.id"), nullable=False)

    sensor = relationship("Sensor", back_populates="readings")


class Actuator(Base):
    __tablename__ = "actuators"
    id = Column(UUIDType, primary_key=True, default=uuid.uuid4)
    name = Column(String, index=True)
    actuator_type = Column(Enum(ActuatorType), nullable=False)
    is_on = Column(Boolean, default=False)
    plant_id = Column(UUIDType, ForeignKey("plants.id"))

    plant = relationship("Plant", back_populates="actuators") 