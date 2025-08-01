from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class PlantCreate(BaseModel):
    name: str
    species: str

class PlantResponse(BaseModel):
    id: UUID
    user_id: UUID
    name: str
    species: str
    planted_at: datetime

    class Config:
        from_attributes = True 