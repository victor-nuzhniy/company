"""Routes for purchase apps."""
from flask_restful import fields

from api import PurchaseInvoice, PurchaseInvoiceProducts, api
from api.apps.purchase.parsers import (
    purchase_invoice_parser,
    purchase_invoice_patch_parser,
    purchase_invoice_products_parser,
    purchase_invoice_products_patch_parser,
)
from api.model_routes import ModelRoute, ModelsRoute

purchase_invoice_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "agreement_id": fields.Integer,
    "created_at": fields.DateTime,
}

purchase_invoice_products_fields = {
    "id": fields.Integer,
    "product_id": fields.Integer,
    "quantity": fields.Integer,
    "price": fields.Integer,
    "purchase_invoice_id": fields.Integer,
    "products_left": fields.Integer,
}


class PurchaseInvoiceRoute(ModelRoute):
    """Operations with single PurchaseInvoice instance."""

    model = PurchaseInvoice
    put_parser = purchase_invoice_parser
    patch_parser = purchase_invoice_patch_parser
    model_fields = purchase_invoice_fields


class PurchaseInvoicesRoute(ModelsRoute):
    """Operations with many PurchaseInvoice instances and instance creations."""

    model = PurchaseInvoice
    post_parser = purchase_invoice_parser
    model_fields = purchase_invoice_products_fields


class PurchaseInvoiceProductsRoute(ModelRoute):
    """Operations with single PurchaseInvoiceProducts instance."""

    model = PurchaseInvoiceProducts
    put_parser = purchase_invoice_products_parser
    patch_parser = purchase_invoice_products_patch_parser
    model_fields = purchase_invoice_products_fields


class ManyPurchaseInvoiceProductsRoute(ModelsRoute):
    """Operatios with PurchaseInvoiceProducts instances and instance creation."""

    model = PurchaseInvoiceProducts
    post_parser = purchase_invoice_products_parser
    model_fields = purchase_invoice_products_fields


api.add_resource(PurchaseInvoiceRoute, "/purchase-invoice/<instance_id>")
api.add_resource(PurchaseInvoicesRoute, "/purchase-invoice/")
api.add_resource(
    PurchaseInvoiceProductsRoute, "/purchase-invoice-products/<instance_id>"
)
