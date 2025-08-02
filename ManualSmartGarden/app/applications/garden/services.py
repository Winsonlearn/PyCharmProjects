import uuid
from uuid import UUID
from typing import List
from app.domains.entities.garden import Plant
from app.domains.interfaces.garden_repository import PlantRepository


class GardenService:
    def __init__(self, plant_repository: PlantRepository):
        self.plant_repository = plant_repository

    def add_plant(self, user_id: UUID, name: str, species: str) -> Plant:
        plant = Plant(
            id=uuid.uuid4(),
            user_id=user_id,
            name=name,
            species=species
        )
        return self.plant_repository.create(plant)

    def get_user_plants(self, user_id: UUID) -> List[Plant]:
        return self.plant_repository.get_by_user_id(user_id)

    def get_plant_by_id(self, plant_id: UUID) -> Plant | None:
        return self.plant_repository.get_by_id(plant_id)

    def update_plant(self, plant_id: UUID, name: str, species: str) -> Plant | None:
        plant = self.plant_repository.get_by_id(plant_id)
        if plant:
            plant.name = name
            plant.species = species
            return self.plant_repository.update(plant)
        return None

    def update_plant_partial(self, plant_id: UUID, name: str = None, species: str = None) -> Plant | None:
        plant = self.plant_repository.get_by_id(plant_id)
        if plant:
            if name is not None:
                plant.name = name
            if species is not None:
                plant.species = species
            return self.plant_repository.update(plant)
        return None

    def remove_plant(self, plant_id: UUID) -> None:
        self.plant_repository.delete(plant_id) 