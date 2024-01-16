"""DB service functionality for purchase apps."""
from datetime import datetime
from typing import Sequence

from sqlalchemy import and_, func

from api import Agreement, Counterparty, Invoice, InvoiceProduct, Order, Product
from api.constants import EARLIEST_DATE, LATEST_DATE


def get_invoice_data(
    offset: int = 0,
    limit: int = 20,
    date_from: datetime = EARLIEST_DATE,
    date_to: datetime = LATEST_DATE,
) -> Sequence:
    """Get Invoice registry list."""
    date_from = date_from if date_from else EARLIEST_DATE
    date_to = date_to if date_to else LATEST_DATE
    query = (
        Invoice.query.with_entities(
            Invoice.id.label("id"),
            Invoice.created_at.label("created_at"),
            Invoice.name.label("invoice_name"),
            Invoice.paid.label("paid"),
            Invoice.order_id.label("order_id"),
            Invoice.agreement_id.label("agreement_id"),
            Order.name.label("order"),
            Agreement.name.label("agreement"),
            Counterparty.id.label("counterparty_id"),
            Counterparty.name.label("counterparty"),
            func.sum((InvoiceProduct.quantity * InvoiceProduct.price)).label("summ"),
            Product.currency.label("currency"),
        )
        .outerjoin(Invoice.invoice_products)
        .join(Agreement)
        .join(Order)
        .join(Counterparty)
        .outerjoin(Product)
    )
    return (
        query
        .filter(and_(Invoice.created_at > date_from, Invoice.created_at < date_to))
        .group_by(Invoice)
        .order_by(Invoice.id.desc())
        .limit(limit)
        .offset(offset)
        .all()
    )


def get_invoice_products_by_invoice_id(invoice_id: int) -> Sequence:
    """Get Invoices products list by invoice id."""
    return (
        InvoiceProduct.query.with_entities(
            InvoiceProduct.id.label("id"),
            InvoiceProduct.product_id.label("product_id"),
            InvoiceProduct.quantity.label("quantity"),
            InvoiceProduct.price.label("price"),
            InvoiceProduct.invoice_id.label("invoice_id"),
            Product.name.label("name"),
            Product.code.label("code"),
            Product.currency.label("currency"),
            Product.units.label("units"),
        )
        .join(Product)
        .filter(InvoiceProduct.invoice_id == invoice_id)
        .all()
    )
