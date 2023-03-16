from src.infrastructure.auth_handler.token_creator import TokenCreator


class TestTokenCreator:
    def test_generate_token(self):
        """
        GIVEN a JWT token is generated
        WHEN access the token
        THEN checks if the token was generated successfully
        """
        token_creator = TokenCreator()
        token = token_creator.get_token("test_user", "test_role")
        assert len(token) == 646
