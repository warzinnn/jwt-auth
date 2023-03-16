from functools import wraps

import jwt
from cryptography.hazmat.primitives import serialization
from flask import jsonify, request


def role_verify(function: callable) -> callable:
    @wraps(function)
    def decorated(*arg, **kwargs):
        """Checks if the token is valid"""

        request_token = request.headers.get("Authorization")

        with open(".ssh/id_rsa.pub", "r") as file:
            public_key = file.read()
        pub_key = serialization.load_ssh_public_key(public_key.encode())

        jwt_decoded = jwt.decode(
            jwt=request_token,
            key=pub_key,
            algorithms=[
                "RS256",
            ],
        )
        if jwt_decoded["role"] != "admin":
            return jsonify({"error": "admin-only-access"}), 401

        return function(*arg, **kwargs)

    return decorated
