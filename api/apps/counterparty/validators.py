"""Validators for counterparty apps."""
from flask import abort

from api import Counterparty, Discount
from api.services import db_utils


def discount_name(name_str):
    """Validate discount_name."""
    if len(name_str) > 30:
        abort(422, f"{name_str} length should be lower than 30 character.")
    return name_str


def discount_id(discount_id_int) -> int:
    """Validate discount id."""
    if db_utils.is_exists(Discount, {"id": discount_id_int}):
        return discount_id_int
    abort(409, f"Discount with id {discount_id_int} does not exist.")


def counterparty_id(counterparty_id_int) -> int:
    """Validate counterparty_id."""
    if db_utils.is_exists(Counterparty, {"id": counterparty_id_int}):
        return counterparty_id_int
    abort(409, f"Counterparty with id {counterparty_id_int} does not exist.")
