"""Routes for sale_specialized apps."""
import typing

from flask.typing import ResponseReturnValue
from flask_restful import Resource, marshal
from flask_restful_swagger import swagger

from api import api, model_routes
from api.apps.invoice.validators import agreement_id_valid
from api.apps.purchase_specialized.parsers import purchase_registry_parser
from api.apps.sale.swagger_models import SaleInvoiceFields
from api.apps.sale.validators import sale_invoice_id_valid
from api.apps.sale_specialized import schemas, services, swagger_models
from api.apps.tax.validators import tax_invoice_id_valid


class SaleRegistryRoute(Resource):
    """Sale registry information."""

    @swagger.operation(**schemas.sale_registry_get_schema)
    @model_routes.token_required()
    def get(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Get sale registry list."""
        arguments = purchase_registry_parser.parse_args()
        return marshal(
            services.get_sale_invoice_data(**arguments),
            swagger_models.SaleRegistryFields.resource_fields,
        )


class SaleInvoicesProductsRoute(Resource):
    """Getting SaleInvoice products list by sale invoice id."""

    @swagger.operation(**schemas.sale_invoices_products_get_schema)
    @model_routes.token_required()
    def get(
        self,
        sale_invoice_id: int,
        *args: typing.Any,
        **kwargs: typing.Any,
    ) -> ResponseReturnValue:
        """Get SaleInvoice products list by sale invoice id."""
        sale_invoice_id = sale_invoice_id_valid(sale_invoice_id)
        return marshal(
            services.get_sale_invoice_products_by_sale_invoice_id(sale_invoice_id),
            swagger_models.SaleInvoicesProductsFields.resourse_fields,
        )


class TaxSaleInvoiceProductsLeftRoute(Resource):
    """
    Getting SaleInvoice products list by sale invoice id.

    Products, included in tax invoice, will not be included in query.
    There are not products will be available from sale invoice with done True.
    """

    @swagger.operation(**schemas.tax_sale_invoices_products_left_get_schema)
    @model_routes.token_required()
    def get(
        self,
        sale_invoice_id: int,
        tax_invoice_id: int,
        *args: typing.Any,
        **kwargs: typing.Any,
    ) -> ResponseReturnValue:
        """Get SaleInvoice products list by sale invoice id and tax_invoice_id."""
        sale_invoice_id = sale_invoice_id_valid(sale_invoice_id)
        tax_invoice_id = tax_invoice_id_valid(tax_invoice_id)
        return marshal(
            services.get_tax_sale_invoice_products_left(
                int(sale_invoice_id),
                int(tax_invoice_id),
            ),
            swagger_models.SaleInvoicesProductsFields.resourse_fields,
        )


class AgreementSaleInvoicesRoute(Resource):
    """Getting SaleInvoice list by agreement id."""

    @swagger.operation(**schemas.agreement_sale_invoices_get_schema)
    @model_routes.token_required()
    def get(
        self,
        agreement_id: int,
        *args: typing.Any,
        **kwargs: typing.Any,
    ) -> ResponseReturnValue:
        """Get SaleInvoice list by agreement id."""
        agreement_id = agreement_id_valid(agreement_id)
        return marshal(
            services.get_sale_invoices_by_agreement_id(agreement_id),
            SaleInvoiceFields.resource_fields,
        )


api.add_resource(SaleRegistryRoute, "/sale-invoice-registry/")
api.add_resource(SaleInvoicesProductsRoute, "/sale-invoice-products/<sale_invoice_id>/")
api.add_resource(
    TaxSaleInvoiceProductsLeftRoute,
    "/sale-invoice-products/<sale_invoice_id>/<tax_invoice_id>/",
)
api.add_resource(AgreementSaleInvoicesRoute, "/agreement-sale-invoices/<agreement_id>/")
