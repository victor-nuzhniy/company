"""Routes for account apps."""
from flask_restful import Resource

from api import InvoiceProducts, api
from api.apps.account.parsers import account_parser
from api.apps.account.services import (
    create_tax_invoice_products,
    get_purchase_products_by_invoice_products,
    prepare_tax_invoice_products,
)
from api.services import crud


class Account(Resource):
    """Operations with saling process."""

    def post(self):
        """Approve saling and create tax invoice."""
        args = account_parser.parse_args()
        invoice_id = args.get("invoice_id")
        invoice_products = crud.read_many(InvoiceProducts, {"invoice_id": invoice_id})
        purchase_products = get_purchase_products_by_invoice_products(invoice_products)
        tax_invoice_products = prepare_tax_invoice_products(
            invoice_products, purchase_products, invoice_id
        )
        create_tax_invoice_products(tax_invoice_products, invoice_id)

        return {"message": "Operation succussfully performed"}


api.add_resource(Account, "/accounting-entry/")
