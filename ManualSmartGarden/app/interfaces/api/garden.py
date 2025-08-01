from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from app.applications.garden.dtos import PlantCreate, PlantResponse
from app.applications.garden.services import GardenService
from app.domains.interfaces.garden_repository import PlantRepository
from app.infrastructures.database import get_db
from app.infrastructures.persistence.sqlalchemy_garden_repository import SQLAlchemyPlantRepository

# Dependency injector to provide the repository
def get_plant_repository(db: Session = Depends(get_db)) -> PlantRepository:
    return SQLAlchemyPlantRepository(db)

# Dependency injector for the service
def get_garden_service(
    repo: PlantRepository = Depends(get_plant_repository)
) -> GardenService:
    return GardenService(plant_repository=repo)

router = APIRouter(
    prefix="/garden",
    tags=["garden"],
)

# A dummy user ID for demonstration purposes.
# In a real app, this would come from an authentication system.
DUMMY_USER_ID = UUID("a1b2c3d4-e5f6-7890-1234-567890abcdef")


@router.post("/plants", response_model=PlantResponse, status_code=201)
def create_plant(
    plant_data: PlantCreate,
    service: GardenService = Depends(get_garden_service),
):
    """
    Create a new plant for the user.
    """
    # In a real app with auth, the user ID would be dynamic.
    # For now, we need to ensure the dummy user exists.
    # This logic will be moved to a user service later.
    from app.infrastructures.persistence.models import User
    from sqlalchemy.orm import Session
    db: Session = next(get_db())
    dummy_user = db.query(User).filter(User.id == DUMMY_USER_ID).first()
    if not dummy_user:
        dummy_user = User(id=DUMMY_USER_ID, email="dummy@example.com", hashed_password="dummy_password")
        db.add(dummy_user)
        db.commit()

    plant = service.add_plant(
        user_id=DUMMY_USER_ID, name=plant_data.name, species=plant_data.species
    )
    return plant

@router.get("/plants", response_model=List[PlantResponse])
def get_user_plants(
    service: GardenService = Depends(get_garden_service),
):
    """
    Get all plants belonging to the user.
    """
    plants = service.get_user_plants(user_id=DUMMY_USER_ID)
    return plants 