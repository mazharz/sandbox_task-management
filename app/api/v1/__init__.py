from flask import Blueprint
from .health import health_bp
from .auth import auth_bp
from .misc import misc_bp

v1_bp = Blueprint("v1_bp", __name__)

v1_bp.register_blueprint(health_bp, url_prefix="/health")
v1_bp.register_blueprint(auth_bp, url_prefix="/auth")
v1_bp.register_blueprint(misc_bp, url_prefix="/misc")
