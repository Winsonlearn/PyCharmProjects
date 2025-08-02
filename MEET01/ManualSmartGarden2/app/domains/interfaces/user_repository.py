from abc import ABC, abstractmethod
from typing import Optional, List
from uuid import UUID
from app.domains.entities.user import User

class UserRepository(ABC):
    @abstractmethod
    def get_by_id(self, user_id: UUID) -> Optional[User]:
        pass
    
    @abstractmethod
    def get_by_email(self, email: str) -> Optional[User]:
        pass
    
    @abstractmethod
    def create(self, user: User) -> User:
        pass
    
    @abstractmethod
    def list(self) -> List[User]:
        pass
    
    @abstractmethod
    def update(self, user: User) -> User:
        pass
    
    @abstractmethod
    def delete(self, user_id: UUID) -> None:
        pass
    
    @abstractmethod
    def get_all(self) -> List[User]:
        pass