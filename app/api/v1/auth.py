from flask import Blueprint, current_app, jsonify, request
import psycopg2

from app.core.dependencies import get_db_cursor
from app.db.queries import INSERT_USER

auth_bp = Blueprint("auth_bp", __name__)


@auth_bp.post("/register")
def register():
    try:
        data = request.get_json()
        with get_db_cursor() as cursor:
            cursor.execute(INSERT_USER, (data["name"], data["email"], data["password"]))
            user = cursor.fetchone()
        return (
            jsonify(
                {
                    "success": True,
                    "user": {"name": user[1], "email": user[2], "is_verified": user[4]},
                }
            ),
            201,
        )
    except Exception as e:
        if (
            isinstance(e, psycopg2.errors.UniqueViolation)
            and e.diag.constraint_name == "users_email_key"
        ):
            return (
                jsonify(
                    {
                        "success": False,
                        "message": "A user with this email already exists",
                    }
                ),
                409,
            )
        else:
            current_app.logger.error(e)
            return jsonify({"success": False, "message": "Internal server error"}), 500
