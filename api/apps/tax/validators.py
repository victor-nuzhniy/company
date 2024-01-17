"""Validators for tax apps."""
from api import (
    InvoiceProduct,
    PurchaseInvoiceProduct,
    SaleInvoiceProduct,
    TaxInvoice,
    TaxInvoiceProduct,
)
from api.services import db_utils


def tax_invoice_id_valid(tax_invoice_id_int: int) -> int:
    """Validate tax_invoice_id."""
    if db_utils.is_exists(TaxInvoice, {"id": tax_invoice_id_int}):
        return tax_invoice_id_int
    raise ValueError(
        "TaxInvoice with id {id} does not exist.".format(id=tax_invoice_id_int),
    )


def invoice_products_id_valid(invoice_products_id_int: int) -> int:
    """Validate invoice_products_id."""
    if db_utils.is_exists(InvoiceProduct, {"id": invoice_products_id_int}):
        return invoice_products_id_int
    raise ValueError(
        "InvoiceProduct with id {id} does not exist.".format(
            id=invoice_products_id_int,
        ),
    )


def purchase_invoice_products_id_valid(pur_inv_prod_id_int: int) -> int:
    """Validate purchase_invoice_products_id."""
    if db_utils.is_exists(PurchaseInvoiceProduct, {"id": pur_inv_prod_id_int}):
        return pur_inv_prod_id_int
    raise ValueError(
        "Order with id {id} does not exist.".format(
            id=pur_inv_prod_id_int,
        ),
    )


def sale_invoice_products_id_valid(sale_invoice_products_id_int: int) -> int:
    """Validate sale_invoice_product_id."""
    if db_utils.is_exists(SaleInvoiceProduct, {"id": sale_invoice_products_id_int}):
        return sale_invoice_products_id_int
    raise ValueError(
        "SaleInvoiceProduct with id {id} does not exist.".format(
            id=sale_invoice_products_id_int,
        ),
    )


def tax_invoice_product_id_valid(tax_invoice_product_id_int: int) -> int:
    """Validate tax_invoice_product_id."""
    if db_utils.is_exists(TaxInvoiceProduct, {"id": tax_invoice_product_id_int}):
        return tax_invoice_product_id_int
    raise ValueError(
        "TaxInvoiceProduct with id {id} does not exist.".format(
            id=tax_invoice_product_id_int,
        ),
    )
