"""DB service functionality for tax apps."""
from datetime import datetime
from typing import Any, Sequence

from flask import abort
from sqlalchemy import func

from api import db
from api.apps.counterparty import models as counterparty_models
from api.apps.invoice import models as invoice_models
from api.apps.product import models as product_models
from api.apps.purchase import models as purchase_models
from api.apps.sale import models as sale_models
from api.apps.tax import models as tax_models
from api.constants import EARLIEST_DATE, LATEST_DATE


def get_tax_data(
    offset: int = 0,
    limit: int = 20,
    date_from: datetime = EARLIEST_DATE,
    date_to: datetime = LATEST_DATE,
) -> Sequence:
    """Get Tax registry list."""
    date_from = date_from if date_from else EARLIEST_DATE
    date_to = date_to if date_to else LATEST_DATE
    query = (
        tax_models.TaxInvoice.query.with_entities(
            tax_models.TaxInvoice.id.label("id"),
            tax_models.TaxInvoice.created_at.label("created_at"),
            tax_models.TaxInvoice.name.label("tax_invoice_name"),
            tax_models.TaxInvoice.sale_invoice_id.label("sale_invoice_id"),
            sale_models.SaleInvoice.name.label("sale_invoice"),
            invoice_models.Invoice.name.label("invoice"),
            invoice_models.Invoice.id.label("invoice_id"),
            purchase_models.PurchaseInvoice.name.label("purchase_invoice"),
            purchase_models.PurchaseInvoice.id.label("purchase_invoice_id"),
            counterparty_models.Agreement.name.label("agreement"),
            counterparty_models.Agreement.id.label("agreement_id"),
            counterparty_models.Counterparty.name.label("counterparty"),
            counterparty_models.Counterparty.id.label("counterparty_id"),
            func.sum(
                (
                    tax_models.TaxInvoiceProduct.quantity
                    * sale_models.SaleInvoiceProduct.price
                ),
            ).label(
                "sale_summ",
            ),
            func.sum(
                (
                    tax_models.TaxInvoiceProduct.quantity
                    * purchase_models.PurchaseInvoiceProduct.price
                ),
            ).label(
                "purchase_summ",
            ),
        )
        .outerjoin(
            sale_models.SaleInvoice,
            sale_models.SaleInvoice.id == tax_models.TaxInvoice.sale_invoice_id,
        )
        .outerjoin(
            invoice_models.Invoice,
            invoice_models.Invoice.id == sale_models.SaleInvoice.invoice_id,
        )
        .outerjoin(
            counterparty_models.Agreement,
            counterparty_models.Agreement.id == invoice_models.Invoice.agreement_id,
        )
        .outerjoin(
            counterparty_models.Counterparty,
            counterparty_models.Counterparty.id
            == counterparty_models.Agreement.counterparty_id,
        )
    )
    additional_query = (
        query.outerjoin(
            tax_models.TaxInvoiceProduct,
            tax_models.TaxInvoiceProduct.tax_invoice_id == tax_models.TaxInvoice.id,
        )
        .outerjoin(
            sale_models.SaleInvoiceProduct,
            sale_models.SaleInvoiceProduct.id
            == tax_models.TaxInvoiceProduct.sale_invoice_product_id,
        )
        .outerjoin(
            purchase_models.PurchaseInvoiceProduct,
            purchase_models.PurchaseInvoiceProduct.id
            == tax_models.TaxInvoiceProduct.purchase_invoice_product_id,
        )
        .outerjoin(
            purchase_models.PurchaseInvoice,
            purchase_models.PurchaseInvoice.id
            == purchase_models.PurchaseInvoiceProduct.purchase_invoice_id,
        )
    )
    return (
        additional_query.filter(
            tax_models.TaxInvoice.created_at > date_from,
            tax_models.TaxInvoice.created_at < date_to,
        )
        .group_by(tax_models.TaxInvoice)
        .order_by(tax_models.TaxInvoice.id.desc())
        .limit(limit)
        .offset(offset)
        .all()
    )


def get_tax_invoice_products_by_tax_invoice_id(tax_invoice_id: int) -> Sequence:
    """Get TaxInvoice products list by tax invoice id."""
    return (
        db.session.query(
            tax_models.TaxInvoiceProduct.id.label("id"),
            tax_models.TaxInvoiceProduct.quantity.label("quantity"),
            tax_models.TaxInvoiceProduct.tax_invoice_id.label("tax_invoice_id"),
            tax_models.TaxInvoiceProduct.sale_invoice_product_id.label(
                "sale_invoice_product_id",
            ),
            tax_models.TaxInvoiceProduct.purchase_invoice_product_id.label(
                "purchase_invoice_product_id",
            ),
            sale_models.SaleInvoiceProduct.price.label("sale_price"),
            purchase_models.PurchaseInvoiceProduct.price.label("purchase_price"),
            product_models.Product.name.label("name"),
            product_models.Product.code.label("code"),
            product_models.Product.currency.label("currency"),
            product_models.Product.units.label("units"),
        )
        .select_from(
            tax_models.TaxInvoiceProduct,
            sale_models.SaleInvoiceProduct,
            product_models.Product,
            purchase_models.PurchaseInvoiceProduct,
        )
        .outerjoin(tax_models.TaxInvoiceProduct.sale_invoice_products)
        .filter(
            sale_models.SaleInvoiceProduct.id
            == tax_models.TaxInvoiceProduct.sale_invoice_product_id,
            purchase_models.PurchaseInvoiceProduct.id
            == tax_models.TaxInvoiceProduct.purchase_invoice_product_id,
            sale_models.SaleInvoiceProduct.product_id == product_models.Product.id,
            tax_models.TaxInvoiceProduct.tax_invoice_id == tax_invoice_id,
        )
        .all()
    )


def create_tax_invoice_products(
    **kwargs: Any,
) -> tax_models.TaxInvoiceProduct:
    """Create TaxInvoiceProduct with subtracting purhcase products_left field."""
    purchase_invoice_product = (
        purchase_models.PurchaseInvoiceProduct.query.with_entities(
            purchase_models.PurchaseInvoiceProduct.products_left,
        )
        .filter(
            purchase_models.PurchaseInvoiceProduct.id
            == kwargs.get("purchase_invoice_product_id"),
        )
        .first()
    )
    if purchase_invoice_product.products_left < kwargs.get("quantity"):
        abort(409, "There are not enough products left.")
    tax_invoice_product = tax_models.TaxInvoiceProduct(**kwargs)
    db.session.add(tax_invoice_product)
    db.session.query(purchase_models.PurchaseInvoiceProduct).filter_by(
        id=tax_invoice_product.purchase_invoice_product_id,
    ).update(
        {
            "products_left": purchase_models.PurchaseInvoiceProduct.products_left
            - tax_invoice_product.quantity,
        },
    )
    db.session.commit()
    return tax_invoice_product


def delete_tax_invoice_products(
    tax_invoice_product_id: int,
) -> None:
    """Delete TaxInvoiceProduct with adding purchase products_left field."""
    tax_invoice_product = tax_models.TaxInvoiceProduct.query.filter(
        tax_models.TaxInvoiceProduct.id == tax_invoice_product_id,
    ).first()
    db.session.query(purchase_models.PurchaseInvoiceProduct).filter_by(
        id=tax_invoice_product.purchase_invoice_product_id,
    ).update(
        {
            "products_left": purchase_models.PurchaseInvoiceProduct.products_left
            + tax_invoice_product.quantity,
        },
    )
    tax_models.TaxInvoiceProduct.query.filter(
        tax_models.TaxInvoiceProduct.id == tax_invoice_product_id,
    ).delete()
    db.session.commit()


def delete_tax_invoice(
    tax_invoice_id: int,
) -> None:
    """Delete TaxInvoice with adding purchase products_left fields."""
    tax_invoice_products = tax_models.TaxInvoiceProduct.query.filter(
        tax_models.TaxInvoiceProduct.tax_invoice_id == tax_invoice_id,
    ).all()
    for product in tax_invoice_products:
        db.session.query(purchase_models.PurchaseInvoiceProduct).filter_by(
            id=product.purchase_invoice_product_id,
        ).update(
            {
                "products_left": (
                    purchase_models.PurchaseInvoiceProduct.products_left
                    + product.quantity
                ),
            },
        )
        db.session.commit()
    tax_models.TaxInvoice.query.filter(
        tax_models.TaxInvoice.id == tax_invoice_id,
    ).delete()
    db.session.commit()
