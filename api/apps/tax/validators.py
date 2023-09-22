"""Validators for tax apps."""
from flask import abort

from api import InvoiceProduct, PurchaseInvoiceProduct, TaxInvoice
from api.services import db_utils


def tax_invoice_id(tax_invoice_id_int: int) -> int:
    """Validate order_id."""
    if db_utils.is_exists(TaxInvoice, {"id": tax_invoice_id_int}):
        return tax_invoice_id_int
    abort(409, f"Order with id {tax_invoice_id_int} does not exist.")


def invoice_products_id(invoice_products_id_int: int) -> int:
    """Validate order_id."""
    if db_utils.is_exists(InvoiceProduct, {"id": invoice_products_id_int}):
        return invoice_products_id_int
    abort(409, f"Order with id {invoice_products_id_int} does not exist.")


def purchase_invoice_products_id(purchase_invoice_products_id_int: int) -> int:
    """Validate order_id."""
    if db_utils.is_exists(
        PurchaseInvoiceProduct, {"id": purchase_invoice_products_id_int}
    ):
        return purchase_invoice_products_id_int
    abort(409, f"Order with id {purchase_invoice_products_id_int} does not exist.")
