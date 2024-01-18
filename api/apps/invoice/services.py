"""DB service functionality for purchase apps."""
from datetime import datetime
from typing import Sequence

from sqlalchemy import and_, func

from api.apps.counterparty import models as counterparty_models
from api.apps.invoice import models as invoice_models
from api.apps.order import models as order_models
from api.apps.product import models as product_models
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
    query = invoice_models.Invoice.query.with_entities(
        invoice_models.Invoice.id.label("id"),
        invoice_models.Invoice.created_at.label("created_at"),
        invoice_models.Invoice.name.label("invoice_name"),
        invoice_models.Invoice.paid.label("paid"),
        invoice_models.Invoice.order_id.label("order_id"),
        invoice_models.Invoice.agreement_id.label("agreement_id"),
        order_models.Order.name.label("order"),
        counterparty_models.Agreement.name.label("agreement"),
        counterparty_models.Counterparty.id.label("counterparty_id"),
        counterparty_models.Counterparty.name.label("counterparty"),
        func.sum(
            (
                invoice_models.InvoiceProduct.quantity
                * invoice_models.InvoiceProduct.price
            ),
        ).label("summ"),
        product_models.Product.currency.label("currency"),
    ).outerjoin(invoice_models.Invoice.invoice_products)
    additional_query = (
        query.join(counterparty_models.Agreement)
        .join(order_models.Order)
        .join(counterparty_models.Counterparty)
        .outerjoin(product_models.Product)
    )
    return (
        additional_query.filter(
            and_(
                invoice_models.Invoice.created_at > date_from,
                invoice_models.Invoice.created_at < date_to,
            ),
        )
        .group_by(invoice_models.Invoice)
        .order_by(invoice_models.Invoice.id.desc())
        .limit(limit)
        .offset(offset)
        .all()
    )


def get_invoice_products_by_invoice_id(invoice_id: int) -> Sequence:
    """Get Invoices products list by invoice id."""
    return (
        invoice_models.InvoiceProduct.query.with_entities(
            invoice_models.InvoiceProduct.id.label("id"),
            invoice_models.InvoiceProduct.product_id.label("product_id"),
            invoice_models.InvoiceProduct.quantity.label("quantity"),
            invoice_models.InvoiceProduct.price.label("price"),
            invoice_models.InvoiceProduct.invoice_id.label("invoice_id"),
            product_models.Product.name.label("name"),
            product_models.Product.code.label("code"),
            product_models.Product.currency.label("currency"),
            product_models.Product.units.label("units"),
        )
        .join(product_models.Product)
        .filter(invoice_models.InvoiceProduct.invoice_id == invoice_id)
        .all()
    )
