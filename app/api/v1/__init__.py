from flask import Blueprint
from .health import health_bp

v1_bp = Blueprint("v1_bp", __name__)

v1_bp.register_blueprint(health_bp, url_prefix="/health")
