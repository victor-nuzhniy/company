"""Validators for purchase apps."""
from api import PurchaseInvoice
from api.services import db_utils


def purchase_invoice_id_valid(purchase_invoice_id_int: int) -> int:
    """Validate order_id."""
    if db_utils.is_exists(PurchaseInvoice, {"id": purchase_invoice_id_int}):
        return purchase_invoice_id_int
    raise ValueError(
        "Order with id {id} does not exist.".format(id=purchase_invoice_id_int),
    )
