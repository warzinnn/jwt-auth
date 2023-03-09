from functools import wraps
from cryptography.hazmat.primitives import serialization
from flask import jsonify, request
import jwt

def token_verify(function: callable) -> callable:

    @wraps(function)
    def decorated(*arg, **kwargs):
        """Checks if the token is valid"""

        request_token = request.headers.get('Authorization')

        
        with open('.ssh/id_rsa.pub', 'r') as file:
            public_key = file.read()
        pub_key = serialization.load_ssh_public_key(public_key.encode())

        try:
            jwt_decoded = jwt.decode(jwt=request_token, key=pub_key, algorithms=['RS256', ])
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'expired token'}), 401
        except jwt.InvalidSignatureError:
            return jsonify({'error': 'invalid token'}), 401
        except Exception:
            return jsonify({'error': 'token error'}), 401
        
        return function(*arg, **kwargs)

    return decorated
