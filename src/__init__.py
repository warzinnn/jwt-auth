from dotenv import dotenv_values
from flask import Flask

import src.infrastructure.entities.orm as ORM
from src.entrypoints.blueprint_auth import blueprint_auth


def create_app():
    app = Flask(__name__)
    config_env = dotenv_values(".env")["CONFIG_ENV"]
    app.config.from_object(config_env)

    print(f"[+] Environment: {app.config['ENV']}")
    print(f"[+] Debug: {app.config['DEBUG']}")
    print(f"[+] Testing: {app.config['TESTING']}")

    ORM.configure_mappers()

    app.register_blueprint(blueprint_auth, url_prefix="/api")

    return app
