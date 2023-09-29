"""Validators for sale apps."""
from api import SaleInvoice
from api.services import db_utils


def sale_invoice_id(sale_invoice_id_int: int) -> int:
    """Validate sale_invoice_id."""
    if db_utils.is_exists(SaleInvoice, {"id": sale_invoice_id_int}):
        return sale_invoice_id_int
    raise ValueError(f"SaleInvoice with id {sale_invoice_id_int} does not exist.")
