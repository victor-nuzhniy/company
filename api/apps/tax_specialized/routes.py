"""Routes for tax_specialized apps."""
import typing

from flask.typing import ResponseReturnValue
from flask_restful import Resource, marshal
from flask_restful_swagger import swagger

from api import api, model_routes
from api.apps.purchase_specialized.parsers import purchase_registry_parser
from api.apps.tax.parsers import tax_invoice_product_parser
from api.apps.tax.swagger_models import TaxInvoiceProductFields
from api.apps.tax.validators import tax_invoice_id_valid, tax_invoice_product_id_valid
from api.apps.tax_specialized.schemas import (
    tax_inv_prod_with_add_prod_left_del_schema,
    tax_inv_with_purch_add_prod_left_del_schema,
    tax_invoice_product_create_schema,
    tax_invoices_products_get_schema,
    tax_registry_get_schema,
)
from api.apps.tax_specialized.services import (
    create_tax_invoice_products,
    delete_tax_invoice,
    delete_tax_invoice_products,
    get_tax_data,
    get_tax_invoice_products_by_tax_invoice_id,
)
from api.apps.tax_specialized.swagger_models import (
    TaxInvoicesProductsFields,
    TaxRegistryFields,
)


class TaxRegistryRoute(Resource):
    """Tax registry information."""

    @swagger.operation(**tax_registry_get_schema)
    @model_routes.token_required()
    def get(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Get tax registry list."""
        arguments = purchase_registry_parser.parse_args()
        return marshal(
            get_tax_data(**arguments),
            TaxRegistryFields.resource_fields,
        )


class TaxInvoicesProductsRoute(Resource):
    """Getting TaxInvoice products list by tax invoice id."""

    @swagger.operation(**tax_invoices_products_get_schema)
    @model_routes.token_required()
    def get(
        self,
        tax_invoice_id: int,
        *args: typing.Any,
        **kwargs: typing.Any,
    ) -> ResponseReturnValue:
        """Get TaxInvoice products list by tax invoice id."""
        tax_invoice_id = tax_invoice_id_valid(tax_invoice_id)
        return marshal(
            get_tax_invoice_products_by_tax_invoice_id(tax_invoice_id),
            TaxInvoicesProductsFields.resource_fields,
        )


class TaxInvoiceProductCreateRoute(Resource):
    """Create TaxInvoiceProduct with subtracting purchase products_left field."""

    @swagger.operation(**tax_invoice_product_create_schema)
    @model_routes.token_required(is_admin=True)
    def post(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Create TaxInvoiceProduct with subtracting purhcase products_left field."""
        arguments = tax_invoice_product_parser.parse_args()
        return marshal(
            create_tax_invoice_products(
                **arguments,
            ),
            TaxInvoiceProductFields.resource_fields,
        )


class TaxInvoiceProductDeleteRoute(Resource):
    """Delete TaxInvoiceProduct with adding purchase products_left field."""

    @swagger.operation(**tax_inv_prod_with_add_prod_left_del_schema)
    @model_routes.token_required(is_admin=True)
    def delete(
        self,
        tax_invoice_product_id: int,
        *args: typing.Any,
        **kwargs: typing.Any,
    ) -> ResponseReturnValue:
        """Delete TaxInvoiceProduct with adding purchase products_left field."""
        tax_invoice_product_id = tax_invoice_product_id_valid(tax_invoice_product_id)
        delete_tax_invoice_products(
            tax_invoice_product_id,
        )
        return {"message": "Tax invoice product was successfully deleted."}


class TaxInvoiceDeleteRoute(Resource):
    """Delete TaxInvoice with adding purchase products_left fields."""

    @swagger.operation(**tax_inv_with_purch_add_prod_left_del_schema)
    @model_routes.token_required(is_admin=True)
    def delete(
        self,
        tax_invoice_id: int,
        *args: typing.Any,
        **kwargs: typing.Any,
    ) -> ResponseReturnValue:
        """Delete TaxInvoice with adding purchase products_left fields."""
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
