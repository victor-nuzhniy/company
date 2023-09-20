"""Validators for invoice apps."""
from flask import abort

from api import Agreement, Order
from api.services import db_utils


def order_id(order_id_int) -> int:
    """Validate order_id."""
    if db_utils.is_exists(Order, {"id": order_id_int}):
        return order_id_int
    abort(409, f"Order with id {order_id_int} does not exist.")


def agreement_id(agreement_id_int) -> int:
    """Validate agreement_id."""
    if db_utils.is_exists(Agreement, {"id": agreement_id_int}):
        return agreement_id_int
    abort(409, f"Agreement with id {agreement_id_int} does not exist.")
