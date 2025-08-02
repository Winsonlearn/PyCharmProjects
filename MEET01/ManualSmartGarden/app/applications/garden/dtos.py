from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class PlantCreate(BaseModel):
    name: str
    species: str

class PlantUpdate(BaseModel):
    name: str
    species: str

class PlantPartialUpdate(BaseModel):
    name: Optional[str] = None
    species: Optional[str] = None

class PlantResponse(BaseModel):
    id: UUID
    user_id: UUID
    name: str
    species: str
    planted_at: datetime

    class Config:
        from_attributes = True 