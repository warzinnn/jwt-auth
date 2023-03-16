from typing import List

from src.domain.model.user import User
from src.interfaces.user_repository_interface import UserRepositoryInterface


class UserRepository(UserRepositoryInterface):
    def __init__(self, connection_handler) -> None:
        self.__connection_handler = connection_handler

    def select_all_users(self) -> List[User]:
        """
        Select data in Users table
        :param - None
        :return - List with all Users
        """
        with self.__connection_handler() as db:
            try:
                data = db.session.query(User).all()
                return data
            except Exception as e:
                return e

    def select_user(self, email: str) -> User:
        """
        Select data in Users table with filter by email
        :param - email
        :return - User object
        """
        with self.__connection_handler() as db:
            try:
                data = db.session.query(User).filter(User.email == email).scalar()
                return data
            except Exception as e:
                return e
