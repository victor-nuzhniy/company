"""Routes for tax apps."""
from flask_restful import Resource, fields, marshal
from flask_restful_swagger import swagger

from api import TaxInvoice, TaxInvoiceProduct, api
from api.apps.purchase.parsers import purchase_registry_parser
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
    tax_registry_get_schema,
)
from api.apps.tax.services import get_tax_data
from api.common import CustomDateTimeFormat
from api.model_routes import ModelRoute, ModelsRoute, token_required


@swagger.model
class TaxInvoiceFields:
    """TaxInvoiceRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "name": fields.String,
        "sale_invoice_id": fields.Integer,
        "created_at": CustomDateTimeFormat,
    }


@swagger.model
class TaxInvoiceProductFields:
    """TaxInvoiceProductRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "tax_invoice_id": fields.Integer,
        "sale_invoice_product_id": fields.Integer,
        "purchase_invoice_product_id": fields.Integer,
        "quantity": fields.Integer,
    }


@swagger.model
class TaxRegistryFields:
    """TaxRegistryRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "created_at": CustomDateTimeFormat,
        "tax_invoice_name": fields.String,
        "invoice": fields.String,
        "invoice_id": fields.Integer,
        "sale_invoice": fields.String,
        "sale_invoice_id": fields.Integer,
        "purchase_invoice": fields.String,
        "purchase_invoice_id": fields.Integer,
        "agreement": fields.String,
        "agreement_id": fields.Integer,
        "counterparty": fields.String,
        "counterparty_id": fields.Integer,
        "sale_summ": fields.Integer,
        "purchase_summ": fields.Integer,
    }


class TaxInvoiceRoute(ModelRoute):
    """Operations with single TaxInvoice instance."""

    model = TaxInvoice
    put_parser = tax_invoice_put_parser
    patch_parser = tax_invoice_patch_parser
    model_fields = TaxInvoiceFields.resource_fields

    @swagger.operation(**tax_invoice_get_schema)
    @token_required()
    def get(self, *args, **kwargs):
        """Get model instance by id."""
        return super().get(*args, **kwargs)

    @swagger.operation(**tax_invoice_put_schema)
    @token_required()
    def put(self, *args, **kwargs):
        """Update instance by id."""
        return super().put(*args, **kwargs)

    @swagger.operation(**tax_invoice_patch_schema)
    @token_required()
    def patch(self, *args, **kwargs):
        """Update instance bu id, partially."""
        return super().patch(*args, **kwargs)

    @swagger.operation(**tax_invoice_delete_schema)
    @token_required()
    def delete(self, *args, **kwargs):
        """Delete instance by id."""
        return super().delete(*args, **kwargs)


class TaxInvoicesRoute(ModelsRoute):
    """Operations with TaxInvoice instances and instance creation."""

    model = TaxInvoice
    post_parser = tax_invoice_post_parser
    model_fields = TaxInvoiceFields.resource_fields

    @swagger.operation(**tax_invoice_post_schema)
    @token_required()
    def post(self, *args, **kwargs):
        """Create model instance."""
        return super().post(*args, **kwargs)

    @swagger.operation(**tax_invoices_get_schema)
    @token_required()
    def get(self, *args, **kwargs):
        """Get model instance list."""
        return super().get(*args, **kwargs)


class TaxInvoiceProductRoute(ModelRoute):
    """Operations with single TaxInvoiceProducts instance."""

    model = TaxInvoiceProduct
    put_parser = tax_invoice_product_parser
    patch_parser = tax_invoice_product_patch_parser
    model_fields = TaxInvoiceProductFields.resource_fields

    @swagger.operation(**tax_invoice_product_get_schema)
    @token_required()
    def get(self, *args, **kwargs):
        """Get model instance by id."""
        return super().get(*args, **kwargs)

    @swagger.operation(**tax_invoice_product_put_schema)
    @token_required()
    def put(self, *args, **kwargs):
        """Update instance by id."""
        return super().put(*args, **kwargs)

    @swagger.operation(**tax_invoice_product_patch_schema)
    @token_required()
    def patch(self, *args, **kwargs):
        """Update instance bu id, partially."""
        return super().patch(*args, **kwargs)

    @swagger.operation(**tax_invoice_product_delete_schema)
    @token_required()
    def delete(self, *args, **kwargs):
        """Delete instance by id."""
        return super().delete(*args, **kwargs)


class TaxInvoiceProductsRoute(ModelsRoute):
    """Operations with TaxInvoiceProducts instances and instance creation."""

    model = TaxInvoiceProduct
    post_parser = tax_invoice_product_parser
    model_fields = TaxInvoiceProductFields.resource_fields

    @swagger.operation(**tax_invoice_product_post_schema)
    @token_required()
    def post(self, *args, **kwargs):
        """Create model instance."""
        return super().post(*args, **kwargs)

    @swagger.operation(**tax_invoice_products_get_schema)
    @token_required()
    def get(self, *args, **kwargs):
        """Get model instance list."""
        return super().get(*args, **kwargs)


class TaxRegistryRoute(Resource):
    """Tax registry information."""

    @swagger.operation(**tax_registry_get_schema)
    @token_required()
    def get(self, *args, **kwargs):
        """Get tax registry list."""
        args = purchase_registry_parser.parse_args()
        return marshal(
            get_tax_data(**args),
            TaxRegistryFields.resource_fields,
        )


api.add_resource(TaxInvoiceRoute, "/tax-invoice/<instance_id>/")
api.add_resource(TaxInvoicesRoute, "/tax-invoice/")
api.add_resource(TaxInvoiceProductRoute, "/tax-invoice-product/<instance_id>/")
api.add_resource(TaxInvoiceProductsRoute, "/tax-invoice-product/")
api.add_resource(TaxRegistryRoute, "/tax-registry/")
