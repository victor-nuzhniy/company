"""Invoice routes."""
from flask_restful import fields

from api import Invoice, api
from api.apps.invoice.parsers import invoice_parser, invoice_patch_parser
from api.model_routes import ModelRoute, ModelsRoute

invoice_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "order_id": fields.Integer,
    "created_at": fields.DateTime,
    "paid": fields.Boolean,
    "agreement_id": fields.Integer,
}

invoice_products_fields = {
    "id": fields.Integer,
    "product_id": fields.Integer,
    "quantity": fields.Integer,
    "price": fields.Integer,
    "invoice_id": fields.Integer,
}

sale_invoice_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "invoice_id": fields.Integer,
    "created_at": fields.DateTime,
    "done": fields.Boolean,
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


api.add_resource(InvoiceRoute, "/invoice/<instance_id>")
api.add_resource(InvoicesRoute, "/invoice/")
