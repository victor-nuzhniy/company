"""Parsers for invoice apps."""
from flask_restful import reqparse
from flask_restful.inputs import boolean, datetime_from_iso8601

from api.apps.invoice.validators import (
    agreement_id,
    invoice_id,
    order_id,
    product_id,
    sale_invoice_id,
    str_length_100,
)

invoice_parser = reqparse.RequestParser()
invoice_parser.add_argument("name", required=True)
invoice_parser.add_argument("order_id", type=order_id, required=True)
invoice_parser.add_argument("agreement_id", type=agreement_id, required=True)

invoice_patch_parser = reqparse.RequestParser()
invoice_parser.add_argument("name", required=False)
invoice_patch_parser.add_argument("order_id", type=order_id, required=False)
invoice_patch_parser.add_argument(
    "created_at", type=datetime_from_iso8601, required=False
)
invoice_patch_parser.add_argument("paid", type=boolean, required=False)
invoice_patch_parser.add_argument("agreement_id", type=agreement_id, required=False)

invoice_products_parser = reqparse.RequestParser()
invoice_products_parser.add_argument("product_id", type=product_id, required=True)
invoice_products_parser.add_argument("quantity", type=int, required=True)
invoice_products_parser.add_argument("price", type=int, required=True)
invoice_products_parser.add_argument("invoice_id", type=invoice_id, required=True)

invoice_products_patch_parser = reqparse.RequestParser()
invoice_products_patch_parser.add_argument(
    "product_id", type=product_id, required=False
)
invoice_products_patch_parser.add_argument("quantity", type=int, required=False)
invoice_products_patch_parser.add_argument("price", type=int, required=False)
invoice_products_patch_parser.add_argument(
    "invoice_id", type=invoice_id, required=False
)

sale_invoice_parser = reqparse.RequestParser()
sale_invoice_parser.add_argument("name", type=str_length_100, required=True)
sale_invoice_parser.add_argument("invoice_id", type=invoice_id, required=True)

sale_invoice_patch_parser = reqparse.RequestParser()
sale_invoice_patch_parser.add_argument("name", type=str_length_100, required=False)
sale_invoice_patch_parser.add_argument("invoice_id", type=invoice_id, required=False)
sale_invoice_patch_parser.add_argument(
    "created_at", type=datetime_from_iso8601, required=False
)
sale_invoice_patch_parser.add_argument("done", type=boolean, required=False)

account_parser = reqparse.RequestParser()
account_parser.add_argument("sale_invoice_id", type=sale_invoice_id, required=True)
