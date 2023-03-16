import pytest

import src.infrastructure.entities.orm as orm
from src.domain.model.user import User
from src.infrastructure.config.connection import DBConnectionHandler


@pytest.fixture(scope="class")
def load_mapper():
    """fixture to configure the mapper"""
    orm.configure_mappers()


@pytest.fixture()
def mock_user() -> User:
    """Fixture to return a user model"""
    return User(
        "test@email.com",
        "test_u",
        "$2b$12$91PDBI/A9nh5GjLo1upqXun.IBQcN7lvd8O1xfqyNIxEISIkzLCDW",
        "test",
    )


@pytest.fixture
def clean_data(mock_user):
    """Fixture to clean the database after User insertion"""
    with DBConnectionHandler() as db:
        try:
            yield
            db.session.delete(mock_user)
            db.session.commit()
        except Exception as e:
            raise e


@pytest.mark.usefixtures("load_mapper")
class TestEntityOrm:
    def test_if_mapper_was_successfully_configured(self, mock_user, clean_data):
        """
        GIVEN an imperative (classical) class mapping is configured
        WHEN the mapper binds domain model to the SQL tables.
        THEN checks if the bind was done successfully without errors
        """
        with DBConnectionHandler() as db:
            try:
                db.session.add(mock_user)
                db.session.commit()
                user_from_db = (
                    db.session.query(User)
                    .filter(User.email == "test@email.com")
                    .scalar()
                )
            except Exception as e:
                raise e

            assert user_from_db == mock_user
