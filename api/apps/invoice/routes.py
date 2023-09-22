"""Invoice routes."""
from flask_restful import fields

from api import Invoice, InvoiceProduct, api
from api.apps.invoice.parsers import (
    invoice_parser,
    invoice_patch_parser,
    invoice_product_parser,
    invoice_product_patch_parser,
)
from api.model_routes import ModelRoute, ModelsRoute

invoice_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "order_id": fields.Integer,
    "created_at": fields.DateTime,
    "paid": fields.Boolean,
    "agreement_id": fields.Integer,
}

invoice_product_fields = {
    "id": fields.Integer,
    "product_id": fields.Integer,
    "quantity": fields.Integer,
    "price": fields.Integer,
    "invoice_id": fields.Integer,
}


class InvoiceRoute(ModelRoute):
    """Operations with single Invoice instance."""

    model = Invoice
    put_parser = invoice_parser
    patch_parser = invoice_patch_parser
    model_fields = invoice_fields


class InvoicesRoute(ModelsRoute):
    """Operations with many Invoice isntances and instance creation."""

    model = Invoice
    post_parser = invoice_parser
    model_fields = invoice_fields


class InvoiceProductRoute(ModelRoute):
    """Operations with single InvoiceProducts instance."""

    model = InvoiceProduct
    put_parser = invoice_product_parser
    patch_parser = invoice_product_patch_parser
    model_fields = invoice_product_fields


class InvoiceProductsRoute(ModelsRoute):
    """Operations with many InvoiceProducts instances and instance creation."""

    model = InvoiceProduct
    post_parser = invoice_product_parser
    model_fields = invoice_product_fields


api.add_resource(InvoiceRoute, "/invoice/<instance_id>")
api.add_resource(InvoicesRoute, "/invoice/")
api.add_resource(InvoiceProductRoute, "/invoice-products/<instance_id>")
api.add_resource(InvoiceProductsRoute, "/invoice-products/")
