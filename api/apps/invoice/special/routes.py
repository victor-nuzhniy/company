"""Routes for invoice special apps."""
import typing

from flask.typing import ResponseReturnValue
from flask_restful import Resource, marshal
from flask_restful_swagger import swagger

from api import Invoice, api
from api.apps.invoice.base.parsers import order_registry_parser
from api.apps.invoice.base.swagger_models import InvoiceFields
from api.apps.invoice.base.validators import agreement_id_valid, invoice_id_valid
from api.apps.invoice.special.schemas import (
    agreement_invoice_products_get_schema,
    invoice_registry_get_schema,
    invoices_products_get_schema,
)
from api.apps.invoice.special.services import (
    get_invoice_data,
    get_invoice_products_by_invoice_id,
)
from api.apps.invoice.special.swagger_models import (
    InvoiceRegistryFields,
    InvoicesProductsFields,
)
from api.common import model_routes, services


class InvoiceRegistryRoute(Resource):
    """Invoice resistry information."""

    @swagger.operation(**invoice_registry_get_schema)
    @model_routes.token_required()
    def get(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Get base registry list."""
        arguments = order_registry_parser.parse_args()
        return marshal(
            get_invoice_data(**arguments),
            InvoiceRegistryFields.resource_fields,
        )


class InvoicesProductsRoute(Resource):
    """Getting Invoice products list by base id."""

    @swagger.operation(**invoices_products_get_schema)
    @model_routes.token_required()
    def get(
        self,
        invoice_id: int,
        *args: typing.Any,
        **kwargs: typing.Any,
    ) -> ResponseReturnValue:
        """Get Invoice products list by base id."""
        invoice_id = invoice_id_valid(invoice_id)
        return marshal(
            get_invoice_products_by_invoice_id(invoice_id),
            InvoicesProductsFields.resource_fields,
        )


class AgreementInvoicesRoute(Resource):
    """Get Agreement Invoices list by agreement id."""

    @swagger.operation(**agreement_invoice_products_get_schema)
    @model_routes.token_required()
    def get(
        self,
        agreement_id: int,
        *args: typing.Any,
        **kwargs: typing.Any,
    ) -> ResponseReturnValue:
        """Get Invoices list by agreement id."""
        agreement_id = agreement_id_valid(agreement_id)
        return marshal(
            services.crud.read_many(Invoice, {"agreement_id": agreement_id}, rev=True),
            InvoiceFields.resource_fields,
        )


api.add_resource(InvoiceRegistryRoute, "/invoice-registry/")
api.add_resource(InvoicesProductsRoute, "/invoice-products/<invoice_id>/")
api.add_resource(AgreementInvoicesRoute, "/invoices/<agreement_id>/")
