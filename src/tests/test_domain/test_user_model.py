import pytest

from src.domain.model.user import User


@pytest.fixture
def mock_user() -> User:
    """Fixture to return a user model"""
    return User(
        "test@email.com",
        "test_u",
        "$2b$12$91PDBI/A9nh5GjLo1upqXun.IBQcN7lvd8O1xfqyNIxEISIkzLCDW",
        "test",
    )


class TestUser:
    def test_user_object_attributes_are_equal_to_the_expected_type(self, mock_user):
        """
        GIVEN a User object is created
        WHEN attributes are required
        THEN checks if the type of attributes are equal to the expected data type
        """
        assert isinstance(mock_user.email, str)
        assert isinstance(mock_user.username, str)
        assert isinstance(mock_user.passwd, str)
        assert isinstance(mock_user.role, str)

    def test_user_attributes_equal_to_expected(self, mock_user):
        """
        GIVEN a User object is created
        WHEN attributes are required
        THEN checks if attributes from the object are equal to the expected data
        """
        assert mock_user.email == "test@email.com"
        assert mock_user.username == "test_u"
        assert (
            mock_user.passwd
            == "$2b$12$91PDBI/A9nh5GjLo1upqXun.IBQcN7lvd8O1xfqyNIxEISIkzLCDW"
        )
        assert mock_user.role == "test"

    def test_user_object_as_dict(self, mock_user):
        """
        GIVEN a user object is created
        WHEN converts the object to dictionary
        THEN returns the user object as a dictionary with his respective  key-value pair
        """
        expected_dict = {
            "email": "test@email.com",
            "username": "test_u",
            "password": "$2b$12$91PDBI/A9nh5GjLo1upqXun.IBQcN7lvd8O1xfqyNIxEISIkzLCDW",
            "role": "test",
        }
        assert mock_user.as_dict() == expected_dict
