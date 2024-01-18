"""Services for purchase_specialized apps."""
from datetime import datetime
from typing import Sequence

from sqlalchemy import and_, func

from api.apps.counterparty import models as counterparty_models
from api.apps.product import models as product_models
from api.apps.purchase import models as purchase_models
from api.constants import EARLIEST_DATE, LATEST_DATE


def get_purchase_invoice_data(
    offset: int = 0,
    limit: int = 20,
    date_from: datetime = EARLIEST_DATE,
    date_to: datetime = LATEST_DATE,
) -> Sequence:
    """Get Purchase registry product list."""
    date_from = date_from if date_from else EARLIEST_DATE
    date_to = date_to if date_to else LATEST_DATE
    query = (
        purchase_models.PurchaseInvoice.query.with_entities(
            purchase_models.PurchaseInvoice.id.label("id"),
            purchase_models.PurchaseInvoice.created_at.label("created_at"),
            purchase_models.PurchaseInvoice.name.label("purchase_name"),
            counterparty_models.Counterparty.name.label("counterparty"),
            counterparty_models.Agreement.name.label("agreement"),
            func.sum(
                (
                    purchase_models.PurchaseInvoiceProduct.quantity
                    * purchase_models.PurchaseInvoiceProduct.price
                ),
            ).label("summ"),
            product_models.Product.currency.label("currency"),
        )
        .outerjoin(purchase_models.PurchaseInvoice.purchase_invoice_products)
        .join(counterparty_models.Agreement)
        .join(counterparty_models.Counterparty)
        .outerjoin(product_models.Product)
    )
    return (
        query.filter(
            and_(
                purchase_models.PurchaseInvoice.created_at > date_from,
                purchase_models.PurchaseInvoice.created_at < date_to,
            ),
        )
        .group_by(purchase_models.PurchaseInvoice)
        .order_by(purchase_models.PurchaseInvoice.id.desc())
        .limit(limit)
        .offset(offset)
        .all()
    )


def get_purchase_invoice_products_by_purchase_id(invoice_id: int) -> Sequence:
    """Get PurchaseInvoices products list by purchase invoice id."""
    return (
        purchase_models.PurchaseInvoiceProduct.query.with_entities(
            purchase_models.PurchaseInvoiceProduct.id.label("id"),
            purchase_models.PurchaseInvoiceProduct.product_id.label("product_id"),
            purchase_models.PurchaseInvoiceProduct.quantity.label("quantity"),
            purchase_models.PurchaseInvoiceProduct.price.label("price"),
            purchase_models.PurchaseInvoiceProduct.products_left.label("products_left"),
            purchase_models.PurchaseInvoiceProduct.purchase_invoice_id.label(
                "purchase_invoice_id",
            ),
            product_models.Product.name.label("name"),
            product_models.Product.code.label("code"),
            product_models.Product.currency.label("currency"),
            product_models.Product.units.label("units"),
        )
        .join(product_models.Product)
        .filter(
            purchase_models.PurchaseInvoiceProduct.purchase_invoice_id == invoice_id,
        )
        .all()
    )


def get_pur_inv_prod_by_prod_id_with_prod_left(
    product_id: int,
) -> Sequence:
    """Get PurchaseInvoice products list with products_left > 0 and product_id."""
    return (
        purchase_models.PurchaseInvoiceProduct.query.with_entities(
            purchase_models.PurchaseInvoiceProduct.id.label("id"),
            purchase_models.PurchaseInvoiceProduct.product_id.label("product_id"),
            purchase_models.PurchaseInvoiceProduct.products_left.label("products_left"),
            product_models.Product.name.label("name"),
            product_models.Product.code.label("code"),
        )
        .outerjoin(product_models.Product)
        .filter(
            purchase_models.PurchaseInvoiceProduct.products_left > 0,
            purchase_models.PurchaseInvoiceProduct.product_id == product_id,
        )
        .all()
    )
