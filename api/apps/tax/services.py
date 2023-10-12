"""DB service functionality for tax apps."""
from datetime import datetime
from typing import Sequence

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
        db.session.query(
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
        .select_from(
            SaleInvoice,
            Invoice,
            Agreement,
            Counterparty,
            TaxInvoiceProduct,
            SaleInvoiceProduct,
            PurchaseInvoiceProduct,
            PurchaseInvoice,
        )
        .outerjoin(SaleInvoice.tax_invoices)
        .filter(
            SaleInvoice.id == TaxInvoice.sale_invoice_id,
            Invoice.id == SaleInvoice.invoice_id,
            Agreement.id == Invoice.agreement_id,
            Counterparty.id == Agreement.counterparty_id,
            TaxInvoice.id == TaxInvoiceProduct.tax_invoice_id,
            TaxInvoiceProduct.purchase_invoice_product_id == PurchaseInvoiceProduct.id,
            PurchaseInvoice.id == PurchaseInvoiceProduct.purchase_invoice_id,
            SaleInvoiceProduct.id == TaxInvoiceProduct.sale_invoice_product_id,
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
