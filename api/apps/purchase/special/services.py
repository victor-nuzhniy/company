"""Services for purchase special apps."""
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
from api.common.constants import EARLIEST_DATE, LATEST_DATE


def get_purchase_invoice_data(
    offset: int = 0,
    limit: int = 20,
    date_from: datetime = EARLIEST_DATE,
    date_to: datetime = LATEST_DATE,
) -> Sequence:
    """Get Purchase registry base list."""
    date_from = date_from if date_from else EARLIEST_DATE
    date_to = date_to if date_to else LATEST_DATE
    query = (
        PurchaseInvoice.query.with_entities(
            PurchaseInvoice.id.label("id"),
            PurchaseInvoice.created_at.label("created_at"),
            PurchaseInvoice.name.label("purchase_name"),
            Counterparty.name.label("counterparty"),
            Agreement.name.label("agreement"),
            func.sum(
                (PurchaseInvoiceProduct.quantity * PurchaseInvoiceProduct.price),
            ).label("summ"),
            Product.currency.label("currency"),
        )
        .outerjoin(PurchaseInvoice.purchase_invoice_products)
        .join(Agreement)
        .join(Counterparty)
        .outerjoin(Product)
    )
    return (
        query.filter(
            and_(
                PurchaseInvoice.created_at > date_from,
                PurchaseInvoice.created_at < date_to,
            ),
        )
        .group_by(PurchaseInvoice)
        .order_by(PurchaseInvoice.id.desc())
        .limit(limit)
        .offset(offset)
        .all()
    )


def get_purchase_invoice_products_by_purchase_id(invoice_id: int) -> Sequence:
    """Get PurchaseInvoices products list by base base id."""
    return (
        PurchaseInvoiceProduct.query.with_entities(
            PurchaseInvoiceProduct.id.label("id"),
            PurchaseInvoiceProduct.product_id.label("product_id"),
            PurchaseInvoiceProduct.quantity.label("quantity"),
            PurchaseInvoiceProduct.price.label("price"),
            PurchaseInvoiceProduct.products_left.label("products_left"),
            PurchaseInvoiceProduct.purchase_invoice_id.label(
                "purchase_invoice_id",
            ),
            Product.name.label("name"),
            Product.code.label("code"),
            Product.currency.label("currency"),
            Product.units.label("units"),
        )
        .join(Product)
        .filter(
            PurchaseInvoiceProduct.purchase_invoice_id == invoice_id,
        )
        .all()
    )


def get_pur_inv_prod_by_prod_id_with_prod_left(
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
