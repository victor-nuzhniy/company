"""Routes for purchase_specialized apps."""
import typing

from flask.typing import ResponseReturnValue
from flask_restful import Resource, marshal
from flask_restful_swagger import swagger

from api import api
from api.apps.invoice.validators import product_id_valid
from api.apps.purchase.validators import purchase_invoice_id_valid
from api.apps.purchase_specialized.parsers import purchase_registry_parser
from api.apps.purchase_specialized.schemas import (
    purchase_invoice_products_left_get_schema,
    purchase_invoices_products_get_schema,
    purchase_registry_get_schema,
)
from api.apps.purchase_specialized.services import (
    get_pur_inv_prod_by_prod_id_with_prod_left,
    get_purchase_invoice_data,
    get_purchase_invoice_products_by_purchase_id,
)
from api.apps.purchase_specialized.swagger_models import (
    PurchaseInvoiceProductsLeftFields,
    PurchaseInvoicesProductsFields,
    PurchaseRegistryFields,
)
from api.model_routes import token_required


class PurchaseRegistryRoute(Resource):
    """Purchase registry information."""

    @swagger.operation(**purchase_registry_get_schema)
    @token_required()
    def get(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Get purchase registry products list."""
        arguments = purchase_registry_parser.parse_args()
        return marshal(
            get_purchase_invoice_data(**arguments),
            PurchaseRegistryFields.resource_fields,
        )


class PurchaseInvoicesProductsRoute(Resource):
    """Getting PurchaseInvoices products list by purchase invoice id."""

    @swagger.operation(**purchase_invoices_products_get_schema)
    @token_required()
    def get(
        self,
        purchase_invoice_id: int,
        *args: typing.Any,
        **kwargs: typing.Any,
    ) -> ResponseReturnValue:
        """Get PurchaseInvoices products list by purchase invoice id."""
        purchase_invoice_id = purchase_invoice_id_valid(purchase_invoice_id)
        return marshal(
            get_purchase_invoice_products_by_purchase_id(purchase_invoice_id),
            PurchaseInvoicesProductsFields.resource_fields,
        )


class PurchaseInvoiceProductsLeftRoute(Resource):
    """Getting PurchaseInvoices products list with products_left > 0 and product_id."""

    @swagger.operation(**purchase_invoice_products_left_get_schema)
    @token_required()
    def get(
        self,
        product_id: int,
        *args: typing.Any,
        **kwargs: typing.Any,
    ) -> ResponseReturnValue:
        """Get PurchaseInvoice products list with products_left > 0 and product_id."""
        product_id = product_id_valid(product_id)
        return marshal(
            get_pur_inv_prod_by_prod_id_with_prod_left(product_id),
            PurchaseInvoiceProductsLeftFields.resource_fields,
        )


api.add_resource(PurchaseRegistryRoute, "/purchase-registry/")
api.add_resource(
    PurchaseInvoicesProductsRoute,
    "/purchase-invoice-products/<purchase_invoice_id>/",
)
api.add_resource(
    PurchaseInvoiceProductsLeftRoute,
    "/purchase-invoice-products/product/<product_id>/",
)
