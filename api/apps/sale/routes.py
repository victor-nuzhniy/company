"""Routes for sale apps."""
from flask_restful import fields
from flask_restful_swagger import swagger

from api import SaleInvoice, SaleInvoiceProduct, api
from api.apps.sale.parsers import (
    sale_invoice_parser,
    sale_invoice_patch_parser,
    sale_invoice_product_parser,
    sale_invoice_product_patch_parser,
)
from api.apps.sale.schemas import (
    sale_invoice_delete_schema,
    sale_invoice_get_schema,
    sale_invoice_patch_schema,
    sale_invoice_post_schema,
    sale_invoice_product_delete_schema,
    sale_invoice_product_get_schema,
    sale_invoice_product_patch_schema,
    sale_invoice_product_post_schema,
    sale_invoice_product_put_schema,
    sale_invoice_products_get_schema,
    sale_invoice_put_schema,
    sale_invoices_get_schema,
)
from api.model_routes import ModelRoute, ModelsRoute, token_required


@swagger.model
class SaleInvoiceFields:
    """SaleInvoiceRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "name": fields.String,
        "invoice_id": fields.Integer,
        "created_at": fields.DateTime,
        "done": fields.Boolean,
    }


@swagger.model
class SaleInvoiceProductFields:
    """SaleInvoiceProductRoute output fields."""

    resource_fields = {
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
    model_fields = SaleInvoiceFields.resource_fields

    @swagger.operation(**sale_invoice_get_schema)
    @token_required()
    def get(self, *args, **kwargs):
        """Get model instance by id."""
        return super().get(*args, **kwargs)

    @swagger.operation(**sale_invoice_put_schema)
    @token_required()
    def put(self, *args, **kwargs):
        """Update instance by id."""
        return super().put(*args, **kwargs)

    @swagger.operation(**sale_invoice_patch_schema)
    @token_required()
    def patch(self, *args, **kwargs):
        """Update instance bu id, partially."""
        return super().patch(*args, **kwargs)

    @swagger.operation(**sale_invoice_delete_schema)
    @token_required()
    def delete(self, *args, **kwargs):
        """Delete instance by id."""
        return super().delete(*args, **kwargs)


class SaleInvoicesRoute(ModelsRoute):
    """Operations with many SaleInvoice instances and instance creation."""

    model = SaleInvoice
    post_parser = sale_invoice_parser
    model_fields = SaleInvoiceFields.resource_fields

    @swagger.operation(**sale_invoice_post_schema)
    @token_required()
    def post(self, *args, **kwargs):
        """Create model instance."""
        return super().post(*args, **kwargs)

    @swagger.operation(**sale_invoices_get_schema)
    @token_required()
    def get(self, *args, **kwargs):
        """Get model instance list."""
        return super().get(*args, **kwargs)


class SaleInvoiceProductRoute(ModelRoute):
    """Operations with single SaleInvoiceProduct instance."""

    model = SaleInvoiceProduct
    put_parser = sale_invoice_product_parser
    patch_parser = sale_invoice_product_patch_parser
    model_fields = SaleInvoiceProductFields.resource_fields

    @swagger.operation(**sale_invoice_product_get_schema)
    @token_required()
    def get(self, *args, **kwargs):
        """Get model instance by id."""
        return super().get(*args, **kwargs)

    @swagger.operation(**sale_invoice_product_put_schema)
    @token_required()
    def put(self, *args, **kwargs):
        """Update instance by id."""
        return super().put(*args, **kwargs)

    @swagger.operation(**sale_invoice_product_patch_schema)
    @token_required()
    def patch(self, *args, **kwargs):
        """Update instance bu id, partially."""
        return super().patch(*args, **kwargs)

    @swagger.operation(**sale_invoice_product_delete_schema)
    @token_required()
    def delete(self, *args, **kwargs):
        """Delete instance by id."""
        return super().delete(*args, **kwargs)


class SaleInvoiceProductsRoute(ModelsRoute):
    """Operations with many SaleInvoiceProduct instance and instance creation."""

    model = SaleInvoiceProduct
    post_parser = sale_invoice_product_parser
    model_fields = SaleInvoiceProductFields.resource_fields

    @swagger.operation(**sale_invoice_product_post_schema)
    @token_required()
    def post(self, *args, **kwargs):
        """Create model instance."""
        return super().post(*args, **kwargs)

    @swagger.operation(**sale_invoice_products_get_schema)
    @token_required()
    def get(self, *args, **kwargs):
        """Get model instance list."""
        return super().get(*args, **kwargs)


api.add_resource(SaleInvoiceRoute, "/sale-invoice/<instance_id>")
api.add_resource(SaleInvoicesRoute, "/sale-invoice/")
api.add_resource(SaleInvoiceProductRoute, "/sale-invoice-product/<instance_id>")
api.add_resource(SaleInvoiceProductsRoute, "/sale-invoice-product/")
