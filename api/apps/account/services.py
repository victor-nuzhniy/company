"""Db services for account apps."""
from typing import Sequence

from flask import abort
from flask.typing import ResponseReturnValue
from sqlalchemy import and_, func

from api import (
    Product,
    PurchaseInvoice,
    PurchaseInvoiceProduct,
    SaleInvoice,
    SaleInvoiceProduct,
    TaxInvoice,
    TaxInvoiceProduct,
    constants,
    db,
)
from api.apps.product.models import ProductType
from api.services import crud


class AccountQueries(object):
    """Class with account apps queries."""

    def get_purchase_products_by_invoice_products(
        self,
        invoice_products: Sequence,
    ) -> Sequence:
        """Get purchase products list by products ids."""
        products_ids: list[int] = [elem.product_id_valid for elem in invoice_products]
        joinload = db.joinedload(Product.purchase_invoice_products)
        return (
            Product.query.options(joinload)
            .outerjoin(PurchaseInvoiceProduct)
            .filter(
                Product.id.in_(products_ids),
                PurchaseInvoiceProduct.products_left > 0,
            )
            .all()
        )

    def update_sale_invoice(self, sale_invoice_id: int) -> None:
        """Update SaleInvoice 'done' field to True."""
        crud.update(SaleInvoice, {"done": True}, {"id": sale_invoice_id})

    def get_sale_invoice_products_by_period(self, period: dict) -> ResponseReturnValue:
        """Get sold products list by given period."""
        date_from = period.get("date_from")
        date_to = period.get("date_to")
        return (
            SaleInvoiceProduct.query.with_entities(
                SaleInvoiceProduct.id.label("id"),
                SaleInvoiceProduct.quantity.label("quantity"),
                SaleInvoiceProduct.price.label("price"),
                SaleInvoice.name.label("sale_invoice_name"),
                SaleInvoice.created_at.label("created_at"),
                Product.name.label("name"),
                Product.units.label("units"),
                Product.code.label("code"),
                Product.currency.label("currency"),
            )
            .join(SaleInvoice.sale_invoice_products)
            .filter(
                and_(
                    SaleInvoice.created_at > date_from,
                    SaleInvoice.created_at < date_to,
                    SaleInvoice.done,
                ),
            )
            .join(Product)
            .all()
        )

    def get_purchase_products_quantity_list(self, input_data: dict) -> Sequence:
        """Get products list with purchase quantities on given date."""
        date = input_data.get("date")
        return (
            Product.query.with_entities(
                Product.id.label("id"),
                Product.name.label("name"),
                Product.units.label("units"),
                Product.currency.label("currency"),
                func.sum(PurchaseInvoiceProduct.quantity).label("quantity"),
            )
            .join(PurchaseInvoiceProduct)
            .join(PurchaseInvoice)
            .filter(
                PurchaseInvoice.created_at < date,
            )
            .group_by(Product.name)
            .all()
        )

    def get_sold_products(self, input_data: dict) -> Sequence:
        """Get sold product dict on given date."""
        date = input_data.get("date")
        return (
            Product.query.with_entities(
                Product.id.label("id"),
                func.sum(SaleInvoiceProduct.quantity).label("quantity"),
            )
            .join(SaleInvoiceProduct)
            .join(SaleInvoice)
            .filter(
                and_(SaleInvoice.done, SaleInvoice.created_at < date),
            )
            .group_by(Product.id)
            .all()
        )

    def get_tax_invoice_products_with_prices_data(self, period: dict) -> Sequence:
        """Get sold products with purchase and sale prices by given period."""
        date_from = period.get("date_from")
        date_to = period.get("date_to")
        return (
            TaxInvoiceProduct.query.with_entities(
                SaleInvoiceProduct.product_id.label("product_id"),
                TaxInvoiceProduct.quantity.label("quantity"),
                SaleInvoiceProduct.price.label("sale_price"),
                PurchaseInvoiceProduct.price.label("purchase_price"),
            )
            .join(SaleInvoiceProduct)
            .join(PurchaseInvoiceProduct)
            .join(TaxInvoice)
            .filter(
                and_(
                    SaleInvoice.created_at > date_from,
                    SaleInvoice.created_at < date_to,
                ),
            )
            .all()
        )

    def get_sold_products_for_period(self, period: dict) -> Sequence:
        """Get sold products for given period."""
        date_from = period.get("date_from")
        date_to = period.get("date_to")
        query = (
            Product.query.with_entities(
                Product.id.label("id"),
                Product.name.label("name"),
                Product.code.label("code"),
                Product.currency.label("currency"),
                ProductType.name.label("product_type"),
            )
            .join(ProductType)
            .join(SaleInvoiceProduct)
            .join(SaleInvoice)
            .filter(
                and_(
                    SaleInvoice.created_at > date_from,
                    SaleInvoice.created_at < date_to,
                    SaleInvoice.done,
                ),
            )
        )
        return query.group_by(Product.id).all()


account_queries = AccountQueries()


def prepare_tax_invoice_products(  # noqa WPS210
    invoice_products: Sequence,
    purchase_products: Sequence,
    invoice_id: int,
) -> list[dict]:
    """
    Create tax_invoice_products list with products quantity checking.

    In case of lacking products amount in purchase invoices raise error with 409 code.
    """
    purchase_products_dict: dict = {it.id: it for it in purchase_products}
    tax_products: list = []
    for product in invoice_products:
        purchase_products = purchase_products_dict[
            product.product_id_valid
        ].purchase_invoice_products
        quantity: int = product.quantity
        for purchase_product in purchase_products:
            tax_product = {
                "sale_invoice_product_id": product.id,
                "purchase_invoice_product_id": purchase_product.id,
            }
            if quantity > purchase_product.products_left:
                quantity -= purchase_product.products_left
                tax_product["quantity"] = purchase_product.products_left
                tax_products.append(tax_product)
                purchase_product.products_left = 0
            else:
                tax_product["quantity"] = quantity
                purchase_product.products_left -= quantity
                tax_products.append(tax_product)
                quantity = 0
                break
        if quantity > 0:
            abort(
                409,
                "{name} not enough to process invoice with id {id}".format(
                    name=purchase_products_dict[product.product_id_valid].name,
                    id=invoice_id,
                ),
            )
    db.session.commit()
    return tax_products


def create_tax_invoice_products(tax_products: list[dict], sale_invoice_id: int) -> None:
    """Create tax_invoice_products and tax_invoice they are connected."""
    last_tax_invoice = (
        TaxInvoice.query.with_entities(TaxInvoice.id).order_by(-TaxInvoice.id).first()
    )
    tax_invoice_num = str(last_tax_invoice.id + 1) if last_tax_invoice else "1"
    tax_invoice = crud.create(
        TaxInvoice,
        {
            "name": constants.TAX_INVOICE_NAME_PREFIX + tax_invoice_num,
            "sale_invoice_id": sale_invoice_id,
        },
    )
    for product in tax_products:
        product["tax_invoice_id"] = tax_invoice.id
    crud.create_many(TaxInvoiceProduct, tax_products)
