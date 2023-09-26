"""Invoice routes."""
from flask_restful import fields
from flask_restful_swagger import swagger

from api import Invoice, InvoiceProduct, api
from api.apps.invoice.parsers import (
    invoice_parser,
    invoice_patch_parser,
    invoice_product_parser,
    invoice_product_patch_parser,
)
from api.model_routes import ModelRoute, ModelsRoute


@swagger.model
class InvoiceFields:
    """InvoiceRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "name": fields.String,
        "order_id": fields.Integer,
        "created_at": fields.DateTime,
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
    put_parser = invoice_parser
    patch_parser = invoice_patch_parser
    model_fields = InvoiceFields.resource_fields

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


class InvoicesRoute(ModelsRoute):
    """Operations with many Invoice isntances and instance creation."""

    model = Invoice
    post_parser = invoice_parser
    model_fields = InvoiceFields.resource_fields

    @swagger.operation()
    def post(self, *args, **kwargs):
        """Create model instance."""
        return super().post(*args, **kwargs)

    @swagger.operation()
    def get(self, *args, **kwargs):
        """Get model instance list."""
        return super().get(*args, **kwargs)


class InvoiceProductRoute(ModelRoute):
    """Operations with single InvoiceProducts instance."""

    model = InvoiceProduct
    put_parser = invoice_product_parser
    patch_parser = invoice_product_patch_parser
    model_fields = InvoiceProductFields.resource_fields

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


class InvoiceProductsRoute(ModelsRoute):
    """Operations with many InvoiceProducts instances and instance creation."""

    model = InvoiceProduct
    post_parser = invoice_product_parser
    model_fields = InvoiceProductFields.resource_fields

    @swagger.operation()
    def post(self, *args, **kwargs):
        """Create model instance."""
        return super().post(*args, **kwargs)

    @swagger.operation()
    def get(self, *args, **kwargs):
        """Get model instance list."""
        return super().get(*args, **kwargs)


api.add_resource(InvoiceRoute, "/invoice/<instance_id>")
api.add_resource(InvoicesRoute, "/invoice/")
api.add_resource(InvoiceProductRoute, "/invoice-product/<instance_id>")
api.add_resource(InvoiceProductsRoute, "/invoice-product/")
