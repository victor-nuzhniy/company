"""Routes for tax apps."""
from flask_restful import fields

from api import TaxInvoice, TaxInvoiceProducts, api
from api.apps.tax.parsers import (
    tax_invoice_parser,
    tax_invoice_patch_parser,
    tax_invoice_products_parser,
    tax_invoice_products_patch_parser,
)
from api.model_routes import ModelRoute, ModelsRoute

tax_invoice_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "invoice_id": fields.Integer,
    "created_at": fields.DateTime,
}

tax_invoice_products_fields = {
    "id": fields.Integer,
    "tax_invoice_id": fields.Integer,
    "invoice_products_id": fields.Integer,
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


class TaxInvoiceProductsRoute(ModelRoute):
    """Operations with single TaxInvoiceProducts instance."""

    model = TaxInvoiceProducts
    put_parser = tax_invoice_products_parser
    patch_parser = tax_invoice_products_patch_parser
    model_fields = tax_invoice_products_fields


class ManyTaxInvoiceProductsRoute(ModelsRoute):
    """Operations with TaxInvoiceProducts instances and instance creation."""

    model = TaxInvoiceProducts
    post_parser = tax_invoice_products_parser
    model_fields = tax_invoice_products_fields


api.add_resource(TaxInvoiceRoute, "/tax-invoice/<instance_id>")
api.add_resource(TaxInvoicesRoute, "/tax-invoice/")
api.add_resource(TaxInvoiceProductsRoute, "/tax-invoice-products/<instance_id>")
api.add_resource(ManyTaxInvoiceProductsRoute, "/tax-invoice-products/")
