from abc import ABC, abstractmethod
from typing import Optional, List
from uuid import UUID

from app.domains.entities.garden import Plant, Sensor, SensorReading, Actuator


class PlantRepository(ABC):

    @abstractmethod
    def create(self, plant: Plant) -> Plant:
        pass

    @abstractmethod
    def get_by_id(self, plant_id: UUID) -> Optional[Plant]:
        pass

    @abstractmethod
    def get_by_user_id(self, user_id: UUID) -> List[Plant]:
        pass

    @abstractmethod
    def list(self) -> List[Plant]:
        pass

    @abstractmethod
    def update(self, plant: Plant) -> Plant:
        pass

    @abstractmethod
    def delete(self, plant_id: UUID) -> None:
        pass


class SensorRepository(ABC):

    @abstractmethod
    def create(self, sensor: Sensor) -> Sensor:
        pass

    @abstractmethod
    def get_by_id(self, sensor_id: UUID) -> Optional[Sensor]:
        pass

    @abstractmethod
    def list(self) -> List[Sensor]:
        pass


class SensorReadingRepository(ABC):

    @abstractmethod
    def create(self, reading: SensorReading) -> SensorReading:
        pass

    @abstractmethod
    def get_by_sensor_id(self, sensor_id: UUID, limit: int = 100) -> List[SensorReading]:
        pass


class ActuatorRepository(ABC):

    @abstractmethod
    def create(self, actuator: Actuator) -> Actuator:
        pass

    @abstractmethod
    def get_by_id(self, actuator_id: UUID) -> Optional[Actuator]:
        pass

    @abstractmethod
    def list(self) -> List[Actuator]:
        pass

    @abstractmethod
    def update_status(self, actuator_id: UUID, is_on: bool) -> Optional[Actuator]:
        pass 