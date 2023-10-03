"""Fixtures for testing account apps."""
from typing import Sequence

from api import PurchaseInvoiceProduct, SaleInvoice, TaxInvoice, TaxInvoiceProduct


def get_tax_products(sale_invoice_id: int) -> Sequence:
    """Get tax invoice products by sale_invoice_id."""
    return (
        TaxInvoiceProduct.query.with_entities(
            TaxInvoiceProduct.id.label("id"),
            TaxInvoiceProduct.sale_invoice_product_id.label("sale_invoice_products_id"),
            TaxInvoiceProduct.purchase_invoice_product_id.label(
                "purchase_invoice_products_id"
            ),
            TaxInvoiceProduct.quantity.label("quantity"),
        )
        .join(TaxInvoice)
        .join(SaleInvoice)
        .filter(SaleInvoice.id == sale_invoice_id)
        .all()
    )


def get_purchase_products(sale_invoice_id: int) -> Sequence:
    """Get puchase invoice products by sale_invoice_id."""
    return (
        PurchaseInvoiceProduct.query.with_entities(
            PurchaseInvoiceProduct.id.label("id"),
            PurchaseInvoiceProduct.products_left.label("products_left"),
        )
        .join(TaxInvoiceProduct)
        .join(TaxInvoice)
        .filter(TaxInvoice.sale_invoice_id == sale_invoice_id)
        .all()
    )
