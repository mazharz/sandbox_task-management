from flask import Flask
from .api.v1 import v1_bp


def bootstrap_app():
    app = Flask(__name__)

    app.register_blueprint(v1_bp, url_prefix="/api/v1")

    return app
