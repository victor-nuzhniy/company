"""Routes for purchase apps."""
import typing

from flask.typing import ResponseReturnValue
from flask_restful_swagger import swagger

from api import api
from api.apps.purchase import models
from api.apps.purchase.parsers import (
    purchase_invoice_patch_parser,
    purchase_invoice_post_parser,
    purchase_invoice_product_parser,
    purchase_invoice_product_patch_parser,
    purchase_invoice_put_parser,
)
from api.apps.purchase.schemas import (
    purchase_invoice_delete_schema,
    purchase_invoice_get_schema,
    purchase_invoice_patch_schema,
    purchase_invoice_post_schema,
    purchase_invoice_product_delete_schema,
    purchase_invoice_product_get_schema,
    purchase_invoice_product_patch_schema,
    purchase_invoice_product_post_schema,
    purchase_invoice_product_put_schema,
    purchase_invoice_products_get_schema,
    purchase_invoice_put_schema,
    purchase_invoices_get_schema,
)
from api.apps.purchase.swagger_models import (
    PurchaseInvoiceFields,
    PurchaseInvoiceProductFields,
)
from api.model_routes import ModelRoute, ModelsRoute, token_required


class PurchaseInvoiceRoute(ModelRoute):
    """Operations with single PurchaseInvoice instance."""

    model = models.PurchaseInvoice
    put_parser = purchase_invoice_put_parser
    patch_parser = purchase_invoice_patch_parser
    model_fields = PurchaseInvoiceFields.resource_fields

    @swagger.operation(**purchase_invoice_get_schema)
    @token_required()
    def get(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Get model instance by id."""
        return super().get(*args, **kwargs)

    @swagger.operation(**purchase_invoice_put_schema)
    @token_required()
    def put(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Update instance by id."""
        return super().put(*args, **kwargs)

    @swagger.operation(**purchase_invoice_patch_schema)
    @token_required()
    def patch(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Update instance bu id, partially."""
        return super().patch(*args, **kwargs)

    @swagger.operation(**purchase_invoice_delete_schema)
    @token_required()
    def delete(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Delete instance by id."""
        return super().delete(*args, **kwargs)


class PurchaseInvoicesRoute(ModelsRoute):
    """Operations with many PurchaseInvoice instances and instance creations."""

    model = models.PurchaseInvoice
    post_parser = purchase_invoice_post_parser
    model_fields = PurchaseInvoiceFields.resource_fields

    @swagger.operation(**purchase_invoice_post_schema)
    @token_required()
    def post(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Create model instance."""
        return super().post(*args, **kwargs)

    @swagger.operation(**purchase_invoices_get_schema)
    @token_required()
    def get(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Get model instance list."""
        return super().get(*args, **kwargs)


class PurchaseInvoiceProductRoute(ModelRoute):
    """Operations with single PurchaseInvoiceProducts instance."""

    model = models.PurchaseInvoiceProduct
    put_parser = purchase_invoice_product_parser
    patch_parser = purchase_invoice_product_patch_parser
    model_fields = PurchaseInvoiceProductFields.resource_fields

    @swagger.operation(**purchase_invoice_product_get_schema)
    @token_required()
    def get(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Get model instance by id."""
        return super().get(*args, **kwargs)

    @swagger.operation(**purchase_invoice_product_put_schema)
    @token_required()
    def put(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Update instance by id."""
        return super().put(*args, **kwargs)

    @swagger.operation(**purchase_invoice_product_patch_schema)
    @token_required()
    def patch(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Update instance bu id, partially."""
        return super().patch(*args, **kwargs)

    @swagger.operation(**purchase_invoice_product_delete_schema)
    @token_required()
    def delete(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Delete instance by id."""
        return super().delete(*args, **kwargs)


class PurchaseInvoiceProductsRoute(ModelsRoute):
    """Operatios with PurchaseInvoiceProducts instances and instance creation."""

    model = models.PurchaseInvoiceProduct
    post_parser = purchase_invoice_product_parser
    model_fields = PurchaseInvoiceProductFields.resource_fields

    @swagger.operation(**purchase_invoice_product_post_schema)
    @token_required()
    def post(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Create model instance."""
        return super().post(*args, **kwargs)

    @swagger.operation(**purchase_invoice_products_get_schema)
    @token_required()
    def get(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Get model instance list."""
        return super().get(*args, **kwargs)


api.add_resource(PurchaseInvoiceRoute, "/purchase-invoice/<instance_id>/")
api.add_resource(PurchaseInvoicesRoute, "/purchase-invoice/")
api.add_resource(
    PurchaseInvoiceProductRoute,
    "/purchase-invoice-product/<instance_id>/",
)
api.add_resource(PurchaseInvoiceProductsRoute, "/purchase-invoice-product/")
