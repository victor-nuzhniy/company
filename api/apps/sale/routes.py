"""Routes for sale apps."""
from flask_restful import Resource, fields, marshal
from flask_restful_swagger import swagger

from api import SaleInvoice, SaleInvoiceProduct, api
from api.apps.invoice.validators import agreement_id as agreement_id_validator
from api.apps.purchase.parsers import purchase_registry_parser
from api.apps.sale.parsers import (
    sale_invoice_patch_parser,
    sale_invoice_post_parser,
    sale_invoice_product_parser,
    sale_invoice_product_patch_parser,
    sale_invoice_put_parser,
)
from api.apps.sale.schemas import (
    agreement_sale_invoices_get_schema,
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
    sale_invoices_products_get_schema,
    sale_registry_get_schema,
    tax_sale_invoices_products_left_get_schema,
)
from api.apps.sale.services import (
    get_sale_invoice_data,
    get_sale_invoice_products_by_sale_invoice_id,
    get_sale_invoices_by_agreement_id,
    get_tax_sale_invoice_products_left,
)
from api.apps.sale.validators import sale_invoice_id as sale_invoice_id_validator
from api.apps.tax.validators import tax_invoice_id as tax_invoice_id_validator
from api.common import CustomDateTimeFormat
from api.model_routes import ModelRoute, ModelsRoute, token_required


@swagger.model
class SaleInvoiceFields:
    """SaleInvoiceRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "name": fields.String,
        "invoice_id": fields.Integer,
        "created_at": CustomDateTimeFormat,
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


@swagger.model
class SaleRegistryFields:
    """SaleRegistryRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "created_at": CustomDateTimeFormat,
        "name": fields.String,
        "summ": fields.Integer,
        "currency": fields.String,
        "counterparty": fields.String,
        "agreement": fields.String,
        "invoice": fields.String,
        "done": fields.Boolean,
    }


@swagger.model
class SaleInvoicesProductsFields:
    """SaleInvoicesProductsRoute output fields."""

    resourse_fields = {
        "id": fields.Integer,
        "product_id": fields.Integer,
        "quantity": fields.Integer,
        "price": fields.Integer,
        "sale_invoice_id": fields.Integer,
        "name": fields.String,
        "code": fields.String,
        "currency": fields.String,
        "units": fields.String,
    }


class SaleInvoiceRoute(ModelRoute):
    """Operations with single SaleInvoice instance."""

    model = SaleInvoice
    put_parser = sale_invoice_put_parser
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
    post_parser = sale_invoice_post_parser
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


class SaleRegistryRoute(Resource):
    """Sale registry information."""

    @swagger.operation(**sale_registry_get_schema)
    @token_required()
    def get(self, *args, **kwargs):
        """Get sale registry list."""
        args = purchase_registry_parser.parse_args()
        return marshal(
            get_sale_invoice_data(**args),
            SaleRegistryFields.resource_fields,
        )


class SaleInvoicesProductsRoute(Resource):
    """Getting SaleInvoice products list by sale invoice id."""

    @swagger.operation(**sale_invoices_products_get_schema)
    @token_required()
    def get(self, sale_invoice_id, *args, **kwargs):
        """Get SaleInvoice products list by sale invoice id."""
        sale_invoice_id = sale_invoice_id_validator(sale_invoice_id)
        return marshal(
            get_sale_invoice_products_by_sale_invoice_id(sale_invoice_id),
            SaleInvoicesProductsFields.resourse_fields,
        )


class TaxSaleInvoiceProductsLeftRoute(Resource):
    """
    Getting SaleInvoice products list by sale invoice id.

    Products, included in tax invoice, will not be included in query.
    There are not products will be available from sale invoice with done True.
    """

    @swagger.operation(**tax_sale_invoices_products_left_get_schema)
    @token_required()
    def get(self, sale_invoice_id, tax_invoice_id, *args, **kwargs):
        """Get SaleInvoice products list by sale invoice id and tax_invoice_id."""
        sale_invoice_id = sale_invoice_id_validator(sale_invoice_id)
        tax_invoice_id = tax_invoice_id_validator(tax_invoice_id)
        return marshal(
            get_tax_sale_invoice_products_left(
                int(sale_invoice_id), int(tax_invoice_id)
            ),
            SaleInvoicesProductsFields.resourse_fields,
        )


class AgreementSaleInvoicesRoute(Resource):
    """Getting SaleInvoice list by agreement id."""

    @swagger.operation(**agreement_sale_invoices_get_schema)
    @token_required()
    def get(self, agreement_id, *args, **kwargs):
        """Get SaleInvoice list by agreement id."""
        agreement_id = agreement_id_validator(agreement_id)
        return marshal(
            get_sale_invoices_by_agreement_id(agreement_id),
            SaleInvoiceFields.resource_fields,
        )


api.add_resource(SaleInvoiceRoute, "/sale-invoice/<instance_id>/")
api.add_resource(SaleInvoicesRoute, "/sale-invoice/")
api.add_resource(SaleInvoiceProductRoute, "/sale-invoice-product/<instance_id>/")
api.add_resource(SaleInvoiceProductsRoute, "/sale-invoice-product/")
api.add_resource(SaleRegistryRoute, "/sale-invoice-registry/")
api.add_resource(SaleInvoicesProductsRoute, "/sale-invoice-products/<sale_invoice_id>/")
api.add_resource(
    TaxSaleInvoiceProductsLeftRoute,
    "/sale-invoice-products/<sale_invoice_id>/<tax_invoice_id>/",
)
api.add_resource(AgreementSaleInvoicesRoute, "/agreement-sale-invoices/<agreement_id>/")
