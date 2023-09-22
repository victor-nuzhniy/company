"""Routes for purchase apps."""
from flask_restful import fields

from api import PurchaseInvoice, PurchaseInvoiceProduct, api
from api.apps.purchase.parsers import (
    purchase_invoice_parser,
    purchase_invoice_patch_parser,
    purchase_invoice_product_parser,
    purchase_invoice_product_patch_parser,
)
from api.model_routes import ModelRoute, ModelsRoute

purchase_invoice_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "agreement_id": fields.Integer,
    "created_at": fields.DateTime,
}

purchase_invoice_product_fields = {
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
    model_fields = purchase_invoice_fields


class PurchaseInvoiceProductRoute(ModelRoute):
    """Operations with single PurchaseInvoiceProducts instance."""

    model = PurchaseInvoiceProduct
    put_parser = purchase_invoice_product_parser
    patch_parser = purchase_invoice_product_patch_parser
    model_fields = purchase_invoice_product_fields


class PurchaseInvoiceProductsRoute(ModelsRoute):
    """Operatios with PurchaseInvoiceProducts instances and instance creation."""

    model = PurchaseInvoiceProduct
    post_parser = purchase_invoice_product_parser
    model_fields = purchase_invoice_product_fields


api.add_resource(PurchaseInvoiceRoute, "/purchase-invoice/<instance_id>")
api.add_resource(PurchaseInvoicesRoute, "/purchase-invoice/")
api.add_resource(PurchaseInvoiceProductRoute, "/purchase-invoice-product/<instance_id>")
api.add_resource(PurchaseInvoiceProductsRoute, "/purchase-invoice-product/")
