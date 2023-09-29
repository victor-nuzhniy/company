"""Validators for order apps."""
from api import User
from api.services import db_utils


def user_id(user_id_int: int) -> int:
    """Validate user_id."""
    if db_utils.is_exists(User, {"id": user_id_int}):
        return user_id_int
    raise ValueError(f"User with id {user_id_int} does not exist.")
