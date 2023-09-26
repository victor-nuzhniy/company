"""Routes for tax apps."""
from flask_restful import fields
from flask_restful_swagger import swagger

from api import TaxInvoice, TaxInvoiceProduct, api
from api.apps.tax.parsers import (
    tax_invoice_parser,
    tax_invoice_patch_parser,
    tax_invoice_product_parser,
    tax_invoice_product_patch_parser,
)
from api.model_routes import ModelRoute, ModelsRoute


@swagger.model
class TaxInvoiceFields:
    """TaxInvoiceRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "name": fields.String,
        "sale_invoice_id": fields.Integer,
        "created_at": fields.DateTime,
    }


@swagger.model
class TaxInvoiceProductFields:
    """TaxInvoiceProductRoute output fields."""

    resource_fields = {
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
    model_fields = TaxInvoiceFields.resource_fields

    @swagger.operation()
    def get(self, *args, **kwargs):
        """Get model instance by id."""
        return super().get(*args, **kwargs)

    @swagger.operation()
    def put(self, *args, **kwargs):
        """Update instance by id."""
        return super().put(*args, **kwargs)

    @swagger.operation()
    def patch(self, *args, **kwargs):
        """Update instance bu id, partially."""
        return super().patch(*args, **kwargs)

    @swagger.operation()
    def delete(self, *args, **kwargs):
        """Delete instance by id."""
        return super().delete(*args, **kwargs)


class TaxInvoicesRoute(ModelsRoute):
    """Operations with TaxInvoice instances and instance creation."""

    model = TaxInvoice
    post_parser = tax_invoice_parser
    model_fields = TaxInvoiceFields.resource_fields

    @swagger.operation()
    def post(self, *args, **kwargs):
        """Create model instance."""
        return super().post(*args, **kwargs)

    @swagger.operation()
    def get(self, *args, **kwargs):
        """Get model instance list."""
        return super().get(*args, **kwargs)


class TaxInvoiceProductRoute(ModelRoute):
    """Operations with single TaxInvoiceProducts instance."""

    model = TaxInvoiceProduct
    put_parser = tax_invoice_product_parser
    patch_parser = tax_invoice_product_patch_parser
    model_fields = TaxInvoiceProductFields.resource_fields

    @swagger.operation()
    def get(self, *args, **kwargs):
        """Get model instance by id."""
        return super().get(*args, **kwargs)

    @swagger.operation()
    def put(self, *args, **kwargs):
        """Update instance by id."""
        return super().put(*args, **kwargs)

    @swagger.operation()
    def patch(self, *args, **kwargs):
        """Update instance bu id, partially."""
        return super().patch(*args, **kwargs)

    @swagger.operation()
    def delete(self, *args, **kwargs):
        """Delete instance by id."""
        return super().delete(*args, **kwargs)


class TaxInvoiceProductsRoute(ModelsRoute):
    """Operations with TaxInvoiceProducts instances and instance creation."""

    model = TaxInvoiceProduct
    post_parser = tax_invoice_product_parser
    model_fields = TaxInvoiceProductFields.resource_fields

    @swagger.operation()
    def post(self, *args, **kwargs):
        """Create model instance."""
        return super().post(*args, **kwargs)

    @swagger.operation()
    def get(self, *args, **kwargs):
        """Get model instance list."""
        return super().get(*args, **kwargs)


api.add_resource(TaxInvoiceRoute, "/tax-invoice/<instance_id>")
api.add_resource(TaxInvoicesRoute, "/tax-invoice/")
api.add_resource(TaxInvoiceProductRoute, "/tax-invoice-product/<instance_id>")
api.add_resource(TaxInvoiceProductsRoute, "/tax-invoice-product/")
