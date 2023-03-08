from cryptography.hazmat.primitives import serialization
import jwt
from datetime import datetime, timedelta
from dotenv import dotenv_values

class TokenCreator:

    def __init__(self) -> None:
        self.__TOKEN_KEY = self.__get_private_key()
        self.__EXP_TIME_MINUTES = 10
        #self.__REFRESH_TIME_MINUTES = 5

    @property
    def get_token(self):
        """Function to return JWT token"""
        return self.__encode_token()
    
    def __get_private_key(self):
        """Function to get the private key"""
        with open('.ssh/id_rsa', 'r') as file:
            private_key = file.read()

        passwd = dotenv_values(".env")['KEY_PASS']
        key = serialization.load_ssh_private_key(private_key.encode(), password=passwd.encode())
        return key

    def __encode_token(self):
        """Function to encode the token with a payload
        :params - None
        :return - JWT token
        Explanation
        ===========
        Payload_data
        :params - sub: user id
                - iat: issued at (identifies the time at which the JWT was issued)
                - exp: expiration time (identifies the expiration time on or after which the JWT MUST NOT be accepted for processing)
                - role: role of the user
        """
        payload_data = {
            "sub": "warzin",
            "iat": datetime.utcnow(),
            "exp": datetime.utcnow() + timedelta(minutes=self.__EXP_TIME_MINUTES),
            'role': 'admin'
        }
        token = jwt.encode(
            payload = payload_data,
            key = self.__TOKEN_KEY,
            algorithm='RS256'
        )
        return token

    