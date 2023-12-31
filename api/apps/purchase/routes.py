"""Routes for purchase apps."""
from flask_restful import Resource, fields, marshal
from flask_restful_swagger import swagger

from api import PurchaseInvoice, PurchaseInvoiceProduct, api
from api.apps.invoice.validators import product_id as product_id_validator
from api.apps.purchase.parsers import (
    purchase_invoice_patch_parser,
    purchase_invoice_post_parser,
    purchase_invoice_product_parser,
    purchase_invoice_product_patch_parser,
    purchase_invoice_put_parser,
    purchase_registry_parser,
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
    purchase_invoice_products_left_get_schema,
    purchase_invoice_put_schema,
    purchase_invoices_get_schema,
    purchase_invoices_products_get_schema,
    purchase_registry_get_schema,
)
from api.apps.purchase.services import (
    get_purchase_invoice_data,
    get_purchase_invoice_products_by_product_id_with_products_left,
    get_purchase_invoice_products_by_purchase_id,
)
from api.apps.purchase.validators import (
    purchase_invoice_id as purchase_invoice_id_validator,
)
from api.common import CustomDateTimeFormat
from api.model_routes import ModelRoute, ModelsRoute, token_required


@swagger.model
class PurchaseInvoiceFields:
    """PurchaseInvoiceRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "name": fields.String,
        "agreement_id": fields.Integer,
        "created_at": CustomDateTimeFormat,
    }


@swagger.model
class PurchaseInvoiceProductFields:
    """PurchaseInvoiceProductRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "product_id": fields.Integer,
        "quantity": fields.Integer,
        "price": fields.Integer,
        "purchase_invoice_id": fields.Integer,
        "products_left": fields.Integer,
    }


@swagger.model
class PurchaseRegistryFields:
    """PurchaseRegistry output fields."""

    resource_fields = {
        "id": fields.Integer,
        "created_at": CustomDateTimeFormat,
        "purchase_name": fields.String,
        "summ": fields.Integer,
        "currency": fields.String,
        "counterparty": fields.String,
        "agreement": fields.String,
    }


@swagger.model
class PurchaseInvoicesProductsFields:
    """PurchaseInvoicesProductsRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "product_id": fields.Integer,
        "quantity": fields.Integer,
        "price": fields.Integer,
        "products_left": fields.Integer,
        "purchase_invoice_id": fields.Integer,
        "name": fields.String,
        "code": fields.String,
        "currency": fields.String,
        "units": fields.String,
    }


class PurchaseInvoiceProductsLeftFields:
    """PurchaseInvoiceProductsLeftRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "product_id": fields.Integer,
        "products_left": fields.Integer,
        "name": fields.String,
        "code": fields.String,
    }


class PurchaseInvoiceRoute(ModelRoute):
    """Operations with single PurchaseInvoice instance."""

    model = PurchaseInvoice
    put_parser = purchase_invoice_put_parser
    patch_parser = purchase_invoice_patch_parser
    model_fields = PurchaseInvoiceFields.resource_fields

    @swagger.operation(**purchase_invoice_get_schema)
    @token_required()
    def get(self, *args, **kwargs):
        """Get model instance by id."""
        return super().get(*args, **kwargs)

    @swagger.operation(**purchase_invoice_put_schema)
    @token_required()
    def put(self, *args, **kwargs):
        """Update instance by id."""
        return super().put(*args, **kwargs)

    @swagger.operation(**purchase_invoice_patch_schema)
    @token_required()
    def patch(self, *args, **kwargs):
        """Update instance bu id, partially."""
        return super().patch(*args, **kwargs)

    @swagger.operation(**purchase_invoice_delete_schema)
    @token_required()
    def delete(self, *args, **kwargs):
        """Delete instance by id."""
        return super().delete(*args, **kwargs)


class PurchaseInvoicesRoute(ModelsRoute):
    """Operations with many PurchaseInvoice instances and instance creations."""

    model = PurchaseInvoice
    post_parser = purchase_invoice_post_parser
    model_fields = PurchaseInvoiceFields.resource_fields

    @swagger.operation(**purchase_invoice_post_schema)
    @token_required()
    def post(self, *args, **kwargs):
        """Create model instance."""
        return super().post(*args, **kwargs)

    @swagger.operation(**purchase_invoices_get_schema)
    @token_required()
    def get(self, *args, **kwargs):
        """Get model instance list."""
        return super().get(*args, **kwargs)


class PurchaseInvoiceProductRoute(ModelRoute):
    """Operations with single PurchaseInvoiceProducts instance."""

    model = PurchaseInvoiceProduct
    put_parser = purchase_invoice_product_parser
    patch_parser = purchase_invoice_product_patch_parser
    model_fields = PurchaseInvoiceProductFields.resource_fields

    @swagger.operation(**purchase_invoice_product_get_schema)
    @token_required()
    def get(self, *args, **kwargs):
        """Get model instance by id."""
        return super().get(*args, **kwargs)

    @swagger.operation(**purchase_invoice_product_put_schema)
    @token_required()
    def put(self, *args, **kwargs):
        """Update instance by id."""
        return super().put(*args, **kwargs)

    @swagger.operation(**purchase_invoice_product_patch_schema)
    @token_required()
    def patch(self, *args, **kwargs):
        """Update instance bu id, partially."""
        return super().patch(*args, **kwargs)

    @swagger.operation(**purchase_invoice_product_delete_schema)
    @token_required()
    def delete(self, *args, **kwargs):
        """Delete instance by id."""
        return super().delete(*args, **kwargs)


class PurchaseInvoiceProductsRoute(ModelsRoute):
    """Operatios with PurchaseInvoiceProducts instances and instance creation."""

    model = PurchaseInvoiceProduct
    post_parser = purchase_invoice_product_parser
    model_fields = PurchaseInvoiceProductFields.resource_fields

    @swagger.operation(**purchase_invoice_product_post_schema)
    @token_required()
    def post(self, *args, **kwargs):
        """Create model instance."""
        return super().post(*args, **kwargs)

    @swagger.operation(**purchase_invoice_products_get_schema)
    @token_required()
    def get(self, *args, **kwargs):
        """Get model instance list."""
        return super().get(*args, **kwargs)


class PurchaseRegistryRoute(Resource):
    """Purchase registry information."""

    @swagger.operation(**purchase_registry_get_schema)
    @token_required()
    def get(self, *args, **kwargs):
        """Get purchase registry products list."""
        args = purchase_registry_parser.parse_args()
        return marshal(
            get_purchase_invoice_data(**args),
            PurchaseRegistryFields.resource_fields,
        )


class PurchaseInvoicesProductsRoute(Resource):
    """Getting PurchaseInvoices products list by purchase invoice id."""

    @swagger.operation(**purchase_invoices_products_get_schema)
    @token_required()
    def get(self, purchase_invoice_id, *args, **kwargs):
        """Get PurchaseInvoices products list by purchase invoice id."""
        purchase_invoice_id = purchase_invoice_id_validator(purchase_invoice_id)
        return marshal(
            get_purchase_invoice_products_by_purchase_id(purchase_invoice_id),
            PurchaseInvoicesProductsFields.resource_fields,
        )


class PurchaseInvoiceProductsLeftRoute(Resource):
    """Getting PurchaseInvoices products list with products_left > 0 and product_id."""

    @swagger.operation(**purchase_invoice_products_left_get_schema)
    @token_required()
    def get(self, product_id, *args, **kwargs):
        """Get PurchaseInvoice products list with products_left > 0 and product_id."""
        product_id = product_id_validator(product_id)
        return marshal(
            get_purchase_invoice_products_by_product_id_with_products_left(product_id),
            PurchaseInvoiceProductsLeftFields.resource_fields,
        )


api.add_resource(PurchaseInvoiceRoute, "/purchase-invoice/<instance_id>/")
api.add_resource(PurchaseInvoicesRoute, "/purchase-invoice/")
api.add_resource(
    PurchaseInvoiceProductRoute, "/purchase-invoice-product/<instance_id>/"
)
api.add_resource(PurchaseInvoiceProductsRoute, "/purchase-invoice-product/")
api.add_resource(PurchaseRegistryRoute, "/purchase-registry/")
api.add_resource(
    PurchaseInvoicesProductsRoute, "/purchase-invoice-products/<purchase_invoice_id>/"
)
api.add_resource(
    PurchaseInvoiceProductsLeftRoute, "/purchase-invoice-products/product/<product_id>/"
)
