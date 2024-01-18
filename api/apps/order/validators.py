"""Validators for order apps."""
from api.apps.user import models
from api.services import db_utils


def user_id_valid(user_id_int: int) -> int:
    """Validate user_id."""
    if db_utils.is_exists(models.User, {"id": user_id_int}):
        return user_id_int
    raise ValueError(
        "User with id {id} does not exist.".format(id=user_id_int),
    )
