"""crypto module"""

from datetime import datetime, timedelta, timezone

import os
import jwt
import bcrypt
import dotenv

from app.core.result import Failure, Result, Success

dotenv.load_dotenv()
ENCODING = "utf-8"
JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")


def hash_password(raw: str) -> tuple[str, str]:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(raw.encode(ENCODING), salt)
    return (hashed.decode(ENCODING), salt.decode(ENCODING))


def compare_with_hash(raw: str, hashed: str) -> bool:
    if bcrypt.checkpw(raw.encode(ENCODING), hashed.encode(ENCODING)):
        return True
    return False


def encode_jwt_token(user_id: int) -> str:
    payload = {
        "user_id": user_id,
        "exp": datetime.now(timezone.utc) + timedelta(days=30),
    }
    token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
    return token


def decode_jwt_token(token: str) -> Result:
    try:
        data = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
        print(data)
        return Success[int](data=data["user_id"])
    except Exception:
        return Failure()
