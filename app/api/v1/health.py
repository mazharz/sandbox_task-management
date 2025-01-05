from datetime import datetime
from flask import Blueprint


health_bp = Blueprint("health_bp", __name__)


@health_bp.get("/")
def health():
    return {"success": True, "date": datetime.now()}
