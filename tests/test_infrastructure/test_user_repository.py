from typing import List

import pytest

from src.domain.model.user import User
from src.infrastructure.config.connection import DBConnectionHandler
from src.infrastructure.repository.user_repository import UserRepository


@pytest.fixture(scope="class")
def load_user_repository():
    """Fixture to return the UserRepository with connection to DB"""
    return UserRepository(DBConnectionHandler)


@pytest.fixture
def mock_user() -> User:
    """Fixture to return a user model"""
    return User(
        "test@email.com",
        "test_u",
        "$2b$12$91PDBI/A9nh5GjLo1upqXun.IBQcN7lvd8O1xfqyNIxEISIkzLCDW",
        "test",
    )


@pytest.fixture
def create_mock_data(mock_user):
    """Fixture to clean the database after User insertion"""
    with DBConnectionHandler() as db:
        try:
            db.session.add(mock_user)
            db.session.commit()
            yield
            db.session.delete(mock_user)
            db.session.commit()
        except Exception as e:
            raise e


class TestUserRepository:
    def test_select_all_users_method(self, load_user_repository, create_mock_data):
        """
        GIVEN a database with users already inserted
        WHEN the select is realized
        THEN checks if the returned object is equal to expected
        """
        data_from_db = load_user_repository.select_all_users()

        assert isinstance(data_from_db, List)
        assert isinstance(data_from_db[-1], User)

    def test_select_user_method(self, load_user_repository, create_mock_data):
        """
        GIVEN a database with users already inserted
        WHEN the select is realized with filter by 'email'
        THEN checks if the returned object is equal to expected
        """
        data_from_db = load_user_repository.select_user("test@email.com")
        assert isinstance(data_from_db, User)
        assert data_from_db.email == "test@email.com"

    def test_select_user_method_fail(self, load_user_repository):
        """
        GIVEN a database with users already inserted
        WHEN the select is realized with filter by 'email' (invalid)
        THEN checks if the returned object is equal to expected
        """
        data_from_db = load_user_repository.select_user("donotexist@email.com")
        assert data_from_db is None
