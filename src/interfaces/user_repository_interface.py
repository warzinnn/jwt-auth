from abc import ABC, abstractmethod
from typing import List

from src.domain.model.user import User


class UserRepositoryInterface(ABC):
    @abstractmethod
    def select_all_users(self) -> List[User]:
        raise NotImplementedError

    @abstractmethod
    def select_user(self, email: str) -> User:
        raise NotImplementedError
