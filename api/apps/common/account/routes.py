"""Routes for account apps."""
import typing

from flask import abort
from flask.typing import ResponseReturnValue
from flask_restful import Resource, marshal, marshal_with
from flask_restful_swagger import swagger

from api import SaleInvoice, SaleInvoiceProduct, api
from api.apps.common.account.account_utilities import (
    add_income_to_products,
    create_income_products_dict,
    get_product_leftovers_on_date,
)
from api.apps.common.account.parsers import (
    account_parser,
    period_parser,
    product_leftovers_parser,
)
from api.apps.common.account.schemas import (
    income_for_period_schema,
    period_report_schema,
    process_sale_invoice_schema,
    product_leftovers_schema,
)
from api.apps.common.account.services import (
    account_queries,
    create_tax_invoice_products,
    prepare_tax_invoice_products,
)
from api.apps.common.account.swagger_models import (
    IncomeForPeriod,
    PeriodReport,
    ProductLeftovers,
)
from api.common import model_routes, services


class ProcessSaleInvoiceRoute(Resource):
    """Operations with saling process."""

    @swagger.operation(**process_sale_invoice_schema)
    @model_routes.token_required()
    def post(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """
        Approve saling and create base base.

        Tax base will be created along with base base products,
        also quantity products number in created tax_invoice_products
        quantity field will be subctructed from purchase_invoice_products
        left field. In case of enough amaount of base products all
        mentioned instances will be created and sale_invoice done field
        will be set to True, otherwise error with 409 code will be raised.
        """
        sale_invoice_id = account_parser.parse_args().get("sale_invoice_id")
        sale_invoice = services.crud.read(SaleInvoice, {"id": sale_invoice_id})
        if sale_invoice and sale_invoice.done:
            abort(
                406,
                "Sale_invoice with id {id} is already done!".format(id=sale_invoice_id),
            )
        sale_invoice_products = services.crud.read_many(
            SaleInvoiceProduct,
            {"sale_invoice_id": sale_invoice_id},
        )
        purchase_products = account_queries.get_purchase_products_by_invoice_products(
            sale_invoice_products,
        )
        tax_invoice_products = prepare_tax_invoice_products(
            sale_invoice_products,
            purchase_products,
            sale_invoice_id,
        )
        create_tax_invoice_products(tax_invoice_products, sale_invoice_id)
        account_queries.update_sale_invoice(sale_invoice_id)

        return {"message": "Operation successfully performed"}


class PeriodReportRoute(Resource):
    """Create period report."""

    @swagger.operation(**period_report_schema)
    @model_routes.token_required()
    @marshal_with(PeriodReport.resource_fields)
    def post(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """
        Create period report.

        Period report will be evaluated on period from
        'date_from' to 'date_to' in args, list of sold
        products will be returned.
        Price field is given in cents.
        """
        arguments = period_parser.parse_args()
        return account_queries.get_sale_invoice_products_by_period(arguments)


class ProductsLeftoversRoute(Resource):
    """Product leftovers to particular date."""

    @swagger.operation(**product_leftovers_schema)
    @model_routes.token_required()
    def post(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Create base leftovers report."""
        arguments = product_leftovers_parser.parse_args()
        purchase_products = marshal(
            account_queries.get_purchase_products_quantity_list(arguments),
            ProductLeftovers.resource_fields,
        )
        sold_products = account_queries.get_sold_products(arguments)
        return get_product_leftovers_on_date(purchase_products, sold_products)


class IncomeForPeriodRoute(Resource):
    """Calculate income for given period."""

    @swagger.operation(**income_for_period_schema)
    @model_routes.token_required()
    def post(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """
        Calculate income for given period.

        Income is field given in cents.
        """
        arguments = period_parser.parse_args()
        income_products = account_queries.get_tax_invoice_products_with_prices_data(
            arguments,
        )
        products = marshal(
            account_queries.get_sold_products_for_period(arguments),
            IncomeForPeriod.resource_fields,
        )
        income_dict = create_income_products_dict(income_products)
        return add_income_to_products(income_dict, products)


api.add_resource(ProcessSaleInvoiceRoute, "/account/process-base-base/")
api.add_resource(PeriodReportRoute, "/account/base-report/")
api.add_resource(ProductsLeftoversRoute, "/account/base-leftovers/")
api.add_resource(IncomeForPeriodRoute, "/account/income-for-period/")
