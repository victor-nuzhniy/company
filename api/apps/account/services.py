"""Db services for account apps."""
from typing import Dict, List

from flask import abort
from sqlalchemy import select

from api import Product, PurchaseInvoiceProducts, TaxInvoice, TaxInvoiceProducts, db
from api.services import crud


def get_purchase_products_by_invoice_products(invoice_products: List) -> List:
    """Get purchase products list by products ids."""
    products_ids = [elem.product_id for elem in invoice_products]
    statement = (
        select(Product, Product.id.in_(products_ids))
        .join(PurchaseInvoiceProducts, Product.id == PurchaseInvoiceProducts.product_id)
        .where(PurchaseInvoiceProducts.products_left > 0)
    )
    result = db.session.execute(statement)
    objects = result.scalars().all()
    return objects


def prepare_tax_invoice_products(
    invoice_products: List, purchase_products: List, invoice_id: int
) -> List[Dict]:
    """Create tax_invoice_products list with products quantity checking."""
    purchase_products_dict = {item.id: item for item in purchase_products}
    tax_products = []
    for product in invoice_products:
        purchase_products = purchase_products_dict[product.id].purchase_invoice_products
        quantity = product.quantity
        for purchase_product in purchase_products:
            tax_product = dict()
            tax_product["invoice_products_id"] = product.id
            tax_product["purchase_invoice_products_id"] = purchase_product.id
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
    """Create tax_invoice_products and tax_invoice they connected."""
    tax_invoice = crud.create(
        TaxInvoice, {"name": "Tax-0001", "invoice_id": invoice_id}
    )
    for product in tax_products:
        product["tax_invoice_id"] = tax_invoice.id
    crud.create_many(TaxInvoiceProducts, tax_products)
