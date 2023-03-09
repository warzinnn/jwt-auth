import bcrypt
from flask import Blueprint, jsonify, request

from src.auth_handler.role_verifier import role_verify
from src.auth_handler.token_creator import TokenCreator
from src.auth_handler.token_verifier import token_verify
from src.infrastructure.config.connection import DBConnectionHandler
from src.infrastructure.repository.user_repository import UserRepository

blueprint_test = Blueprint(name="blueprint_test", import_name=__name__)


@blueprint_test.route("/auth/login", methods=["POST"])
def do_login():
    user_repo = UserRepository(DBConnectionHandler)

    json_input = request.json
    email_input = json_input["email"]
    passwd_input = json_input["password"]

    # Query database by email
    data = user_repo.select_user(email_input)

    # Check password
    password = passwd_input.encode("utf-8")
    if bcrypt.checkpw(password, data.passwd.encode("utf-8")):
        token_creator = TokenCreator()
        token = token_creator.get_token(data.username, data.role)
        return jsonify({"message": "authenticated", "token": token})

    return jsonify({"message": "error"})


@blueprint_test.route("/secret/admin", methods=["GET"])
@token_verify
@role_verify
def get_secret_admin():
    return jsonify({"message": "Successful admin access"})


@blueprint_test.route("/secret", methods=["GET"])
@token_verify
def get_secret():
    return jsonify({"message": "s3cr3t_m3ss4g3"})
