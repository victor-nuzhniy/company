"""Validators for tax base apps."""
from api import (
    InvoiceProduct,
    PurchaseInvoiceProduct,
    SaleInvoiceProduct,
    TaxInvoice,
    TaxInvoiceProduct,
)
from api.common.services import db_utils


def tax_invoice_id_valid(id_int: int) -> int:
    """Validate tax_invoice_id."""
    if db_utils.is_exists(TaxInvoice, {"id": id_int}):
        return id_int
    raise ValueError(
        "TaxInvoice with id {id} does not exist.".format(id=id_int),
    )


def invoice_products_id_valid(id_int: int) -> int:
    """Validate invoice_products_id."""
    if db_utils.is_exists(InvoiceProduct, {"id": id_int}):
        return id_int
    raise ValueError(
        "InvoiceProduct with id {id} does not exist.".format(
            id=id_int,
        ),
    )


def purchase_invoice_products_id_valid(id_int: int) -> int:
    """Validate purchase_invoice_products_id."""
    if db_utils.is_exists(PurchaseInvoiceProduct, {"id": id_int}):
        return id_int
    raise ValueError(
        "Order with id {id} does not exist.".format(
            id=id_int,
        ),
    )


def sale_invoice_products_id_valid(id_int: int) -> int:
    """Validate sale_invoice_product_id."""
    if db_utils.is_exists(SaleInvoiceProduct, {"id": id_int}):
        return id_int
    raise ValueError(
        "SaleInvoiceProduct with id {id} does not exist.".format(
            id=id_int,
        ),
    )


def tax_invoice_product_id_valid(id_int: int) -> int:
    """Validate tax_invoice_product_id."""
    if db_utils.is_exists(TaxInvoiceProduct, {"id": id_int}):
        return id_int
    raise ValueError(
        "TaxInvoiceProduct with id {id} does not exist.".format(
            id=id_int,
        ),
    )
