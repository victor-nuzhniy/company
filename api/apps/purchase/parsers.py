"""Parsers for purchase apps."""
from flask_restful import reqparse
from flask_restful.inputs import datetime_from_iso8601

from api.apps.invoice.validators import agreement_id, product_id, str_length_100
from api.apps.purchase.validators import purchase_invoice_id

purchase_invoice_parser = reqparse.RequestParser()
purchase_invoice_parser.add_argument("name", type=str_length_100, required=True)
purchase_invoice_parser.add_argument("agreement_id", type=agreement_id, required=True)

purchase_invoice_patch_parser = reqparse.RequestParser()
purchase_invoice_patch_parser.add_argument("name", type=str_length_100, required=False)
purchase_invoice_patch_parser.add_argument(
    "agreement_id", type=agreement_id, required=False
)
purchase_invoice_patch_parser.add_argument(
    "created_at", type=datetime_from_iso8601, required=False
)

purchase_invoice_products_parser = reqparse.RequestParser()
purchase_invoice_products_parser.add_argument(
    "product_id", type=product_id, required=True
)
purchase_invoice_products_parser.add_argument("quantity", type=int, required=True)
purchase_invoice_products_parser.add_argument("price", type=int, required=True)
purchase_invoice_products_parser.add_argument(
    "purchase_invoice_id", type=purchase_invoice_id, required=True
)
purchase_invoice_products_parser.add_argument("products_left", type=int, required=True)

purchase_invoice_products_patch_parser = reqparse.RequestParser()
purchase_invoice_products_patch_parser.add_argument(
    "product_id", type=product_id, required=False
)
purchase_invoice_products_patch_parser.add_argument(
    "quantity", type=int, required=False
)
purchase_invoice_products_patch_parser.add_argument("price", type=int, required=False)
purchase_invoice_products_patch_parser.add_argument(
    "purchase_invoice_id", type=purchase_invoice_id, required=False
)
purchase_invoice_products_patch_parser.add_argument(
    "products_left", type=int, required=False
)