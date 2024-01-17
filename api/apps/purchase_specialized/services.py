"""Services for purchase_specialized apps."""
from datetime import datetime
from typing import Sequence

from sqlalchemy import and_, func

from api import (
    Agreement,
    Counterparty,
    Product,
    PurchaseInvoice,
    PurchaseInvoiceProduct,
)


def get_purchase_invoice_data(
    offset: int = 0,
    limit: int = 20,
    date_from: datetime = datetime(1000, 1, 1),
    date_to: datetime = datetime(9000, 1, 1),
) -> Sequence:
    """Get Purchase registry product list."""
    date_from = datetime(1000, 1, 1) if not date_from else date_from
    date_to = datetime(9000, 1, 1) if not date_to else date_to
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
        .outerjoin(PurchaseInvoice.purchase_invoice_products)
        .join(Agreement)
        .join(Counterparty)
        .outerjoin(Product)
        .filter(
            and_(
                PurchaseInvoice.created_at > date_from,
                PurchaseInvoice.created_at < date_to,
            )
        )
        .group_by(PurchaseInvoice)
        .order_by(PurchaseInvoice.id.desc())
        .limit(limit)
        .offset(offset)
        .all()
    )


def get_purchase_invoice_products_by_purchase_id(invoice_id: int) -> Sequence:
    """Get PurchaseInvoices products list by purchase invoice id."""
    return (
        PurchaseInvoiceProduct.query.with_entities(
            PurchaseInvoiceProduct.id.label("id"),
            PurchaseInvoiceProduct.product_id.label("product_id"),
            PurchaseInvoiceProduct.quantity.label("quantity"),
            PurchaseInvoiceProduct.price.label("price"),
            PurchaseInvoiceProduct.products_left.label("products_left"),
            PurchaseInvoiceProduct.purchase_invoice_id.label("purchase_invoice_id"),
            Product.name.label("name"),
            Product.code.label("code"),
            Product.currency.label("currency"),
            Product.units.label("units"),
        )
        .join(Product)
        .filter(PurchaseInvoiceProduct.purchase_invoice_id == invoice_id)
        .all()
    )


def get_purchase_invoice_products_by_product_id_with_products_left(
    product_id: int,
) -> Sequence:
    """Get PurchaseInvoice products list with products_left > 0 and product_id."""
    return (
        PurchaseInvoiceProduct.query.with_entities(
            PurchaseInvoiceProduct.id.label("id"),
            PurchaseInvoiceProduct.product_id.label("product_id"),
            PurchaseInvoiceProduct.products_left.label("products_left"),
            Product.name.label("name"),
            Product.code.label("code"),
        )
        .outerjoin(Product)
        .filter(
            PurchaseInvoiceProduct.products_left > 0,
            PurchaseInvoiceProduct.product_id == product_id,
        )
        .all()
    )
