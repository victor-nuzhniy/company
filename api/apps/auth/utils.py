"""Utilities for auth apps."""
from typing import Optional

from werkzeug.security import check_password_hash, generate_password_hash

from api import User
from api.services import crud


def login(email: str, password: str) -> Optional[User]:
    """Login and return user."""
    user = crud.read(User, {"email": email})
    if not user or check_password_hash(user.password, password):
        return
    return user


def disable_account(user_id: int) -> User:
    """Disable user account - is_active to False."""
    return crud.update(User, {"is_active": False}, {"id": user_id})


def encrypt_password(password: str) -> str:
    """Encrypt password."""
    return generate_password_hash(password, salt_length=4)  # TODO change length
