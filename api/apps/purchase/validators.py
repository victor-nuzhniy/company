"""Validators for purchase apps."""
from flask import abort

from api import PurchaseInvoice
from api.services import db_utils


def purchase_invoice_id(purchase_invoice_id_int: int) -> int:
    """Validate order_id."""
    if db_utils.is_exists(PurchaseInvoice, {"id": purchase_invoice_id_int}):
        return purchase_invoice_id_int
    abort(409, f"Order with id {purchase_invoice_id_int} does not exist.")
