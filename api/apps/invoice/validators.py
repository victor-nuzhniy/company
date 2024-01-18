"""Validators for invoice apps."""
from api.apps.counterparty import models
from api.apps.invoice import models as invoice_models
from api.apps.order import models as order_models
from api.apps.product import models as product_models
from api.services import db_utils


def order_id_valid(order_id_int: int) -> int:
    """Validate order_id."""
    if db_utils.is_exists(order_models.Order, {"id": order_id_int}):
        return order_id_int
    raise ValueError(
        "Order with id {id} does not exist.".format(id=order_id_int),
    )


def agreement_id_valid(agreement_id_int: int) -> int:
    """Validate agreement_id."""
    if db_utils.is_exists(models.Agreement, {"id": agreement_id_int}):
        return agreement_id_int
    raise ValueError(
        "Agreement with id {id} does not exist.".format(id=agreement_id_int),
    )


def product_id_valid(product_id_int: int) -> int:
    """Validate product_id."""
    if db_utils.is_exists(product_models.Product, {"id": product_id_int}):
        return product_id_int
    raise ValueError(
        "Product with id {id} does not exist.".format(id=product_id_int),
    )


def invoice_id_valid(invoice_id_int: int) -> int:
    """Validate invoice_id."""
    if db_utils.is_exists(invoice_models.Invoice, {"id": invoice_id_int}):
        return invoice_id_int
    raise ValueError(
        "Product with id {id} does not exist.".format(id=invoice_id_int),
    )


def str_hundred(name_str: str) -> str:
    """Validate arg length."""
    if len(name_str) > 100:
        raise ValueError(
            "{name} length should be lower then 100 character.".format(name=name_str),
        )
    return name_str
