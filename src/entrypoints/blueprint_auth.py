from flask import Blueprint, jsonify, request

from src.infrastructure.auth_handler.role_verifier import role_verify
from src.infrastructure.auth_handler.token_creator import TokenCreator
from src.infrastructure.auth_handler.token_verifier import token_verify
from src.infrastructure.config.connection import DBConnectionHandler
from src.infrastructure.repository.user_repository import UserRepository
from src.use_cases.authenticate_user import AuthenticateUser

blueprint_auth = Blueprint(name="blueprint_auth", import_name=__name__)


@blueprint_auth.route("/auth/login", methods=["POST"])
def do_login():
    user_repo = UserRepository(DBConnectionHandler)
    token_creator = TokenCreator()
    uc = AuthenticateUser()

    json_input = request.json
    email_input = json_input["email"]
    passwd_input = json_input["password"]

    # call use_case
    result = uc.authenticate_use_case(
        user_repo, token_creator, email_input, passwd_input
    )

    return jsonify(result)


@blueprint_auth.route("/secret/admin", methods=["GET"])
@token_verify
@role_verify
def get_secret_admin():
    return jsonify({"message": "Successful admin access"})


@blueprint_auth.route("/secret", methods=["GET"])
@token_verify
def get_secret():
    return jsonify({"message": "s3cr3t_m3ss4g3"})
