from typing import List

from src.domain.model.user import User
from src.interfaces.token_creator_interface import TokenCreatorInterface
from src.interfaces.user_repository_interface import UserRepositoryInterface
from src.use_cases.authenticate_user import AuthenticateUser


class FakeUserRepository(UserRepositoryInterface):
    """Fake Repository for Tests"""

    def select_all_users(self) -> List[User]:
        return [
            User(
                "test@email.com" "test_u",
                "$2b$12$91PDBI/A9nh5GjLo1upqXun.IBQcN7lvd8O1xfqyNIxEISIkzLCDW",
                "test",
            )
        ]

    def select_user(self, email) -> User:
        return User(
            email,
            "test_u",
            "$2b$12$91PDBI/A9nh5GjLo1upqXun.IBQcN7lvd8O1xfqyNIxEISIkzLCDW",
            "test",
        )


class FakeTokenHandler(TokenCreatorInterface):
    """Fake Token Handler for Tests"""

    def get_token(self, username, role):
        return (
            "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJib18xIiwiaWF0IjoxNjc4OTkxMDYyLC"
            "JleHAiOjE2Nzg5OTE2NjIsInJvbGUiOiJiYWNrb2ZmaWNlIn0.HvYlBDzFTzqculAXtIMMmK5CU9HTWJfyHU"
            "sBaTE2rbe3VB_9Dnlew3HarOsk79maSQnRiJI-D77YTocQS7_G5KCeszpz3UPioSgxwQgighxcJRV5mD16hvukCR"
            "ODfXQOAY9TeL08_8e4nzYedIKiuqwA-Gb1uEbmZFNppR1LJCGEs-G-zRjD_FNAePHYtX1mqG7HWy6rYIrbuP99XTJmYb"
            "lAP3bBKY2gLTZHu830mq2f0BTUGKfU3RWYtKwkQlG1FMsGpnIGBJzO_eiWzcFhq7YAQUGHMlvoxV88VgT0cR_x_ssly-n-c"
            "NZiVKTpk6UKqo4l8U6Q3tWn8Tf3emmRsc4rcaHVyYY9xrbZnYQ9VMx-GubuE0KUSAGG51nD8JfNha3VmVgYZf9cdDY_smCzKwax"
            "F_-TvY_4lqbbphRPiK-udyvngSeJizGa10xteQLGAX_XK5EtRpCpYQAlKYiLDfZoW4OYmjRFt0O8nF_02KQ8ustjw0FFcVGxOZAWdQoZ"
        )

    def _get_private_key(self):
        pass

    def _encode_token(self, username, role):
        pass


class TestAuthenticateUserCase:
    def test_authenticate_user(self):
        """
        GIVEN a user is authenticating into the system
        WHEN email and password are inputed
        THEN checks if the user can authenticated successfully
        """
        repo = FakeUserRepository()
        handler = FakeTokenHandler()

        email = "test@email.com"
        password = "pass_a"

        uc = AuthenticateUser()
        result = uc.authenticate_use_case(repo, handler, email, password)

        assert result["message"] == "authenticated"

    def test_authenticate_user_fail_with_wrong_password(self):
        """
        GIVEN a user is authenticating into the system
        WHEN email and password are inputed
        THEN checks if the user authentication failed
        """
        repo = FakeUserRepository()
        handler = FakeTokenHandler()

        email = "test@email.com"
        password = "pass_xxx"

        uc = AuthenticateUser()
        result = uc.authenticate_use_case(repo, handler, email, password)

        assert result["message"] == "error"
