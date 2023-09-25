"""Routes for account apps."""
from flask_restful import Resource, fields, marshal, marshal_with

from api import SaleInvoiceProduct, api
from api.apps.account.parsers import (
    account_parser,
    period_parser,
    product_leftovers_parser,
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
from api.services import crud

period_report_fields = {
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


product_leftovers_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "units": fields.String,
    "currency": fields.String,
    "quantity": fields.Integer,
}

product_income_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "code": fields.String,
    "currency": fields.String,
    "product_type": fields.String,
}


class ProcessSaleInvoiceRoute(Resource):
    """Operations with saling process."""

    def post(self, *args, **kwargs):
        """Approve saling and create tax invoice."""
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

    @marshal_with(period_report_fields)
    def post(self, *args, **kwargs):
        """Create period report."""
        args = period_parser.parse_args()
        return get_sale_invoice_products_by_period(args)


class ProductsLeftoversRoute(Resource):
    """Product leftovers to particular date."""

    def post(self, *args, **kwargs):
        """Create product leftovers report."""
        args = product_leftovers_parser.parse_args()
        purchase_products = marshal(
            get_purchase_products_quantity_list(args), product_leftovers_fields
        )
        sold_products = get_sold_products(args)
        return get_product_leftovers_on_date(purchase_products, sold_products)


class IncomeForPeriod(Resource):
    """Calculate income for given period."""

    def post(self, *args, **kwargs):
        """Calculate income for given period."""
        args = period_parser.parse_args()
        income_products_data = get_tax_invoice_products_with_prices_data(args)
        products = marshal(get_sold_products_for_period(args), product_income_fields)
        income_dict = create_income_products_dict(income_products_data)
        return add_income_to_products(income_dict, products)


api.add_resource(ProcessSaleInvoiceRoute, "/process-sale-invoice/")
api.add_resource(PeriodReportRoute, "/sale-report/")
api.add_resource(ProductsLeftoversRoute, "/product-leftovers/")
api.add_resource(IncomeForPeriod, "/income-for-period/")
