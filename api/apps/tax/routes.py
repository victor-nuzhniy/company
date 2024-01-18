"""Routes for tax apps."""
import typing

from flask.typing import ResponseReturnValue
from flask_restful_swagger import swagger

from api import api
from api.apps.tax import models
from api.apps.tax.parsers import (
    tax_invoice_patch_parser,
    tax_invoice_post_parser,
    tax_invoice_product_parser,
    tax_invoice_product_patch_parser,
    tax_invoice_put_parser,
)
from api.apps.tax.schemas import (
    tax_invoice_delete_schema,
    tax_invoice_get_schema,
    tax_invoice_patch_schema,
    tax_invoice_post_schema,
    tax_invoice_product_delete_schema,
    tax_invoice_product_get_schema,
    tax_invoice_product_patch_schema,
    tax_invoice_product_post_schema,
    tax_invoice_product_put_schema,
    tax_invoice_products_get_schema,
    tax_invoice_put_schema,
    tax_invoices_get_schema,
)
from api.apps.tax.swagger_models import TaxInvoiceFields, TaxInvoiceProductFields
from api.model_routes import ModelRoute, ModelsRoute, token_required


class TaxInvoiceRoute(ModelRoute):
    """Operations with single TaxInvoice instance."""

    model = models.TaxInvoice
    put_parser = tax_invoice_put_parser
    patch_parser = tax_invoice_patch_parser
    model_fields = TaxInvoiceFields.resource_fields

    @swagger.operation(**tax_invoice_get_schema)
    @token_required()
    def get(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Get model instance by id."""
        return super().get(*args, **kwargs)

    @swagger.operation(**tax_invoice_put_schema)
    @token_required(is_admin=True)
    def put(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Update instance by id."""
        return super().put(*args, **kwargs)

    @swagger.operation(**tax_invoice_patch_schema)
    @token_required(is_admin=True)
    def patch(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Update instance bu id, partially."""
        return super().patch(*args, **kwargs)

    @swagger.operation(**tax_invoice_delete_schema)
    @token_required(is_admin=True)
    def delete(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Delete instance by id."""
        return super().delete(*args, **kwargs)


class TaxInvoicesRoute(ModelsRoute):
    """Operations with TaxInvoice instances and instance creation."""

    model = models.TaxInvoice
    post_parser = tax_invoice_post_parser
    model_fields = TaxInvoiceFields.resource_fields

    @swagger.operation(**tax_invoice_post_schema)
    @token_required(is_admin=True)
    def post(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Create model instance."""
        return super().post(*args, **kwargs)

    @swagger.operation(**tax_invoices_get_schema)
    @token_required()
    def get(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Get model instance list."""
        return super().get(*args, **kwargs)


class TaxInvoiceProductRoute(ModelRoute):
    """Operations with single TaxInvoiceProducts instance."""

    model = models.TaxInvoiceProduct
    put_parser = tax_invoice_product_parser
    patch_parser = tax_invoice_product_patch_parser
    model_fields = TaxInvoiceProductFields.resource_fields

    @swagger.operation(**tax_invoice_product_get_schema)
    @token_required()
    def get(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Get model instance by id."""
        return super().get(*args, **kwargs)

    @swagger.operation(**tax_invoice_product_put_schema)
    @token_required(is_admin=True)
    def put(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Update instance by id."""
        return super().put(*args, **kwargs)

    @swagger.operation(**tax_invoice_product_patch_schema)
    @token_required(is_admin=True)
    def patch(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Update instance bu id, partially."""
        return super().patch(*args, **kwargs)

    @swagger.operation(**tax_invoice_product_delete_schema)
    @token_required(is_admin=True)
    def delete(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Delete instance by id."""
        return super().delete(*args, **kwargs)


class TaxInvoiceProductsRoute(ModelsRoute):
    """Operations with TaxInvoiceProducts instances and instance creation."""

    model = models.TaxInvoiceProduct
    post_parser = tax_invoice_product_parser
    model_fields = TaxInvoiceProductFields.resource_fields

    @swagger.operation(**tax_invoice_product_post_schema)
    @token_required(is_admin=True)
    def post(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Create model instance."""
        return super().post(*args, **kwargs)

    @swagger.operation(**tax_invoice_products_get_schema)
    @token_required()
    def get(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Get model instance list."""
        return super().get(*args, **kwargs)


api.add_resource(TaxInvoiceRoute, "/tax-invoice/<instance_id>/")
api.add_resource(TaxInvoicesRoute, "/tax-invoice/")
api.add_resource(TaxInvoiceProductRoute, "/tax-invoice-product/<instance_id>/")
api.add_resource(TaxInvoiceProductsRoute, "/tax-invoice-product/")
