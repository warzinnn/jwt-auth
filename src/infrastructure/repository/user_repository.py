from typing import List

from src.domain.model.user import User


class UserRepository:
    def __init__(self, connection_handler) -> None:
        self.__connection_handler = connection_handler

    def select_all_users(self) -> List[User]:
        with self.__connection_handler() as db:
            try:
                data = db.session.query(User).all()
                return data
            except Exception as e:
                return e

    def select_user(self, email: str) -> User:
        with self.__connection_handler() as db:
            try:
                data = db.session.query(User).filter(User.email == email).scalar()
                return data
            except Exception as e:
                return e
