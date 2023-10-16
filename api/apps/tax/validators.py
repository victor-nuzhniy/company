"""Validators for tax apps."""
from api import (
    InvoiceProduct,
    PurchaseInvoiceProduct,
    SaleInvoiceProduct,
    TaxInvoice,
    TaxInvoiceProduct,
)
from api.services import db_utils


def tax_invoice_id(tax_invoice_id_int: int) -> int:
    """Validate tax_invoice_id."""
    if db_utils.is_exists(TaxInvoice, {"id": tax_invoice_id_int}):
        return tax_invoice_id_int
    raise ValueError(f"TaxInvoice with id {tax_invoice_id_int} does not exist.")


def invoice_products_id(invoice_products_id_int: int) -> int:
    """Validate invoice_products_id."""
    if db_utils.is_exists(InvoiceProduct, {"id": invoice_products_id_int}):
        return invoice_products_id_int
    raise ValueError(
        f"InvoiceProduct with id {invoice_products_id_int} does not exist."
    )


def purchase_invoice_products_id(purchase_invoice_products_id_int: int) -> int:
    """Validate purchase_invoice_products_id."""
    if db_utils.is_exists(
        PurchaseInvoiceProduct, {"id": purchase_invoice_products_id_int}
    ):
        return purchase_invoice_products_id_int
    raise ValueError(
        f"Order with id {purchase_invoice_products_id_int} does not exist."
    )


def sale_invoice_products_id(sale_invoice_products_id_int: int) -> int:
    """Validate sale_invoice_product_id."""
    if db_utils.is_exists(SaleInvoiceProduct, {"id": sale_invoice_products_id_int}):
        return sale_invoice_products_id_int
    raise ValueError(
        f"SaleInvoiceProduct with id {sale_invoice_products_id_int} does not exist."
    )


def tax_invoice_product_id(tax_invoice_product_id_int: int) -> int:
    """Validate tax_invoice_product_id."""
    if db_utils.is_exists(TaxInvoiceProduct, {"id": tax_invoice_product_id_int}):
        return tax_invoice_product_id_int
    raise ValueError(
        f"TaxInvoiceProduct with id {tax_invoice_product_id_int} does not exist."
    )
