"""Invoice routes."""
from flask_restful import fields
from flask_restful_swagger import swagger

from api import Invoice, InvoiceProduct, api
from api.apps.invoice.parsers import (
    invoice_patch_parser,
    invoice_post_parser,
    invoice_product_parser,
    invoice_product_patch_parser,
    invoice_put_parser,
)
from api.apps.invoice.schemas import (
    invoice_delete_schema,
    invoice_get_schema,
    invoice_patch_schema,
    invoice_post_schema,
    invoice_product_delete_schema,
    invoice_product_get_schema,
    invoice_product_patch_schema,
    invoice_product_post_schema,
    invoice_product_put_schema,
    invoice_products_get_schema,
    invoice_put_schema,
    invoices_get_schema,
)
from api.common import CustomDateTimeFormat
from api.model_routes import ModelRoute, ModelsRoute, token_required


@swagger.model
class InvoiceFields:
    """InvoiceRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "name": fields.String,
        "order_id": fields.Integer,
        "created_at": CustomDateTimeFormat,
        "paid": fields.Boolean,
        "agreement_id": fields.Integer,
    }


@swagger.model
class InvoiceProductFields:
    """InvoiceProductRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "product_id": fields.Integer,
        "quantity": fields.Integer,
        "price": fields.Integer,
        "invoice_id": fields.Integer,
    }


class InvoiceRoute(ModelRoute):
    """Operations with single Invoice instance."""

    model = Invoice
    put_parser = invoice_put_parser
    patch_parser = invoice_patch_parser
    model_fields = InvoiceFields.resource_fields

    @swagger.operation(**invoice_get_schema)
    @token_required()
    def get(self, *args, **kwargs):
        """Get model instance by id."""
        return super().get(*args, **kwargs)

    @swagger.operation(**invoice_put_schema)
    @token_required()
    def put(self, *args, **kwargs):
        """Update instance by id."""
        return super().put(*args, **kwargs)

    @swagger.operation(**invoice_patch_schema)
    @token_required()
    def patch(self, *args, **kwargs):
        """Update instance bu id, partially."""
        return super().patch(*args, **kwargs)

    @swagger.operation(**invoice_delete_schema)
    @token_required()
    def delete(self, *args, **kwargs):
        """Delete instance by id."""
        return super().delete(*args, **kwargs)


class InvoicesRoute(ModelsRoute):
    """Operations with many Invoice isntances and instance creation."""

    model = Invoice
    post_parser = invoice_post_parser
    model_fields = InvoiceFields.resource_fields

    @swagger.operation(**invoice_post_schema)
    @token_required()
    def post(self, *args, **kwargs):
        """Create model instance."""
        return super().post(*args, **kwargs)

    @swagger.operation(**invoices_get_schema)
    @token_required()
    def get(self, *args, **kwargs):
        """Get model instance list."""
        return super().get(*args, **kwargs)


class InvoiceProductRoute(ModelRoute):
    """Operations with single InvoiceProducts instance."""

    model = InvoiceProduct
    put_parser = invoice_product_parser
    patch_parser = invoice_product_patch_parser
    model_fields = InvoiceProductFields.resource_fields

    @swagger.operation(**invoice_product_get_schema)
    @token_required()
    def get(self, *args, **kwargs):
        """Get model instance by id."""
        return super().get(*args, **kwargs)

    @swagger.operation(**invoice_product_put_schema)
    @token_required()
    def put(self, *args, **kwargs):
        """Update instance by id."""
        return super().put(*args, **kwargs)

    @swagger.operation(**invoice_product_patch_schema)
    @token_required()
    def patch(self, *args, **kwargs):
        """Update instance bu id, partially."""
        return super().patch(*args, **kwargs)

    @swagger.operation(**invoice_product_delete_schema)
    @token_required()
    def delete(self, *args, **kwargs):
        """Delete instance by id."""
        return super().delete(*args, **kwargs)


class InvoiceProductsRoute(ModelsRoute):
    """Operations with many InvoiceProducts instances and instance creation."""

    model = InvoiceProduct
    post_parser = invoice_product_parser
    model_fields = InvoiceProductFields.resource_fields

    @swagger.operation(**invoice_product_post_schema)
    @token_required()
    def post(self, *args, **kwargs):
        """Create model instance."""
        return super().post(*args, **kwargs)

    @swagger.operation(**invoice_products_get_schema)
    @token_required()
    def get(self, *args, **kwargs):
        """Get model instance list."""
        return super().get(*args, **kwargs)


api.add_resource(InvoiceRoute, "/invoice/<instance_id>")
api.add_resource(InvoicesRoute, "/invoice/")
api.add_resource(InvoiceProductRoute, "/invoice-product/<instance_id>")
api.add_resource(InvoiceProductsRoute, "/invoice-product/")
