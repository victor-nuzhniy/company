"""Parsers for product apps."""
from flask_restful import reqparse

from api.apps.invoice.validators import str_length_100
from api.apps.product.validators import product_type_id, str_length_15, str_length_200

product_parser = reqparse.RequestParser()
product_parser.add_argument("name", type=str_length_200, required=True)
product_parser.add_argument("code", type=str_length_100, required=True)
product_parser.add_argument("units", type=str_length_100, required=True)
product_parser.add_argument("currency", type=str_length_15, required=True)
product_parser.add_argument("price", type=int, required=True)
product_parser.add_argument("product_type_id", type=product_type_id, required=True)

product_patch_parser = reqparse.RequestParser()
product_patch_parser.add_argument("name", type=str_length_200, required=False)
product_patch_parser.add_argument("code", type=str_length_100, required=False)
product_patch_parser.add_argument("units", type=str_length_100, required=False)
product_patch_parser.add_argument("currency", type=str_length_15, required=False)
product_patch_parser.add_argument("price", type=int, required=False)
product_patch_parser.add_argument(
    "product_type_id", type=product_type_id, required=False
)


product_type_parser = reqparse.RequestParser()
product_type_parser.add_argument("name", type=str_length_100, required=True)

product_type_patch_parser = reqparse.RequestParser()
product_type_patch_parser.add_argument("name", type=str_length_100, required=False)
