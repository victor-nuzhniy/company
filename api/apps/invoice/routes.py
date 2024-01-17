"""Invoice routes."""
import typing

from flask.typing import ResponseReturnValue
from flask_restful import Resource, marshal
from flask_restful_swagger import swagger

from api import Invoice, InvoiceProduct, api
from api.apps.invoice.parsers import (
    invoice_patch_parser,
    invoice_post_parser,
    invoice_product_parser,
    invoice_product_patch_parser,
    invoice_put_parser,
    order_registry_parser,
)
from api.apps.invoice.schemas import (
    agreement_invoice_products_get_schema,
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
    invoice_registry_get_schema,
    invoices_get_schema,
    invoices_products_get_schema,
)
from api.apps.invoice.services import (
    get_invoice_data,
    get_invoice_products_by_invoice_id,
)
from api.apps.invoice.swagger_models import (
    InvoiceFields,
    InvoiceProductFields,
    InvoiceRegistryFields,
    InvoicesProductsFields,
)
from api.apps.invoice.validators import agreement_id_valid, invoice_id_valid
from api.model_routes import ModelRoute, ModelsRoute, token_required
from api.services import crud


class InvoiceRoute(ModelRoute):
    """Operations with single Invoice instance."""

    model = Invoice
    put_parser = invoice_put_parser
    patch_parser = invoice_patch_parser
    model_fields = InvoiceFields.resource_fields

    @swagger.operation(**invoice_get_schema)
    @token_required()
    def get(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Get model instance by id."""
        return super().get(*args, **kwargs)

    @swagger.operation(**invoice_put_schema)
    @token_required()
    def put(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Update instance by id."""
        return super().put(*args, **kwargs)

    @swagger.operation(**invoice_patch_schema)
    @token_required()
    def patch(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Update instance bu id, partially."""
        return super().patch(*args, **kwargs)

    @swagger.operation(**invoice_delete_schema)
    @token_required()
    def delete(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Delete instance by id."""
        return super().delete(*args, **kwargs)


class InvoicesRoute(ModelsRoute):
    """Operations with many Invoice isntances and instance creation."""

    model = Invoice
    post_parser = invoice_post_parser
    model_fields = InvoiceFields.resource_fields

    @swagger.operation(**invoice_post_schema)
    @token_required()
    def post(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Create model instance."""
        return super().post(*args, **kwargs)

    @swagger.operation(**invoices_get_schema)
    @token_required()
    def get(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
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
    def get(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Get model instance by id."""
        return super().get(*args, **kwargs)

    @swagger.operation(**invoice_product_put_schema)
    @token_required()
    def put(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Update instance by id."""
        return super().put(*args, **kwargs)

    @swagger.operation(**invoice_product_patch_schema)
    @token_required()
    def patch(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Update instance bu id, partially."""
        return super().patch(*args, **kwargs)

    @swagger.operation(**invoice_product_delete_schema)
    @token_required()
    def delete(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Delete instance by id."""
        return super().delete(*args, **kwargs)


class InvoiceProductsRoute(ModelsRoute):
    """Operations with many InvoiceProducts instances and instance creation."""

    model = InvoiceProduct
    post_parser = invoice_product_parser
    model_fields = InvoiceProductFields.resource_fields

    @swagger.operation(**invoice_product_post_schema)
    @token_required()
    def post(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Create model instance."""
        return super().post(*args, **kwargs)

    @swagger.operation(**invoice_products_get_schema)
    @token_required()
    def get(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Get model instance list."""
        return super().get(*args, **kwargs)


class InvoiceRegistryRoute(Resource):
    """Invoice resistry information."""

    @swagger.operation(**invoice_registry_get_schema)
    @token_required()
    def get(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Get invoice registry list."""
        arguments = order_registry_parser.parse_args()
        return marshal(
            get_invoice_data(**arguments),
            InvoiceRegistryFields.resource_fields,
        )


class InvoicesProductsRoute(Resource):
    """Getting Invoice products list by invoice id."""

    @swagger.operation(**invoices_products_get_schema)
    @token_required()
    def get(
        self,
        invoice_id: int,
        *args: typing.Any,
        **kwargs: typing.Any,
    ) -> ResponseReturnValue:
        """Get Invoice products list by invoice id."""
        invoice_id = invoice_id_valid(invoice_id)
        return marshal(
            get_invoice_products_by_invoice_id(invoice_id),
            InvoicesProductsFields.resource_fields,
        )


class AgreementInvoicesRoute(Resource):
    """Get Agreement Invoices list by agreement id."""

    @swagger.operation(**agreement_invoice_products_get_schema)
    @token_required()
    def get(
        self,
        agreement_id: int,
        *args: typing.Any,
        **kwargs: typing.Any,
    ) -> ResponseReturnValue:
        """Get Invoices list by agreement id."""
        agreement_id = agreement_id_valid(agreement_id)
        return marshal(
            crud.read_many(Invoice, {"agreement_id": agreement_id}, rev=True),
            InvoiceFields.resource_fields,
        )


api.add_resource(InvoiceRoute, "/invoice/<instance_id>/")
api.add_resource(InvoicesRoute, "/invoice/")
api.add_resource(InvoiceProductRoute, "/invoice-product/<instance_id>/")
api.add_resource(InvoiceProductsRoute, "/invoice-product/")
api.add_resource(InvoiceRegistryRoute, "/invoice-registry/")
api.add_resource(InvoicesProductsRoute, "/invoice-products/<invoice_id>/")
api.add_resource(AgreementInvoicesRoute, "/invoices/<agreement_id>/")
