from flask import Blueprint, jsonify
import jwt
from datetime import datetime, timedelta
from cryptography.hazmat.primitives import serialization
from src.auth_handler.token_creator import TokenCreator
from src.auth_handler.token_verifier import token_verify
from dotenv import dotenv_values

blueprint_test = Blueprint(name='blueprint_test', import_name=__name__)

@blueprint_test.route("/secret", methods=["GET"])
@token_verify
def get_secret():
    return jsonify({'message': 's3cr3t_m3ss4g3'})


@blueprint_test.route("/auth", methods=["GET"])
def do_auth():
    token_creator = TokenCreator()
    token = token_creator.get_token
    return jsonify({'message': token})


@blueprint_test.route("/auth/old/rs256", methods=["GET"])
def do_auth_rs256():
    """With asymmetric algorithm"""
    
    with open('.ssh/id_rsa', 'r') as file:
        private_key = file.read()
    passwd = dotenv_values(".env")['KEY_PASS']
    key = serialization.load_ssh_private_key(private_key.encode(), password=passwd.encode())


    payload_data = {
        "sub": "warzin",
        "exp": datetime.utcnow() + timedelta(minutes=10)
    }
    token = jwt.encode(
        payload=payload_data,
        key=key,
        algorithm='RS256'
    )

    # verify the signature of a token
    with open('.ssh/id_rsa.pub', 'r') as file:
        public_key = file.read()
    pub_key = serialization.load_ssh_public_key(public_key.encode())

    try:
        jwt_decoded = jwt.decode(jwt=token, key=pub_key, algorithms=['RS256', ])
    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'expired token'}), 401
    except jwt.InvalidSignatureError:
        return jsonify({'error': 'invalid token'}), 401
    except Exception:
        return jsonify({'error': 'token error'}), 401
    
    return jsonify({'token': token, 'decoded': jwt_decoded})


@blueprint_test.route("/auth/old/hs256", methods=["GET"])
def do_auth_HS256():
    """With symmetric algorithm"""

    payload_data = {
        "sub": "warzin",
        "exp": datetime.utcnow() + timedelta(minutes=10)
    }
    secret = dotenv_values(".env")['SECRET']  

    token = jwt.encode(
        payload=payload_data, key=secret, algorithm='HS256'
    )

    # verify the signature of a token
    token_decoded = jwt.decode(token, key=secret, algorithms=['HS256', ])

    # Verify token by checking the algorithm used
    header_data = jwt.get_unverified_header(token)
    # using that variable in the decode method
    token_decoded2 = jwt.decode(
        token,
        key=secret,
        algorithms=[header_data['alg'], ]
    )

    return jsonify({'token': token, 'decoded': token_decoded2})
