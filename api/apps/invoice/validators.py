"""Validators for invoice apps."""
from api import Agreement, Invoice, Order, Product
from api.services import db_utils


def order_id(order_id_int: int) -> int:
    """Validate order_id."""
    if db_utils.is_exists(Order, {"id": order_id_int}):
        return order_id_int
    raise ValueError(f"Order with id {order_id_int} does not exist.")


def agreement_id(agreement_id_int: int) -> int:
    """Validate agreement_id."""
    if db_utils.is_exists(Agreement, {"id": agreement_id_int}):
        return agreement_id_int
    raise ValueError(f"Agreement with id {agreement_id_int} does not exist.")


def product_id(product_id_int: int) -> int:
    """Validate product_id."""
    if db_utils.is_exists(Product, {"id": product_id_int}):
        return product_id_int
    raise ValueError(f"Product with id {product_id_int} does not exist.")


def invoice_id(invoice_id_int: int) -> int:
    """Validate invoice_id."""
    if db_utils.is_exists(Invoice, {"id": invoice_id_int}):
        return invoice_id_int
    raise ValueError(f"Product with id {invoice_id_int} does not exist.")


def str_length_100(name_str: str) -> str:
    """Validate arg length."""
    if len(name_str) > 100:
        raise ValueError(f"{name_str} length should be lower then 100 character.")
    return name_str
