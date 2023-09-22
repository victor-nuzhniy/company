"""Routes for account apps."""
from flask_restful import Resource

from api import SaleInvoiceProduct, api
from api.apps.account.parsers import account_parser
from api.apps.account.services import (
    create_tax_invoice_products,
    get_purchase_products_by_invoice_products,
    prepare_tax_invoice_products,
    update_sale_invoice,
)
from api.services import crud


class Account(Resource):
    """Operations with saling process."""

    def post(self):
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


api.add_resource(Account, "/accounting-entry/")
