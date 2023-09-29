"""Routes for account apps."""
from flask_restful import Resource, fields, marshal, marshal_with
from flask_restful_swagger import swagger

from api import SaleInvoiceProduct, api
from api.apps.account.parsers import (
    account_parser,
    period_parser,
    product_leftovers_parser,
)
from api.apps.account.schemas import (
    income_for_period_schema,
    period_report_schema,
    process_sale_invoice_schema,
    product_leftovers_schema,
)
from api.apps.account.services import (
    create_tax_invoice_products,
    get_purchase_products_by_invoice_products,
    get_purchase_products_quantity_list,
    get_sale_invoice_products_by_period,
    get_sold_products,
    get_sold_products_for_period,
    get_tax_invoice_products_with_prices_data,
    prepare_tax_invoice_products,
    update_sale_invoice,
)
from api.apps.account.utils import (
    add_income_to_products,
    create_income_products_dict,
    get_product_leftovers_on_date,
)
from api.model_routes import token_required
from api.services import crud


@swagger.model
class PeriodReport:
    """PeriodReportRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "quantity": fields.String,
        "price": fields.String,
        "sale_invoice_name": fields.String,
        "created_at": fields.DateTime,
        "name": fields.String,
        "units": fields.String,
        "code": fields.String,
        "currency": fields.String,
    }


@swagger.model
class ProductLeftovers:
    """ProductLeftoversRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "name": fields.String,
        "units": fields.String,
        "currency": fields.String,
        "quantity": fields.Integer,
    }


@swagger.model
class IncomeForPeriod:
    """IncomeForPeriodRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "name": fields.String,
        "code": fields.String,
        "currency": fields.String,
        "product_type": fields.String,
        "income": fields.Integer,
    }


class ProcessSaleInvoiceRoute(Resource):
    """Operations with saling process."""

    @swagger.operation(**process_sale_invoice_schema)
    @token_required()
    def post(self, *args, **kwargs):
        """
        Approve saling and create tax invoice.

        Tax invoice will be created along with tax invoice products,
        also quantity products number in created tax_invoice_products
        quantity field will be subctructed from purchase_invoice_products
        left field. In case of enough amaount of purchase products all
        mentioned instances will be created and sale_invoice done field
        will be set to True, otherwise error with 409 code will be raised.
        """
        args = account_parser.parse_args()
        sale_invoice_id = args.get("sale_invoice_id")
        sale_invoice_products = crud.read_many(
            SaleInvoiceProduct, {"sale_invoice_id": sale_invoice_id}
        )
        purchase_products = get_purchase_products_by_invoice_products(
            sale_invoice_products
        )
        tax_invoice_products = prepare_tax_invoice_products(
            sale_invoice_products, purchase_products, sale_invoice_id
        )
        create_tax_invoice_products(tax_invoice_products, sale_invoice_id)
        update_sale_invoice(sale_invoice_id)

        return {"message": "Operation succussfully performed"}


class PeriodReportRoute(Resource):
    """Create period report."""

    @swagger.operation(**period_report_schema)
    @token_required()
    @marshal_with(PeriodReport.resource_fields)
    def post(self, *args, **kwargs):
        """
        Create period report.

        Period report will be evaluated on period from
        'date_from' to 'date_to' in args, list of sold
        products will be returned.
        Price field is given in cents.
        """
        args = period_parser.parse_args()
        return get_sale_invoice_products_by_period(args)


class ProductsLeftoversRoute(Resource):
    """Product leftovers to particular date."""

    @swagger.operation(**product_leftovers_schema)
    @token_required()
    def post(self, *args, **kwargs):
        """Create product leftovers report."""
        args = product_leftovers_parser.parse_args()
        purchase_products = marshal(
            get_purchase_products_quantity_list(args), ProductLeftovers.resource_fields
        )
        sold_products = get_sold_products(args)
        return get_product_leftovers_on_date(purchase_products, sold_products)


class IncomeForPeriodRoute(Resource):
    """Calculate income for given period."""

    @swagger.operation(**income_for_period_schema)
    @token_required()
    def post(self, *args, **kwargs):
        """
        Calculate income for given period.

        Income is field given in cents.
        """
        args = period_parser.parse_args()
        income_products_data = get_tax_invoice_products_with_prices_data(args)
        products = marshal(
            get_sold_products_for_period(args), IncomeForPeriod.resource_fields
        )
        income_dict = create_income_products_dict(income_products_data)
        return add_income_to_products(income_dict, products)


api.add_resource(ProcessSaleInvoiceRoute, "/account/process-sale-invoice/")
api.add_resource(PeriodReportRoute, "/account/sale-report/")
api.add_resource(ProductsLeftoversRoute, "/account/product-leftovers/")
api.add_resource(IncomeForPeriodRoute, "/account/income-for-period/")
