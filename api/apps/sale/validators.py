"""Validators for sale apps."""
from api.apps.sale import models
from api.services import db_utils


def sale_invoice_id_valid(sale_invoice_id_int: int) -> int:
    """Validate sale_invoice_id."""
    if db_utils.is_exists(models.SaleInvoice, {"id": sale_invoice_id_int}):
        return sale_invoice_id_int
    raise ValueError(
        "SaleInvoice with id {id} does not exist.".format(id=sale_invoice_id_int),
    )
