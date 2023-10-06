"""DB service functionality for purchase apps."""
from typing import Sequence

from sqlalchemy import func

from api import (
    Agreement,
    Counterparty,
    Product,
    PurchaseInvoice,
    PurchaseInvoiceProduct,
)


def get_purchase_invoice_data(offset: int = 0, limit: int = 20) -> Sequence:
    """Get Purchase registry product list."""
    return (
        PurchaseInvoice.query.with_entities(
            PurchaseInvoice.id.label("id"),
            PurchaseInvoice.created_at.label("created_at"),
            PurchaseInvoice.name.label("purchase_name"),
            Counterparty.name.label("counterparty"),
            Agreement.name.label("agreement"),
            func.sum(
                (PurchaseInvoiceProduct.quantity * PurchaseInvoiceProduct.price)
            ).label("summ"),
            Product.currency.label("currency"),
        )
        .join(PurchaseInvoice.purchase_invoice_products)
        .join(Agreement)
        .join(Counterparty)
        .join(Product)
        .group_by(PurchaseInvoice)
        .limit(limit)
        .offset(offset)
        .all()
    )


def get_purchase_invoice_products_by_purchase_id(invoice_id: int) -> Sequence:
    """Get PurchaseInvoices products list by purchase invoice id."""
    return PurchaseInvoiceProduct.query.filter(
        PurchaseInvoiceProduct.purchase_invoice_id == invoice_id
    ).all()
