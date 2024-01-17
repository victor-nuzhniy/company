"""Parsers for invoice apps."""
from datetime import datetime

from flask_restful import reqparse
from flask_restful.inputs import boolean

from api.apps.invoice.validators import (
    agreement_id_valid,
    invoice_id_valid,
    order_id_valid,
    product_id_valid,
    str_hundred,
)
from api.apps.order_specialized.parsers import order_registry_parser as order_parser

order_registry_parser = order_parser

invoice_post_parser = reqparse.RequestParser()
invoice_post_parser.add_argument("name", type=str_hundred, required=True)
invoice_post_parser.add_argument("order_id", type=order_id_valid, required=True)
invoice_post_parser.add_argument("agreement_id", type=agreement_id_valid, required=True)

invoice_put_parser = reqparse.RequestParser()
invoice_put_parser.add_argument("name", type=str_hundred, required=True)
invoice_put_parser.add_argument("order_id", type=order_id_valid, required=True)
invoice_put_parser.add_argument(
    "created_at",
    type=lambda arg: datetime.strptime(arg, "%Y-%m-%d %H:%M:%S"),
    required=True,
)
invoice_put_parser.add_argument("paid", type=boolean, required=True)
invoice_put_parser.add_argument("agreement_id", type=agreement_id_valid, required=True)


invoice_patch_parser = reqparse.RequestParser()
invoice_patch_parser.add_argument("name", type=str_hundred, required=False)
invoice_patch_parser.add_argument("order_id", type=order_id_valid, required=False)
invoice_patch_parser.add_argument(
    "created_at",
    type=lambda arg: datetime.strptime(arg, "%Y-%m-%d %H:%M:%S"),
    required=False,
)
invoice_patch_parser.add_argument("paid", type=boolean, required=False)
invoice_patch_parser.add_argument(
    "agreement_id",
    type=agreement_id_valid,
    required=False,
)

invoice_product_parser = reqparse.RequestParser()
invoice_product_parser.add_argument("product_id", type=product_id_valid, required=True)
invoice_product_parser.add_argument("quantity", type=int, required=True)
invoice_product_parser.add_argument("price", type=int, required=True)
invoice_product_parser.add_argument("invoice_id", type=invoice_id_valid, required=True)

invoice_product_patch_parser = reqparse.RequestParser()
invoice_product_patch_parser.add_argument(
    "product_id",
    type=product_id_valid,
    required=False,
)
invoice_product_patch_parser.add_argument("quantity", type=int, required=False)
invoice_product_patch_parser.add_argument("price", type=int, required=False)
invoice_product_patch_parser.add_argument(
    "invoice_id",
    type=invoice_id_valid,
    required=False,
)
