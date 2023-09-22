"""Routes for tax apps."""
from flask_restful import fields

from api import TaxInvoice, TaxInvoiceProduct, api
from api.apps.tax.parsers import (
    tax_invoice_parser,
    tax_invoice_patch_parser,
    tax_invoice_product_parser,
    tax_invoice_product_patch_parser,
)
from api.model_routes import ModelRoute, ModelsRoute

tax_invoice_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "sale_invoice_id": fields.Integer,
    "created_at": fields.DateTime,
}

tax_invoice_product_fields = {
    "id": fields.Integer,
    "tax_invoice_id": fields.Integer,
    "sale_invoice_products_id": fields.Integer,
    "purchase_invoice_products_id": fields.Integer,
    "quantity": fields.Integer,
}


class TaxInvoiceRoute(ModelRoute):
    """Operations with single TaxInvoice instance."""

    model = TaxInvoice
    put_parser = tax_invoice_parser
    patch_parser = tax_invoice_patch_parser
    model_fields = tax_invoice_fields


class TaxInvoicesRoute(ModelsRoute):
    """Operations with TaxInvoice instances and instance creation."""

    model = TaxInvoice
    post_parser = tax_invoice_parser
    model_fields = tax_invoice_fields


class TaxInvoiceProductRoute(ModelRoute):
    """Operations with single TaxInvoiceProducts instance."""

    model = TaxInvoiceProduct
    put_parser = tax_invoice_product_parser
    patch_parser = tax_invoice_product_patch_parser
    model_fields = tax_invoice_product_fields


class TaxInvoiceProductsRoute(ModelsRoute):
    """Operations with TaxInvoiceProducts instances and instance creation."""

    model = TaxInvoiceProduct
    post_parser = tax_invoice_product_parser
    model_fields = tax_invoice_product_fields


api.add_resource(TaxInvoiceRoute, "/tax-invoice/<instance_id>")
api.add_resource(TaxInvoicesRoute, "/tax-invoice/")
api.add_resource(TaxInvoiceProductRoute, "/tax-invoice-product/<instance_id>")
api.add_resource(TaxInvoiceProductsRoute, "/tax-invoice-product/")
