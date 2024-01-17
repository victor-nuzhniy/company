"""Parsers for purchase apps."""
from datetime import datetime

from flask_restful import reqparse

from api.apps.invoice.validators import (
    agreement_id_valid,
    product_id_valid,
    str_hundred,
)
from api.apps.purchase.validators import purchase_invoice_id_valid

purchase_invoice_post_parser = reqparse.RequestParser()
purchase_invoice_post_parser.add_argument("name", type=str_hundred, required=True)
purchase_invoice_post_parser.add_argument(
    "agreement_id", type=agreement_id_valid, required=True,
)

purchase_invoice_put_parser = reqparse.RequestParser()
purchase_invoice_put_parser.add_argument("name", type=str_hundred, required=True)
purchase_invoice_put_parser.add_argument(
    "agreement_id", type=agreement_id_valid, required=True,
)
purchase_invoice_put_parser.add_argument(
    "created_at",
    type=lambda arg: datetime.strptime(arg, "%Y-%m-%d %H:%M:%S"),
    required=True,
)

purchase_invoice_patch_parser = reqparse.RequestParser()
purchase_invoice_patch_parser.add_argument("name", type=str_hundred, required=False)
purchase_invoice_patch_parser.add_argument(
    "agreement_id", type=agreement_id_valid, required=False,
)
purchase_invoice_patch_parser.add_argument(
    "created_at",
    type=lambda arg: datetime.strptime(arg, "%Y-%m-%d %H:%M:%S"),
    required=False,
)

purchase_invoice_product_parser = reqparse.RequestParser()
purchase_invoice_product_parser.add_argument(
    "product_id", type=product_id_valid, required=True,
)
purchase_invoice_product_parser.add_argument("quantity", type=int, required=True)
purchase_invoice_product_parser.add_argument("price", type=int, required=True)
purchase_invoice_product_parser.add_argument(
    "purchase_invoice_id", type=purchase_invoice_id_valid, required=True,
)
purchase_invoice_product_parser.add_argument("products_left", type=int, required=True)

purchase_invoice_product_patch_parser = reqparse.RequestParser()
purchase_invoice_product_patch_parser.add_argument(
    "product_id", type=product_id_valid, required=False,
)
purchase_invoice_product_patch_parser.add_argument("quantity", type=int, required=False)
purchase_invoice_product_patch_parser.add_argument("price", type=int, required=False)
purchase_invoice_product_patch_parser.add_argument(
    "purchase_invoice_id", type=purchase_invoice_id_valid, required=False,
)
purchase_invoice_product_patch_parser.add_argument(
    "products_left", type=int, required=False,
)
