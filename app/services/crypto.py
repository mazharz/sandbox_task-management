"""crypto module"""

import bcrypt

ENCODING = "utf-8"


def hash_password(raw: str) -> tuple[str, str]:
    """hash password"""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(raw.encode(ENCODING), salt)
    return (hashed.decode(ENCODING), salt.decode(ENCODING))


def compare_with_hash(raw: str, hashed: str) -> bool:
    """compare raw password against its hash"""
    if bcrypt.checkpw(raw.encode(ENCODING), hashed.encode(ENCODING)):
        return True
    return False
