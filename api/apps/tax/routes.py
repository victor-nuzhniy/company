"""Routes for tax apps."""
from flask_restful import Resource, fields, marshal
from flask_restful_swagger import swagger

from api import TaxInvoice, TaxInvoiceProduct, api
from api.apps.purchase.parsers import purchase_registry_parser
from api.apps.purchase.schemas import purchase_invoice_products_left_get_schema
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
    tax_invoice_product_with_adding_products_left_delete_schema,
    tax_invoice_products_get_schema,
    tax_invoice_put_schema,
    tax_invoice_with_purchase_add_products_left_delete_schema,
    tax_invoices_get_schema,
    tax_invoices_products_get_schema,
    tax_registry_get_schema,
)
from api.apps.tax.services import (
    create_tax_invoice_product_with_subtract_purchase_products_left,
    delete_tax_invoice_product_with_adding_purchase_products_left,
    delete_tax_invoice_with_adding_purchase_products_left_fieds,
    get_tax_data,
    get_tax_invoice_products_by_tax_invoice_id,
)
from api.apps.tax.validators import tax_invoice_id as tax_invoice_id_validator
from api.apps.tax.validators import (
    tax_invoice_product_id as tax_invoice_product_id_validator,
)
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


@swagger.model
class TaxInvoicesProductsFields:
    """InvoicesProductsRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "product_id": fields.Integer,
        "quantity": fields.Integer,
        "sale_price": fields.Integer,
        "purchase_price": fields.Integer,
        "tax_invoice_id": fields.Integer,
        "sale_invoice_product_id": fields.Integer,
        "purchase_invoice_product_id": fields.Integer,
        "name": fields.String,
        "code": fields.String,
        "currency": fields.String,
        "units": fields.String,
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
    @token_required(is_admin=True)
    def put(self, *args, **kwargs):
        """Update instance by id."""
        return super().put(*args, **kwargs)

    @swagger.operation(**tax_invoice_patch_schema)
    @token_required(is_admin=True)
    def patch(self, *args, **kwargs):
        """Update instance bu id, partially."""
        return super().patch(*args, **kwargs)

    @swagger.operation(**tax_invoice_delete_schema)
    @token_required(is_admin=True)
    def delete(self, *args, **kwargs):
        """Delete instance by id."""
        return super().delete(*args, **kwargs)


class TaxInvoicesRoute(ModelsRoute):
    """Operations with TaxInvoice instances and instance creation."""

    model = TaxInvoice
    post_parser = tax_invoice_post_parser
    model_fields = TaxInvoiceFields.resource_fields

    @swagger.operation(**tax_invoice_post_schema)
    @token_required(is_admin=True)
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
    @token_required(is_admin=True)
    def put(self, *args, **kwargs):
        """Update instance by id."""
        return super().put(*args, **kwargs)

    @swagger.operation(**tax_invoice_product_patch_schema)
    @token_required(is_admin=True)
    def patch(self, *args, **kwargs):
        """Update instance bu id, partially."""
        return super().patch(*args, **kwargs)

    @swagger.operation(**tax_invoice_product_delete_schema)
    @token_required(is_admin=True)
    def delete(self, *args, **kwargs):
        """Delete instance by id."""
        return super().delete(*args, **kwargs)


class TaxInvoiceProductsRoute(ModelsRoute):
    """Operations with TaxInvoiceProducts instances and instance creation."""

    model = TaxInvoiceProduct
    post_parser = tax_invoice_product_parser
    model_fields = TaxInvoiceProductFields.resource_fields

    @swagger.operation(**tax_invoice_product_post_schema)
    @token_required(is_admin=True)
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


class TaxInvoicesProductsRoute(Resource):
    """Getting TaxInvoice products list by tax invoice id."""

    @swagger.operation(**tax_invoices_products_get_schema)
    @token_required()
    def get(self, tax_invoice_id, *args, **kwargs):
        """Get TaxInvoice products list by tax invoice id."""
        tax_invoice_id = tax_invoice_id_validator(tax_invoice_id)
        return marshal(
            get_tax_invoice_products_by_tax_invoice_id(tax_invoice_id),
            TaxInvoicesProductsFields.resource_fields,
        )


class TaxInvoiceProductCreateRoute(Resource):
    """Create TaxInvoiceProduct with subtracting purchase products_left field."""

    @swagger.operation(**purchase_invoice_products_left_get_schema)
    @token_required(is_admin=True)
    def post(self, *args, **kwargs):
        """Create TaxInvoiceProduct with subtracting purhcase products_left field."""
        args = tax_invoice_product_parser.parse_args()
        return marshal(
            create_tax_invoice_product_with_subtract_purchase_products_left(**args),
            TaxInvoiceProductFields.resource_fields,
        )


class TaxInvoiceProductDeleteRoute(Resource):
    """Delete TaxInvoiceProduct with adding purchase products_left field."""

    @swagger.operation(**tax_invoice_product_with_adding_products_left_delete_schema)
    @token_required(is_admin=True)
    def delete(self, tax_invoice_product_id, *args, **kwargs):
        """Delete TaxInvoiceProduct with adding purchase products_left field."""
        tax_invoice_product_id = tax_invoice_product_id_validator(
            tax_invoice_product_id
        )
        delete_tax_invoice_product_with_adding_purchase_products_left(
            tax_invoice_product_id
        )
        return {"message": "Tax invoice product was successfully deleted."}


class TaxInvoiceDeleteRoute(Resource):
    """Delete TaxInvoice with adding purchase products_left fields."""

    @swagger.operation(**tax_invoice_with_purchase_add_products_left_delete_schema)
    @token_required(is_admin=True)
    def delete(self, tax_invoice_id, *args, **kwargs):
        """Delete TaxInvoice with adding purchase products_left fields."""
        tax_invoice_id = tax_invoice_id_validator(tax_invoice_id)
        delete_tax_invoice_with_adding_purchase_products_left_fieds(tax_invoice_id)
        return {
            "message": f"TaxInvoice with id {tax_invoice_id} was successfully deleted."
        }


api.add_resource(TaxInvoiceRoute, "/tax-invoice/<instance_id>/")
api.add_resource(TaxInvoicesRoute, "/tax-invoice/")
api.add_resource(TaxInvoiceProductRoute, "/tax-invoice-product/<instance_id>/")
api.add_resource(TaxInvoiceProductsRoute, "/tax-invoice-product/")
api.add_resource(TaxRegistryRoute, "/tax-registry/")
api.add_resource(TaxInvoicesProductsRoute, "/tax-invoice-products/<tax_invoice_id>/")
api.add_resource(TaxInvoiceProductCreateRoute, "/tax-invoice-product-create/")
api.add_resource(
    TaxInvoiceProductDeleteRoute,
    "/tax-invoice-product-delete/<tax_invoice_product_id>/",
)
api.add_resource(TaxInvoiceDeleteRoute, "/tax-invoice-delete/<tax_invoice_id>/")
