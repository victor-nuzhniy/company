"""Routes for tax special apps."""
import typing

from flask.typing import ResponseReturnValue
from flask_restful import Resource, marshal
from flask_restful_swagger import swagger

from api.app import api
from api.apps.purchase.special.parsers import purchase_registry_parser
from api.apps.tax.base import parsers, swagger_models
from api.apps.tax.base.validators import (
    tax_invoice_id_valid,
    tax_invoice_product_id_valid,
)
from api.apps.tax.special.schemas import (
    tax_inv_prod_with_add_prod_left_del_schema,
    tax_inv_with_purch_add_prod_left_del_schema,
    tax_invoice_product_create_schema,
    tax_invoices_products_get_schema,
    tax_registry_get_schema,
)
from api.apps.tax.special.services import (
    create_tax_invoice_products,
    delete_tax_invoice,
    delete_tax_invoice_products,
    get_tax_data,
    get_tax_invoice_products_by_tax_invoice_id,
)
from api.apps.tax.special.swagger_models import (
    TaxInvoicesProductsFields,
    TaxRegistryFields,
)
from api.common import model_routes


class TaxRegistryRoute(Resource):
    """Tax registry information."""

    @swagger.operation(**tax_registry_get_schema)
    @model_routes.token_required()
    def get(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Get base registry list."""
        arguments = purchase_registry_parser.parse_args()
        return marshal(
            get_tax_data(**arguments),
            TaxRegistryFields.resource_fields,
        )


class TaxInvoicesProductsRoute(Resource):
    """Getting TaxInvoice products list by base base id."""

    @swagger.operation(**tax_invoices_products_get_schema)
    @model_routes.token_required()
    def get(
        self,
        tax_invoice_id: int,
        *args: typing.Any,
        **kwargs: typing.Any,
    ) -> ResponseReturnValue:
        """Get TaxInvoice products list by base base id."""
        tax_invoice_id = tax_invoice_id_valid(tax_invoice_id)
        return marshal(
            get_tax_invoice_products_by_tax_invoice_id(tax_invoice_id),
            TaxInvoicesProductsFields.resource_fields,
        )


class TaxInvoiceProductCreateRoute(Resource):
    """Create TaxInvoiceProduct with subtracting base products_left field."""

    @swagger.operation(**tax_invoice_product_create_schema)
    @model_routes.token_required(is_admin=True)
    def post(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Create TaxInvoiceProduct with subtracting purhcase products_left field."""
        arguments = parsers.tax_invoice_product_parser.parse_args()
        return marshal(
            create_tax_invoice_products(
                **arguments,
            ),
            swagger_models.TaxInvoiceProductFields.resource_fields,
        )


class TaxInvoiceProductDeleteRoute(Resource):
    """Delete TaxInvoiceProduct with adding base products_left field."""

    @swagger.operation(**tax_inv_prod_with_add_prod_left_del_schema)
    @model_routes.token_required(is_admin=True)
    def delete(
        self,
        tax_invoice_product_id: int,
        *args: typing.Any,
        **kwargs: typing.Any,
    ) -> ResponseReturnValue:
        """Delete TaxInvoiceProduct with adding base products_left field."""
        tax_invoice_product_id = tax_invoice_product_id_valid(tax_invoice_product_id)
        delete_tax_invoice_products(
            tax_invoice_product_id,
        )
        return {"message": "Tax base base was successfully deleted."}


class TaxInvoiceDeleteRoute(Resource):
    """Delete TaxInvoice with adding base products_left fields."""

    @swagger.operation(**tax_inv_with_purch_add_prod_left_del_schema)
    @model_routes.token_required(is_admin=True)
    def delete(
        self,
        tax_invoice_id: int,
        *args: typing.Any,
        **kwargs: typing.Any,
    ) -> ResponseReturnValue:
        """Delete TaxInvoice with adding base products_left fields."""
        tax_invoice_id = tax_invoice_id_valid(tax_invoice_id)
        delete_tax_invoice(tax_invoice_id)
        return {
            "message": "TaxInvoice with id {id} was successfully deleted.".format(
                id=tax_invoice_id,
            ),
        }


api.add_resource(TaxRegistryRoute, "/tax-registry/")
api.add_resource(TaxInvoicesProductsRoute, "/tax-invoice-products/<tax_invoice_id>/")
api.add_resource(TaxInvoiceProductCreateRoute, "/tax-invoice-product-create/")
api.add_resource(
    TaxInvoiceProductDeleteRoute,
    "/tax-invoice-product-delete/<tax_invoice_product_id>/",
)
api.add_resource(TaxInvoiceDeleteRoute, "/tax-invoice-delete/<tax_invoice_id>/")
