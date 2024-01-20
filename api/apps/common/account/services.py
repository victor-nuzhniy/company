"""Db services for account apps."""
from typing import Sequence

from flask import abort
from flask.typing import ResponseReturnValue
from sqlalchemy import and_, func

from api import db
from api.apps.product.base import models as product_models
from api.apps.purchase.base import models as purchase_models
from api.apps.sale.base import models as sale_models
from api.apps.tax.base import models as tax_models
from api.common import constants
from api.common.services import crud


class AccountQueries(object):
    """Class with account apps queries."""

    def get_purchase_products_by_invoice_products(
        self,
        invoice_products: Sequence,
    ) -> Sequence:
        """Get base products list by products ids."""
        products_ids: list[int] = [elem.product_id for elem in invoice_products]
        joinload = db.joinedload(product_models.Product.purchase_invoice_products)
        return (
            product_models.Product.query.options(joinload)
            .outerjoin(purchase_models.PurchaseInvoiceProduct)
            .filter(
                product_models.Product.id.in_(products_ids),
                purchase_models.PurchaseInvoiceProduct.products_left > 0,
            )
            .all()
        )

    def update_sale_invoice(self, sale_invoice_id: int) -> None:
        """Update SaleInvoice 'done' field to True."""
        crud.update(sale_models.SaleInvoice, {"done": True}, {"id": sale_invoice_id})

    def get_sale_invoice_products_by_period(self, period: dict) -> ResponseReturnValue:
        """Get sold products list by given period."""
        date_from = period.get("date_from")
        date_to = period.get("date_to")
        return (
            sale_models.SaleInvoiceProduct.query.with_entities(
                sale_models.SaleInvoiceProduct.id.label("id"),
                sale_models.SaleInvoiceProduct.quantity.label("quantity"),
                sale_models.SaleInvoiceProduct.price.label("price"),
                sale_models.SaleInvoice.name.label("sale_invoice_name"),
                sale_models.SaleInvoice.created_at.label("created_at"),
                product_models.Product.name.label("name"),
                product_models.Product.units.label("units"),
                product_models.Product.code.label("code"),
                product_models.Product.currency.label("currency"),
            )
            .join(sale_models.SaleInvoice.sale_invoice_products)
            .filter(
                and_(
                    sale_models.SaleInvoice.created_at > date_from,
                    sale_models.SaleInvoice.created_at < date_to,
                    sale_models.SaleInvoice.done,
                ),
            )
            .join(product_models.Product)
            .all()
        )

    def get_purchase_products_quantity_list(self, input_data: dict) -> Sequence:
        """Get products list with base quantities on given date."""
        date = input_data.get("date")
        query = product_models.Product.query.with_entities(
            product_models.Product.id.label("id"),
            product_models.Product.name.label("name"),
            product_models.Product.units.label("units"),
            product_models.Product.currency.label("currency"),
            func.sum(purchase_models.PurchaseInvoiceProduct.quantity).label(
                "quantity",
            ),
        )
        return (
            query.join(purchase_models.PurchaseInvoiceProduct)
            .join(purchase_models.PurchaseInvoice)
            .filter(
                purchase_models.PurchaseInvoice.created_at < date,
            )
            .group_by(product_models.Product.name)
            .all()
        )

    def get_sold_products(self, input_data: dict) -> Sequence:
        """Get sold base dict on given date."""
        date = input_data.get("date")
        query = product_models.Product.query.with_entities(
            product_models.Product.id.label("id"),
            func.sum(sale_models.SaleInvoiceProduct.quantity).label("quantity"),
        )
        return (
            query.join(sale_models.SaleInvoiceProduct)
            .join(sale_models.SaleInvoice)
            .filter(
                and_(
                    sale_models.SaleInvoice.done,
                    sale_models.SaleInvoice.created_at < date,
                ),
            )
            .group_by(product_models.Product.id)
            .all()
        )

    def get_tax_invoice_products_with_prices_data(self, period: dict) -> Sequence:
        """Get sold products with base and base prices by given period."""
        date_from = period.get("date_from")
        date_to = period.get("date_to")
        query = tax_models.TaxInvoiceProduct.query.with_entities(
            sale_models.SaleInvoiceProduct.product_id.label("product_id"),
            tax_models.TaxInvoiceProduct.quantity.label("quantity"),
            sale_models.SaleInvoiceProduct.price.label("sale_price"),
            purchase_models.PurchaseInvoiceProduct.price.label("purchase_price"),
        )
        return (
            query.join(sale_models.SaleInvoiceProduct)
            .join(purchase_models.PurchaseInvoiceProduct)
            .join(tax_models.TaxInvoice)
            .filter(
                and_(
                    sale_models.SaleInvoice.created_at > date_from,
                    sale_models.SaleInvoice.created_at < date_to,
                ),
            )
            .all()
        )

    def get_sold_products_for_period(self, period: dict) -> Sequence:
        """Get sold products for given period."""
        date_from = period.get("date_from")
        date_to = period.get("date_to")
        query = (
            product_models.Product.query.with_entities(
                product_models.Product.id.label("id"),
                product_models.Product.name.label("name"),
                product_models.Product.code.label("code"),
                product_models.Product.currency.label("currency"),
                product_models.ProductType.name.label("product_type"),
            )
            .join(product_models.ProductType)
            .join(sale_models.SaleInvoiceProduct)
            .join(sale_models.SaleInvoice)
            .filter(
                and_(
                    sale_models.SaleInvoice.created_at > date_from,
                    sale_models.SaleInvoice.created_at < date_to,
                    sale_models.SaleInvoice.done,
                ),
            )
        )
        return query.group_by(product_models.Product.id).all()


account_queries = AccountQueries()


def prepare_tax_invoice_products(  # noqa WPS210
    invoice_products: Sequence,
    purchase_products: Sequence,
    invoice_id: int,
) -> list[dict]:
    """
    Create tax_invoice_products list with products quantity checking.

    In case of lacking products amount in base invoices raise error with 409 code.
    """
    purchase_products_dict: dict = {it.id: it for it in purchase_products}
    tax_products: list = []
    for product in invoice_products:
        purchase_products = purchase_products_dict[
            product.product_id
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
                "{name} not enough to process base with id {id}".format(
                    name=purchase_products_dict[product.product_id].name,
                    id=invoice_id,
                ),
            )
    db.session.commit()
    return tax_products


def create_tax_invoice_products(tax_products: list[dict], sale_invoice_id: int) -> None:
    """Create tax_invoice_products and tax_invoice they are connected."""
    last_tax_invoice = (
        tax_models.TaxInvoice.query.with_entities(tax_models.TaxInvoice.id)
        .order_by(-tax_models.TaxInvoice.id)
        .first()
    )
    tax_invoice_num = str(last_tax_invoice.id + 1) if last_tax_invoice else "1"
    tax_invoice = crud.create(
        tax_models.TaxInvoice,
        {
            "name": constants.TAX_INVOICE_NAME_PREFIX + tax_invoice_num,
            "sale_invoice_id": sale_invoice_id,
        },
    )
    for product in tax_products:
        product["tax_invoice_id"] = tax_invoice.id
    crud.create_many(tax_models.TaxInvoiceProduct, tax_products)
