from datetime import datetime, timedelta, timezone
import uuid

from flask import Blueprint, current_app, jsonify, request
from psycopg2.errors import UniqueViolation

from app.core.dependencies import get_db_cursor
from app.core.result import Failure, Success
from app.db.queries import (
    FIND_USER,
    FIND_VERIFICATION_TOKEN,
    INSERT_USER,
    INSERT_VERIFICATION_TOKEN,
    VERIFY_USER,
)
from app.services.crypto import (
    compare_with_hash,
    decode_jwt_token,
    encode_jwt_token,
    hash_password,
)

auth_bp = Blueprint("auth_bp", __name__)


@auth_bp.post("/register")
def register():
    try:
        payload = request.get_json()
        with get_db_cursor() as cursor:
            (hashed, salt) = hash_password(payload["password"])
            cursor.execute(
                INSERT_USER % (payload["name"], payload["email"], hashed, salt)
            )
            user = cursor.fetchone()
            verification_token = str(uuid.uuid4())
            verification_expires_at = datetime.now(timezone.utc) + timedelta(minutes=15)
            cursor.execute(
                INSERT_VERIFICATION_TOKEN
                % (user[0], verification_token, verification_expires_at)
            )
            token = encode_jwt_token(user[0])
        return (
            jsonify(
                Success(
                    data={
                        # TODO: use sqlalchemy and not this nonsense positional fields
                        "name": user[1],
                        "email": user[2],
                        # let's imagine this is sent to user via email
                        "verification_token": verification_token,
                        "access_token": token,
                    }
                ).model_dump()
            ),
            201,
        )
    except Exception as e:
        if (
            isinstance(e, UniqueViolation)
            and e.diag.constraint_name == "users_email_key"  # pylint: disable=no-member
        ):
            return (
                jsonify(
                    Failure(
                        message="A user with this email already exists"
                    ).model_dump()
                ),
                409,
            )
        current_app.logger.error(e)
        return jsonify(Failure(message="Internal server error").model_dump()), 500


@auth_bp.post("/login")
def login():
    try:
        payload = request.get_json()
        with get_db_cursor() as cursor:
            cursor.execute(FIND_USER % payload["email"])
            user = cursor.fetchone()
        if user is None:
            return (jsonify(Failure(message="not found").model_dump()), 404)
        pass_matches = compare_with_hash(payload["password"], user[3])
        if pass_matches is True:
            token = encode_jwt_token(user[0])
            return jsonify(Success(data=token).model_dump()), 200
        return jsonify(Failure().model_dump()), 401
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(Failure(message="Internal server error").model_dump()), 500


@auth_bp.post("/verify-email")
def verify_email():
    try:
        payload = request.get_json()
        with get_db_cursor() as cursor:
            cursor.execute(FIND_VERIFICATION_TOKEN % payload["email"])
            token = cursor.fetchone()
            if token is None:
                return jsonify(Failure(message="Invalid token").model_dump()), 401
            if token[2] == payload["token"]:
                cursor.execute(VERIFY_USER % token[1])
                return jsonify(Success().model_dump()), 200
            return jsonify(Failure().model_dump()), 401
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(Failure(message="Internal server error").model_dump()), 500


# TODO: temp route, remove me once routes are protected
@auth_bp.post("/checkjwt")
def checkjwt():
    try:
        payload = request.get_json()
        result = decode_jwt_token(payload["token"])
        if isinstance(result, Success):
            print(result)
            return jsonify(Success(data=result.data).model_dump()), 200
        return jsonify(Failure(message="Invalid token").model_dump()), 401
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(Failure(message="Internal server error").model_dump()), 500
