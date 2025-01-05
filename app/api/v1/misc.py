from flask import Blueprint, current_app, jsonify

from app.core.dependencies import get_db_cursor

DB_INIT_FILE = "./db/init.sql"

misc_bp = Blueprint("misc_bp", __name__)


@misc_bp.post("/db/init")
def db_init():
    try:
        with get_db_cursor() as cursor:
            with open(DB_INIT_FILE, "r") as file:
                sql_script = file.read()
            cursor.execute(sql_script)
        return (
            jsonify(
                {
                    "success": True,
                    "message": "Database was initialized successfully!",
                }
            ),
            201,
        )
    except Exception as e:
        current_app.logger.error(e)
        return jsonify({"success": False}), 500
