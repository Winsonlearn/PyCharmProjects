from typing import List, Optional
from uuid import UUID

from sqlalchemy.orm import Session

from app.domains.entities.garden import Plant
from app.domains.interfaces.garden_repository import PlantRepository
from app.infrastructures.persistence import models


class SQLAlchemyPlantRepository(PlantRepository):

    def __init__(self, db_session: Session):
        self.db = db_session

    def create(self, plant: Plant) -> Plant:
        db_plant = models.Plant(
            id=plant.id,
            name=plant.name,
            species=plant.species,
            planted_at=plant.planted_at,
            owner_id=plant.user_id,
        )
        self.db.add(db_plant)
        self.db.commit()
        self.db.refresh(db_plant)
        return self._to_entity(db_plant)

    def get_by_id(self, plant_id: UUID) -> Optional[Plant]:
        db_plant = self.db.query(models.Plant).filter(models.Plant.id == plant_id).first()
        if db_plant:
            return self._to_entity(db_plant)
        return None

    def get_by_user_id(self, user_id: UUID) -> List[Plant]:
        db_plants = self.db.query(models.Plant).filter(models.Plant.owner_id == user_id).all()
        return [self._to_entity(p) for p in db_plants]

    def list(self) -> List[Plant]:
        db_plants = self.db.query(models.Plant).all()
        return [self._to_entity(p) for p in db_plants]

    def update(self, plant: Plant) -> Plant:
        db_plant = self.db.query(models.Plant).filter(models.Plant.id == plant.id).first()
        if db_plant:
            db_plant.name = plant.name
            db_plant.species = plant.species
            self.db.commit()
            self.db.refresh(db_plant)
            return self._to_entity(db_plant)
        return None

    def delete(self, plant_id: UUID) -> None:
        db_plant = self.db.query(models.Plant).filter(models.Plant.id == plant_id).first()
        if db_plant:
            self.db.delete(db_plant)
            self.db.commit()
    
    def _to_entity(self, db_plant: models.Plant) -> Plant:
        return Plant(
            id=db_plant.id,
            user_id=db_plant.owner_id,
            name=db_plant.name,
            species=db_plant.species,
            planted_at=db_plant.planted_at
        ) 