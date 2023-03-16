import bcrypt

from src.interfaces.token_creator_interface import TokenCreatorInterface
from src.interfaces.user_repository_interface import UserRepositoryInterface


class AuthenticateUser:
    def authenticate_use_case(
        self,
        repo: UserRepositoryInterface,
        token_handler: TokenCreatorInterface,
        email: str,
        password: str,
    ):
        # access user repository
        data_from_db = repo.select_user(email)

        # Check password provided by the user
        try:
            password = password.encode("utf-8")
            if bcrypt.checkpw(password, data_from_db.passwd.encode("utf-8")):
                token = token_handler.get_token(
                    data_from_db.username, data_from_db.role
                )
                return {"message": "authenticated", "token": token}
            return {"message": "error"}
        except Exception:
            return {"message": "error"}
