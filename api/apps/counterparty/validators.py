"""Validators for counterparty apps."""
from api import Counterparty, Discount
from api.services import db_utils


def str_length_30(name_str):
    """Validate discount_name."""
    if len(name_str) > 30:
        raise ValueError(f"{name_str} length should be lower than 30 character.")
    return name_str


def discount_id(discount_id_int) -> int:
    """Validate discount id."""
    if db_utils.is_exists(Discount, {"id": discount_id_int}):
        return discount_id_int
    raise ValueError(f"Discount with id {discount_id_int} does not exist.")


def counterparty_id(counterparty_id_int) -> int:
    """Validate counterparty_id."""
    if db_utils.is_exists(Counterparty, {"id": counterparty_id_int}):
        return counterparty_id_int
    raise ValueError(f"Counterparty with id {counterparty_id_int} does not exist.")


def str_length_150(name_str: str) -> str:
    """Validate arg length."""
    if len(name_str) > 150:
        raise ValueError(f"{name_str} length should be lower then 150 character.")
    return name_str


def str_length_255(name_str: str) -> str:
    """Validate arg length."""
    if len(name_str) > 255:
        raise ValueError(f"{name_str} length should be lower then 255 character.")
    return name_str


def str_length_10(name_str: str) -> str:
    """Validate arg length."""
    if len(name_str) > 10:
        raise ValueError(f"{name_str} length should be lower then 10 character.")
    return name_str
