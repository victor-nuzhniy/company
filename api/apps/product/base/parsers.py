"""Parsers for product base apps."""
from flask_restful import reqparse

from api.apps.invoice.base.validators import str_hundred
from api.apps.product.base.validators import (
    product_type_id,
    str_fifteen,
    str_two_hundred,
)

product_parser = reqparse.RequestParser()
product_parser.add_argument("name", type=str_two_hundred, required=True)
product_parser.add_argument("code", type=str_hundred, required=True)
product_parser.add_argument("units", type=str_hundred, required=True)
product_parser.add_argument("currency", type=str_fifteen, required=True)
product_parser.add_argument("price", type=int, required=True)
product_parser.add_argument("product_type_id", type=product_type_id, required=True)

product_patch_parser = reqparse.RequestParser()
product_patch_parser.add_argument("name", type=str_two_hundred, required=False)
product_patch_parser.add_argument("code", type=str_hundred, required=False)
product_patch_parser.add_argument("units", type=str_hundred, required=False)
product_patch_parser.add_argument("currency", type=str_fifteen, required=False)
product_patch_parser.add_argument("price", type=int, required=False)
product_patch_parser.add_argument(
    "product_type_id",
    type=product_type_id,
    required=False,
)


product_type_parser = reqparse.RequestParser()
product_type_parser.add_argument("name", type=str_hundred, required=True)

product_type_patch_parser = reqparse.RequestParser()
product_type_patch_parser.add_argument("name", type=str_hundred, required=False)
