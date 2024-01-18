"""Validators for counterparty apps."""
from api.apps.counterparty import models
from api.services import db_utils


def str_thirty(name_str: str) -> str:
    """Validate discount_name."""
    if len(name_str) > 30:
        raise ValueError(
            "{name} length should be lower than 30 character.".format(name=name_str),
        )
    return name_str


def discount_id_valid(discount_id_int: int) -> int:
    """Validate discount id."""
    if db_utils.is_exists(models.Discount, {"id": discount_id_int}):
        return discount_id_int
    raise ValueError(
        "Discount with id {id} does not exist.".format(id=discount_id_int),
    )


def counterparty_id_valid(counterparty_id_int: int) -> int:
    """Validate counterparty_id."""
    if db_utils.is_exists(models.Counterparty, {"id": counterparty_id_int}):
        return counterparty_id_int
    raise ValueError(
        "Counterparty with id {id} does not exist.".format(id=counterparty_id_int),
    )


def str_hundred_fifty(name_str: str) -> str:
    """Validate arg length."""
    if len(name_str) > 150:
        raise ValueError(
            "{name} length should be lower then 150 character.".format(name=name_str),
        )
    return name_str


def str_hundred_fifty_five(name_str: str) -> str:
    """Validate arg length."""
    if len(name_str) > 255:
        raise ValueError(
            "{name} length should be lower then 255 character.".format(name=name_str),
        )
    return name_str


def str_ten(name_str: str) -> str:
    """Validate arg length."""
    if len(name_str) > 10:
        raise ValueError(
            "{name} length should be lower then 10 character.".format(name=name_str),
        )
    return name_str
