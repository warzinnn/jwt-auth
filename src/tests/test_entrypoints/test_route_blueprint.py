import pytest

from src.domain.model.user import User
from src.infrastructure.config.connection import DBConnectionHandler


@pytest.fixture()
def mock_user() -> User:
    """Fixture to return a user model"""
    return User(
        "test@email.com",
        "test_u",
        "$2b$12$91PDBI/A9nh5GjLo1upqXun.IBQcN7lvd8O1xfqyNIxEISIkzLCDW",
        "test",
    )


@pytest.fixture()
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


class TestBlueprintAuth:
    def test_blueprint_auth_e2e(self, client, create_mock_data):
        """
        GIVEN a flask app is configured for testing (e2e)
        WHEN endpoint '/api/auth/login' is requested with POST method
        THEN checks the authentication was successful
        """
        payload = {"email": "test@email.com", "password": "pass_a"}
        response = client.post("/api/auth/login", json=payload)
        assert response.status_code == 200
        assert response.json["message"] == "authenticated"
        assert len(response.json["token"]) > 100

    def test_blueprint_auth_with_wrong_http_method(self, client):
        """
        GIVEN a flask app is configured for testing
        WHEN endpoint '/api/auth/login' is requested with wrong HTTP Method
        THEN checks if http status code is equal to 405
        """
        response = client.put("/api/auth/login")
        assert response.status_code == 405

    def test_blueprint_auth_in_route_protected_by_authentication_without_an_admin_token(
        self, client
    ):
        """
        GIVEN a flask app is configured for testing
        WHEN endpoint '/secret/admin' is requested without an admin token
        THEN checks if http status code is equal to 401
        """
        response = client.get("/api/secret/admin")
        assert response.status_code == 401

    def test_blueprint_auth_in_route_protected_by_authentication_without_a_valid_token(
        self, client
    ):
        """
        GIVEN a flask app is configured for testing
        WHEN endpoint '/secret' is requested without a valid JWT token
        THEN checks if http status code is equal to 401
        """
        response = client.get("/api/secret")
        assert response.status_code == 401
