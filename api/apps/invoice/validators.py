"""Validators for invoice apps."""
from flask import abort

from api import Agreement, Invoice, Order, Product
from api.services import db_utils


def order_id(order_id_int: int) -> int:
    """Validate order_id."""
    if db_utils.is_exists(Order, {"id": order_id_int}):
        return order_id_int
    abort(409, f"Order with id {order_id_int} does not exist.")


def agreement_id(agreement_id_int: int) -> int:
    """Validate agreement_id."""
    if db_utils.is_exists(Agreement, {"id": agreement_id_int}):
        return agreement_id_int
    abort(409, f"Agreement with id {agreement_id_int} does not exist.")


def product_id(product_id_int: int) -> int:
    """Validate product_id."""
    if db_utils.is_exists(Product, {"id": product_id_int}):
        return product_id_int
    abort(409, f"Product with id {product_id_int} does not exist.")


def invoice_id(invoice_id_int: int) -> int:
    """Validate product_id."""
    if db_utils.is_exists(Invoice, {"id": invoice_id_int}):
        return invoice_id_int
    abort(409, f"Product with id {invoice_id_int} does not exist.")


def str_length_100(name_str: str) -> str:
    """Validate sale_invoice name."""
    if len(name_str) > 100:
        abort(422, f"{name_str} length should be lower then 100 character.")
    return name_str
