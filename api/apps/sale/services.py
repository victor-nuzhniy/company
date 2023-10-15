"""DB service functionality for sale apps."""
from datetime import datetime
from typing import Sequence

from sqlalchemy import and_, func, or_

from api import (
    Agreement,
    Counterparty,
    Invoice,
    Product,
    SaleInvoice,
    SaleInvoiceProduct,
    TaxInvoiceProduct,
)


def get_sale_invoice_data(
    offset: int = 0,
    limit: int = 20,
    date_from: datetime = datetime(1000, 1, 1),
    date_to: datetime = datetime(9000, 1, 1),
) -> Sequence:
    """Get SaleInvoice registry list."""
    date_from = datetime(1000, 1, 1) if not date_from else date_from
    date_to = datetime(9000, 1, 1) if not date_to else date_to
    return (
        SaleInvoice.query.with_entities(
            SaleInvoice.id.label("id"),
            SaleInvoice.created_at.label("created_at"),
            SaleInvoice.name.label("name"),
            SaleInvoice.invoice_id.label("invoice_id"),
            SaleInvoice.done.label("done"),
            Invoice.name.label("invoice"),
            Agreement.id.label("agreement_id"),
            Agreement.name.label("agreement"),
            Counterparty.id.label("counterparty_id"),
            Counterparty.name.label("counterparty"),
            func.sum((SaleInvoiceProduct.quantity * SaleInvoiceProduct.price)).label(
                "summ"
            ),
            Product.currency.label("currency"),
        )
        .outerjoin(SaleInvoice.sale_invoice_products)
        .outerjoin(Invoice)
        .outerjoin(Agreement)
        .outerjoin(Counterparty)
        .outerjoin(Product)
        .filter(
            and_(SaleInvoice.created_at > date_from, SaleInvoice.created_at < date_to)
        )
        .group_by(SaleInvoice)
        .order_by(SaleInvoice.id.desc())
        .limit(limit)
        .offset(offset)
        .all()
    )


def get_sale_invoice_products_by_sale_invoice_id(sale_invoice_id: int) -> Sequence:
    """Get SaleInvoice products list by sale invoice id."""
    return (
        SaleInvoiceProduct.query.with_entities(
            SaleInvoiceProduct.id.label("id"),
            SaleInvoiceProduct.product_id.label("product_id"),
            SaleInvoiceProduct.quantity.label("quantity"),
            SaleInvoiceProduct.price.label("price"),
            SaleInvoiceProduct.sale_invoice_id.label("sale_invoice_id"),
            Product.name.label("name"),
            Product.code.label("code"),
            Product.currency.label("currency"),
            Product.units.label("units"),
        )
        .join(Product)
        .filter(SaleInvoiceProduct.sale_invoice_id == sale_invoice_id)
        .all()
    )


def get_tax_sale_invoice_products_left(
    sale_invoice_id: int, tax_invoice_id: int
) -> Sequence:
    """
    Get SaleInvoice products list by sale invoice id.

    Products, included in tax invoice, will not be included in query.
    There are not products will be available from sale invoice with done True.
    """
    return (
        SaleInvoiceProduct.query.with_entities(
            SaleInvoiceProduct.id.label("id"),
            SaleInvoiceProduct.product_id.label("product_id"),
            SaleInvoiceProduct.quantity.label("quantity"),
            SaleInvoiceProduct.price.label("price"),
            SaleInvoiceProduct.sale_invoice_id.label("sale_invoice_id"),
            func.sum(
                SaleInvoiceProduct.quantity
                - TaxInvoiceProduct.query.with_entities(
                    func.sum(TaxInvoiceProduct.quantity).label(
                        "tax_invoice_product_sum"
                    )
                )
                .filter(
                    TaxInvoiceProduct.sale_invoice_product_id == SaleInvoiceProduct.id
                )
                .first()
                .tax_invoice_product_sum
            ).label("sale_products_left"),
            Product.name.label("name"),
            Product.code.label("code"),
            Product.currency.label("currency"),
            Product.units.label("units"),
        )
        .join(Product)
        .filter(SaleInvoiceProduct.sale_invoice_id == sale_invoice_id)
        .filter(
            or_(
                SaleInvoiceProduct.id.not_in(
                    TaxInvoiceProduct.query.with_entities(
                        TaxInvoiceProduct.sale_invoice_product_id
                    ).filter(TaxInvoiceProduct.tax_invoice_id == tax_invoice_id)
                ),
                and_(
                    SaleInvoiceProduct.id.in_(
                        TaxInvoiceProduct.query.with_entities(
                            TaxInvoiceProduct.sale_invoice_product_id
                        ).filter(TaxInvoiceProduct.tax_invoice_id == tax_invoice_id)
                    ),
                    SaleInvoiceProduct.quantity
                    > TaxInvoiceProduct.query.with_entities(
                        func.sum(TaxInvoiceProduct.quantity).label(
                            "tax_invoice_product_sum"
                        )
                    ).filter(
                        TaxInvoiceProduct.sale_invoice_product_id
                        == SaleInvoiceProduct.id
                    ),
                ),
            ),
        )
        .all()
    )


def get_sale_invoices_by_agreement_id(agreement_id: int) -> Sequence:
    """Get SaleInvoice list by agreement_id."""
    return (
        SaleInvoice.query.outerjoin(Invoice)
        .filter(Invoice.agreement_id == agreement_id)
        .all()
    )
