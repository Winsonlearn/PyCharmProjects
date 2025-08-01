from uuid import UUID
from dataclasses import dataclass

@dataclass
class User:
    id: UUID
    full_name: str
    email: str
    hashed_password: str
    is_active: bool = True
    