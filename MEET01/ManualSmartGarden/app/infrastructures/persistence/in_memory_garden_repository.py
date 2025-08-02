from typing import List, Optional
from uuid import UUID
from app.domains.entities.garden import Plant, Sensor, Actuator, SensorReading
from app.domains.interfaces.garden_repository import PlantRepository, SensorRepository, ActuatorRepository, SensorReadingRepository


class InMemoryPlantRepository(PlantRepository):
    def __init__(self):
        self._plants: dict[UUID, Plant] = {}

    def create(self, plant: Plant) -> Plant:
        self._plants[plant.id] = plant
        return plant

    def get_by_id(self, plant_id: UUID) -> Optional[Plant]:
        return self._plants.get(plant_id)

    def get_by_user_id(self, user_id: UUID) -> List[Plant]:
        return [p for p in self._plants.values() if p.user_id == user_id]

    def list(self) -> List[Plant]:
        return list(self._plants.values())

    def update(self, plant: Plant) -> Plant:
        if plant.id in self._plants:
            self._plants[plant.id] = plant
            return plant
        return None

    def delete(self, plant_id: UUID) -> None:
        if plant_id in self._plants:
            del self._plants[plant_id]

class InMemorySensorRepository(SensorRepository):
    def __init__(self):
        self._sensors: dict[UUID, Sensor] = {}
    
    def create(self, sensor: Sensor) -> Sensor:
        self._sensors[sensor.id] = sensor
        return sensor

    def get_by_id(self, sensor_id: UUID) -> Optional[Sensor]:
        return self._sensors.get(sensor_id)

    def list(self) -> List[Sensor]:
        return list(self._sensors.values())

class InMemorySensorReadingRepository(SensorReadingRepository):
    def __init__(self):
        self._readings: list[SensorReading] = []

    def create(self, reading: SensorReading) -> SensorReading:
        self._readings.append(reading)
        return reading

    def get_by_sensor_id(self, sensor_id: UUID, limit: int = 100) -> List[SensorReading]:
        readings = [r for r in self._readings if r.sensor_id == sensor_id]
        return sorted(readings, key=lambda r: r.timestamp, reverse=True)[:limit]

class InMemoryActuatorRepository(ActuatorRepository):
    def __init__(self):
        self._actuators: dict[UUID, Actuator] = {}
    
    def create(self, actuator: Actuator) -> Actuator:
        self._actuators[actuator.id] = actuator
        return actuator

    def get_by_id(self, actuator_id: UUID) -> Optional[Actuator]:
        return self._actuators.get(actuator_id)

    def list(self) -> List[Actuator]:
        return list(self._actuators.values())

    def update_status(self, actuator_id: UUID, is_on: bool) -> Optional[Actuator]:
        actuator = self.get_by_id(actuator_id)
        if actuator:
            actuator.is_on = is_on
            return actuator
        return None 