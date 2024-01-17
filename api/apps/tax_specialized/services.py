"""DB service functionality for tax apps."""
from datetime import datetime
from typing import Any, Sequence

from flask import abort
from sqlalchemy import func

from api import (
    Agreement,
    Counterparty,
    Invoice,
    Product,
    PurchaseInvoice,
    PurchaseInvoiceProduct,
    SaleInvoice,
    SaleInvoiceProduct,
    TaxInvoice,
    TaxInvoiceProduct,
    db,
)


def get_tax_data(
    offset: int = 0,
    limit: int = 20,
    date_from: datetime = datetime(1000, 1, 1),
    date_to: datetime = datetime(9000, 1, 1),
) -> Sequence:
    """Get Tax registry list."""
    date_from = datetime(1000, 1, 1) if not date_from else date_from
    date_to = datetime(9000, 1, 1) if not date_to else date_to
    return (
        TaxInvoice.query.with_entities(
            TaxInvoice.id.label("id"),
            TaxInvoice.created_at.label("created_at"),
            TaxInvoice.name.label("tax_invoice_name"),
            TaxInvoice.sale_invoice_id.label("sale_invoice_id"),
            SaleInvoice.name.label("sale_invoice"),
            Invoice.name.label("invoice"),
            Invoice.id.label("invoice_id"),
            PurchaseInvoice.name.label("purchase_invoice"),
            PurchaseInvoice.id.label("purchase_invoice_id"),
            Agreement.name.label("agreement"),
            Agreement.id.label("agreement_id"),
            Counterparty.name.label("counterparty"),
            Counterparty.id.label("counterparty_id"),
            func.sum((TaxInvoiceProduct.quantity * SaleInvoiceProduct.price)).label(
                "sale_summ"
            ),
            func.sum((TaxInvoiceProduct.quantity * PurchaseInvoiceProduct.price)).label(
                "purchase_summ"
            ),
        )
        .outerjoin(SaleInvoice, SaleInvoice.id == TaxInvoice.sale_invoice_id)
        .outerjoin(Invoice, Invoice.id == SaleInvoice.invoice_id)
        .outerjoin(Agreement, Agreement.id == Invoice.agreement_id)
        .outerjoin(Counterparty, Counterparty.id == Agreement.counterparty_id)
        .outerjoin(TaxInvoiceProduct, TaxInvoiceProduct.tax_invoice_id == TaxInvoice.id)
        .outerjoin(
            SaleInvoiceProduct,
            SaleInvoiceProduct.id == TaxInvoiceProduct.sale_invoice_product_id,
        )
        .outerjoin(
            PurchaseInvoiceProduct,
            PurchaseInvoiceProduct.id == TaxInvoiceProduct.purchase_invoice_product_id,
        )
        .outerjoin(
            PurchaseInvoice,
            PurchaseInvoice.id == PurchaseInvoiceProduct.purchase_invoice_id,
        )
        .filter(
            TaxInvoice.created_at > date_from,
            TaxInvoice.created_at < date_to,
        )
        .group_by(TaxInvoice)
        .order_by(TaxInvoice.id.desc())
        .limit(limit)
        .offset(offset)
        .all()
    )


def get_tax_invoice_products_by_tax_invoice_id(tax_invoice_id: int) -> Sequence:
    """Get TaxInvoice products list by tax invoice id."""
    return (
        db.session.query(
            TaxInvoiceProduct.id.label("id"),
            TaxInvoiceProduct.quantity.label("quantity"),
            TaxInvoiceProduct.tax_invoice_id.label("tax_invoice_id"),
            TaxInvoiceProduct.sale_invoice_product_id.label("sale_invoice_product_id"),
            TaxInvoiceProduct.purchase_invoice_product_id.label(
                "purchase_invoice_product_id"
            ),
            SaleInvoiceProduct.price.label("sale_price"),
            PurchaseInvoiceProduct.price.label("purchase_price"),
            Product.name.label("name"),
            Product.code.label("code"),
            Product.currency.label("currency"),
            Product.units.label("units"),
        )
        .select_from(
            TaxInvoiceProduct,
            SaleInvoiceProduct,
            Product,
            PurchaseInvoiceProduct,
        )
        .outerjoin(TaxInvoiceProduct.sale_invoice_products)
        .filter(
            SaleInvoiceProduct.id == TaxInvoiceProduct.sale_invoice_product_id,
            PurchaseInvoiceProduct.id == TaxInvoiceProduct.purchase_invoice_product_id,
            SaleInvoiceProduct.product_id == Product.id,
            TaxInvoiceProduct.tax_invoice_id == tax_invoice_id,
        )
        .all()
    )


def create_tax_invoice_product_with_subtract_purchase_products_left(
    **kwargs: Any,
) -> TaxInvoiceProduct:
    """Create TaxInvoiceProduct with subtracting purhcase products_left field."""
    purchase_invoice_product = (
        PurchaseInvoiceProduct.query.with_entities(PurchaseInvoiceProduct.products_left)
        .filter(PurchaseInvoiceProduct.id == kwargs.get("purchase_invoice_product_id"))
        .first()
    )
    if purchase_invoice_product.products_left < kwargs.get("quantity"):
        abort(409, "There are not enough products left.")
    tax_invoice_product = TaxInvoiceProduct(**kwargs)
    db.session.add(tax_invoice_product)
    db.session.query(PurchaseInvoiceProduct).filter_by(
        id=tax_invoice_product.purchase_invoice_product_id
    ).update(
        {
            "products_left": PurchaseInvoiceProduct.products_left
            - tax_invoice_product.quantity
        }
    )
    db.session.commit()
    return tax_invoice_product


def delete_tax_invoice_product_with_adding_purchase_products_left(
    tax_invoice_product_id: int,
) -> None:
    """Delete TaxInvoiceProduct with adding purchase products_left field."""
    tax_invoice_product = TaxInvoiceProduct.query.filter(
        TaxInvoiceProduct.id == tax_invoice_product_id
    ).first()
    db.session.query(PurchaseInvoiceProduct).filter_by(
        id=tax_invoice_product.purchase_invoice_product_id
    ).update(
        {
            "products_left": PurchaseInvoiceProduct.products_left
            + tax_invoice_product.quantity
        }
    )
    TaxInvoiceProduct.query.filter(
        TaxInvoiceProduct.id == tax_invoice_product_id
    ).delete()
    db.session.commit()


def delete_tax_invoice_with_adding_purchase_products_left_fieds(
    tax_invoice_id: int,
) -> None:
    """Delete TaxInvoice with adding purchase products_left fields."""
    tax_invoice_products = TaxInvoiceProduct.query.filter(
        TaxInvoiceProduct.tax_invoice_id == tax_invoice_id
    ).all()
    for product in tax_invoice_products:
        db.session.query(PurchaseInvoiceProduct).filter_by(
            id=product.purchase_invoice_product_id
        ).update(
            {"products_left": (PurchaseInvoiceProduct.products_left + product.quantity)}
        )
        db.session.commit()
    TaxInvoice.query.filter(TaxInvoice.id == tax_invoice_id).delete()
    db.session.commit()
