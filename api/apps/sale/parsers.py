"""Parsers for sale apps."""
from flask_restful import reqparse
from flask_restful.inputs import boolean, datetime_from_iso8601

from api.apps.invoice.validators import invoice_id, product_id, str_length_100
from api.apps.sale.validators import sale_invoice_id

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

sale_invoice_product_parser = reqparse.RequestParser()
sale_invoice_product_parser.add_argument("product_id", type=product_id, required=True)
sale_invoice_product_parser.add_argument("quantity", type=int, required=True)
sale_invoice_product_parser.add_argument("price", type=int, required=True)
sale_invoice_product_parser.add_argument(
    "sale_invoice_id", type=sale_invoice_id, required=True
)

sale_invoice_product_patch_parser = reqparse.RequestParser()
sale_invoice_product_patch_parser.add_argument(
    "product_id", type=product_id, required=False
)
sale_invoice_product_patch_parser.add_argument("quantity", type=int, required=False)
sale_invoice_product_patch_parser.add_argument("price", type=int, required=False)
sale_invoice_product_patch_parser.add_argument(
    "sale_invoice_id", type=sale_invoice_id, required=False
)
