"""Routes for sale apps."""
from flask_restful import fields

from api import SaleInvoice, SaleInvoiceProduct, api
from api.apps.sale.parsers import (
    sale_invoice_parser,
    sale_invoice_patch_parser,
    sale_invoice_product_parser,
    sale_invoice_product_patch_parser,
)
from api.model_routes import ModelRoute, ModelsRoute

sale_invoice_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "invoice_id": fields.Integer,
    "created_at": fields.DateTime,
    "done": fields.Boolean,
}

sale_invoice_product_fields = {
    "id": fields.Integer,
    "product_id": fields.Integer,
    "quantity": fields.Integer,
    "price": fields.Integer,
    "sale_invoice_id": fields.Integer,
}


class SaleInvoiceRoute(ModelRoute):
    """Operations with single SaleInvoice instance."""

    model = SaleInvoice
    put_parser = sale_invoice_parser
    patch_parser = sale_invoice_patch_parser
    model_fields = sale_invoice_fields


class SaleInvoicesRoute(ModelsRoute):
    """Operations with many SaleInvoice instances and instance creation."""

    model = SaleInvoice
    post_parser = sale_invoice_parser
    model_fields = sale_invoice_fields


class SaleInvoiceProductRoute(ModelRoute):
    """Operations with single SaleInvoiceProduct instance."""

    model = SaleInvoiceProduct
    put_parser = sale_invoice_product_parser
    patch_parser = sale_invoice_product_patch_parser
    model_fields = sale_invoice_product_fields


class SaleInvoiceProductsRoute(ModelsRoute):
    """Operations with many SaleInvoiceProduct instance and instance creation."""

    model = SaleInvoiceProduct
    post_parser = sale_invoice_product_parser
    model_fields = sale_invoice_product_fields


api.add_resource(SaleInvoiceRoute, "/sale-invoice/<instance_id>")
api.add_resource(SaleInvoicesRoute, "/sale-invoice/")
api.add_resource(SaleInvoiceProductRoute, "/sale-invoice-product/<instance_id>")
api.add_resource(SaleInvoiceProductsRoute, "/sale-invoice-product/")
