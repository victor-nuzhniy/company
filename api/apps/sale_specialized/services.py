"""DB service functionality for sale_specialized apps."""
from datetime import datetime
from typing import Sequence

from sqlalchemy import and_, func, or_

from api.apps.counterparty import models as counterparty_models
from api.apps.invoice import models as invoice_models
from api.apps.product import models as product_models
from api.apps.sale import models as sale_models
from api.apps.tax import models as tax_models
from api.constants import EARLIEST_DATE, LATEST_DATE


def get_sale_invoice_data(
    offset: int = 0,
    limit: int = 20,
    date_from: datetime = EARLIEST_DATE,
    date_to: datetime = LATEST_DATE,
) -> Sequence:
    """Get SaleInvoice registry list."""
    date_from = date_from if date_from else EARLIEST_DATE
    date_to = date_to if date_to else LATEST_DATE
    query = sale_models.SaleInvoice.query.with_entities(
        sale_models.SaleInvoice.id.label("id"),
        sale_models.SaleInvoice.created_at.label("created_at"),
        sale_models.SaleInvoice.name.label("name"),
        sale_models.SaleInvoice.invoice_id.label("invoice_id"),
        sale_models.SaleInvoice.done.label("done"),
        invoice_models.Invoice.name.label("invoice"),
        counterparty_models.Agreement.id.label("agreement_id"),
        counterparty_models.Agreement.name.label("agreement"),
        counterparty_models.Counterparty.id.label("counterparty_id"),
        counterparty_models.Counterparty.name.label("counterparty"),
        func.sum(
            (
                sale_models.SaleInvoiceProduct.quantity
                * sale_models.SaleInvoiceProduct.price
            ),
        ).label(
            "summ",
        ),
        product_models.Product.currency.label("currency"),
    )
    additional_query = (
        query.outerjoin(sale_models.SaleInvoice.sale_invoice_products)
        .outerjoin(invoice_models.Invoice)
        .outerjoin(counterparty_models.Agreement)
        .outerjoin(counterparty_models.Counterparty)
        .outerjoin(product_models.Product)
    )
    return (
        additional_query.filter(
            and_(
                sale_models.SaleInvoice.created_at > date_from,
                sale_models.SaleInvoice.created_at < date_to,
            ),
        )
        .group_by(sale_models.SaleInvoice)
        .order_by(sale_models.SaleInvoice.id.desc())
        .limit(limit)
        .offset(offset)
        .all()
    )


def get_sale_invoice_products_by_sale_invoice_id(sale_invoice_id: int) -> Sequence:
    """Get SaleInvoice products list by sale invoice id."""
    return (
        sale_models.SaleInvoiceProduct.query.with_entities(
            sale_models.SaleInvoiceProduct.id.label("id"),
            sale_models.SaleInvoiceProduct.product_id.label("product_id"),
            sale_models.SaleInvoiceProduct.quantity.label("quantity"),
            sale_models.SaleInvoiceProduct.price.label("price"),
            sale_models.SaleInvoiceProduct.sale_invoice_id.label("sale_invoice_id"),
            product_models.Product.name.label("name"),
            product_models.Product.code.label("code"),
            product_models.Product.currency.label("currency"),
            product_models.Product.units.label("units"),
        )
        .join(product_models.Product)
        .filter(sale_models.SaleInvoiceProduct.sale_invoice_id == sale_invoice_id)
        .all()
    )


def get_tax_sale_invoice_products_left(
    sale_invoice_id: int,
    tax_invoice_id: int,
) -> Sequence:
    """
    Get SaleInvoice products list by sale invoice id.

    Products, included in tax invoice, will not be included in query.
    There are not products will be available from sale invoice with done True.
    """
    return (
        sale_models.SaleInvoiceProduct.query.with_entities(
            sale_models.SaleInvoiceProduct.id.label("id"),
            sale_models.SaleInvoiceProduct.product_id.label("product_id"),
            sale_models.SaleInvoiceProduct.quantity.label("quantity"),
            sale_models.SaleInvoiceProduct.price.label("price"),
            sale_models.SaleInvoiceProduct.sale_invoice_id.label("sale_invoice_id"),
            func.sum(
                sale_models.SaleInvoiceProduct.quantity
                - tax_models.TaxInvoiceProduct.query.with_entities(
                    func.sum(tax_models.TaxInvoiceProduct.quantity).label(
                        "tax_invoice_product_sum",
                    ),
                )
                .filter(
                    tax_models.TaxInvoiceProduct.sale_invoice_product_id
                    == sale_models.SaleInvoiceProduct.id,
                )
                .first()
                .tax_invoice_product_sum,
            ).label("sale_products_left"),
            product_models.Product.name.label("name"),
            product_models.Product.code.label("code"),
            product_models.Product.currency.label("currency"),
            product_models.Product.units.label("units"),
        )
        .join(product_models.Product)
        .filter(sale_models.SaleInvoiceProduct.sale_invoice_id == sale_invoice_id)
        .filter(
            or_(
                sale_models.SaleInvoiceProduct.id.not_in(
                    tax_models.TaxInvoiceProduct.query.with_entities(
                        tax_models.TaxInvoiceProduct.sale_invoice_product_id,
                    ).filter(
                        tax_models.TaxInvoiceProduct.tax_invoice_id == tax_invoice_id,
                    ),
                ),
                and_(
                    sale_models.SaleInvoiceProduct.id.in_(
                        tax_models.TaxInvoiceProduct.query.with_entities(
                            tax_models.TaxInvoiceProduct.sale_invoice_product_id,
                        ).filter(
                            tax_models.TaxInvoiceProduct.tax_invoice_id
                            == tax_invoice_id,
                        ),
                    ),
                    sale_models.SaleInvoiceProduct.quantity
                    > tax_models.TaxInvoiceProduct.query.with_entities(
                        func.sum(tax_models.TaxInvoiceProduct.quantity).label(
                            "tax_invoice_product_sum",
                        ),
                    ).filter(
                        tax_models.TaxInvoiceProduct.sale_invoice_product_id
                        == sale_models.SaleInvoiceProduct.id,
                    ),
                ),
            ),
        )
        .all()
    )


def get_sale_invoices_by_agreement_id(agreement_id: int) -> Sequence:
    """Get SaleInvoice list by agreement_id."""
    return (
        sale_models.SaleInvoice.query.outerjoin(invoice_models.Invoice)
        .filter(invoice_models.Invoice.agreement_id == agreement_id)
        .all()
    )
