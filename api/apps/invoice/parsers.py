"""Parsers for invoice apps."""
from datetime import datetime

from flask_restful import reqparse
from flask_restful.inputs import boolean

from api.apps.invoice.validators import (
    agreement_id,
    invoice_id,
    order_id,
    product_id,
    str_length_100,
)

invoice_post_parser = reqparse.RequestParser()
invoice_post_parser.add_argument("name", type=str_length_100, required=True)
invoice_post_parser.add_argument("order_id", type=order_id, required=True)
invoice_post_parser.add_argument("agreement_id", type=agreement_id, required=True)

invoice_put_parser = reqparse.RequestParser()
invoice_put_parser.add_argument("name", type=str_length_100, required=True)
invoice_put_parser.add_argument("order_id", type=order_id, required=True)
invoice_put_parser.add_argument(
    "created_at",
    type=lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S"),
    required=True,
)
invoice_put_parser.add_argument("paid", type=boolean, required=True)
invoice_put_parser.add_argument("agreement_id", type=agreement_id, required=True)


invoice_patch_parser = reqparse.RequestParser()
invoice_patch_parser.add_argument("name", type=str_length_100, required=False)
invoice_patch_parser.add_argument("order_id", type=order_id, required=False)
invoice_patch_parser.add_argument(
    "created_at",
    type=lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S"),
    required=False,
)
invoice_patch_parser.add_argument("paid", type=boolean, required=False)
invoice_patch_parser.add_argument("agreement_id", type=agreement_id, required=False)

invoice_product_parser = reqparse.RequestParser()
invoice_product_parser.add_argument("product_id", type=product_id, required=True)
invoice_product_parser.add_argument("quantity", type=int, required=True)
invoice_product_parser.add_argument("price", type=int, required=True)
invoice_product_parser.add_argument("invoice_id", type=invoice_id, required=True)

invoice_product_patch_parser = reqparse.RequestParser()
invoice_product_patch_parser.add_argument("product_id", type=product_id, required=False)
invoice_product_patch_parser.add_argument("quantity", type=int, required=False)
invoice_product_patch_parser.add_argument("price", type=int, required=False)
invoice_product_patch_parser.add_argument("invoice_id", type=invoice_id, required=False)
