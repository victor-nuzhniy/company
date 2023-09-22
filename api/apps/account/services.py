"""Db services for account apps."""
from typing import Dict, List, Sequence

from flask import abort
from sqlalchemy import CursorResult, and_, select

from api import (
    Product,
    PurchaseInvoiceProduct,
    SaleInvoice,
    SaleInvoiceProduct,
    TaxInvoice,
    TaxInvoiceProduct,
    constants,
    db,
)
from api.services import crud


def get_purchase_products_by_invoice_products(invoice_products: List) -> Sequence:
    """Get purchase products list by products ids."""
    products_ids: List[int] = [elem.product_id for elem in invoice_products]
    statement: str = (
        select(Product, Product.id.in_(products_ids))
        .join(PurchaseInvoiceProduct, Product.id == PurchaseInvoiceProduct.product_id)
        .where(PurchaseInvoiceProduct.products_left > 0)
    )
    result: CursorResult = db.session.execute(statement)
    objects: Sequence = result.scalars().all()
    return objects


def prepare_tax_invoice_products(
    invoice_products: List, purchase_products: Sequence, invoice_id: int
) -> List[Dict]:
    """
    Create tax_invoice_products list with products quantity checking.

    In case of lacking products amount in purchase invoices raise error with 409 code.
    """
    purchase_products_dict: Dict = {item.id: item for item in purchase_products}
    tax_products: List = []
    for product in invoice_products:
        purchase_products: Sequence = purchase_products_dict[
            product.id
        ].purchase_invoice_products
        quantity: int = product.quantity
        for purchase_product in purchase_products:
            tax_product: Dict = dict()
            tax_product["sale_invoice_product_id"] = product.id
            tax_product["purchase_invoice_product_id"] = purchase_product.id
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
                f"{purchase_products_dict[product.product_id].name} not enough"
                f" to process invoice with id {invoice_id}",
            )
    db.session.commit()
    return tax_products


def create_tax_invoice_products(tax_products: List[Dict], invoice_id: int) -> None:
    """Create tax_invoice_products and tax_invoice they are connected."""
    last_tax_invoice = (
        TaxInvoice.query.with_entities(TaxInvoice.id).order_by(-TaxInvoice.id).first()
    )
    tax_invoice = crud.create(
        TaxInvoice,
        {
            "name": constants.TAX_INVOICE_NAME_PREFIX + str(last_tax_invoice.id),
            "invoice_id": invoice_id,
        },
    )
    for product in tax_products:
        product["tax_invoice_id"] = tax_invoice.id
    crud.create_many(TaxInvoiceProduct, tax_products)


def update_sale_invoice(sale_invoice_id: int) -> None:
    """Update SaleInvoice 'done' field to True."""
    crud.update(SaleInvoice, {"done": True}, {"id": sale_invoice_id})


def get_sale_invoice_products_by_period(period: Dict) -> Sequence:
    """Get sold products list by given period."""
    date_from = period.get("date_from")
    date_to = period.get("date_to")
    result = (
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
            )
        )
        .join(Product)
        .all()
    )
    return result
