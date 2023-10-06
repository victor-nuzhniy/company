"""Parsers for purchase apps."""
from datetime import datetime

from flask_restful import reqparse

from api.apps.invoice.validators import agreement_id, product_id, str_length_100
from api.apps.purchase.validators import purchase_invoice_id

purchase_invoice_post_parser = reqparse.RequestParser()
purchase_invoice_post_parser.add_argument("name", type=str_length_100, required=True)
purchase_invoice_post_parser.add_argument(
    "agreement_id", type=agreement_id, required=True
)

purchase_invoice_put_parser = reqparse.RequestParser()
purchase_invoice_put_parser.add_argument("name", type=str_length_100, required=True)
purchase_invoice_put_parser.add_argument(
    "agreement_id", type=agreement_id, required=True
)
purchase_invoice_put_parser.add_argument(
    "created_at",
    type=lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S"),
    required=True,
)

purchase_invoice_patch_parser = reqparse.RequestParser()
purchase_invoice_patch_parser.add_argument("name", type=str_length_100, required=False)
purchase_invoice_patch_parser.add_argument(
    "agreement_id", type=agreement_id, required=False
)
purchase_invoice_patch_parser.add_argument(
    "created_at",
    type=lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S"),
    required=False,
)

purchase_invoice_product_parser = reqparse.RequestParser()
purchase_invoice_product_parser.add_argument(
    "product_id", type=product_id, required=True
)
purchase_invoice_product_parser.add_argument("quantity", type=int, required=True)
purchase_invoice_product_parser.add_argument("price", type=int, required=True)
purchase_invoice_product_parser.add_argument(
    "purchase_invoice_id", type=purchase_invoice_id, required=True
)
purchase_invoice_product_parser.add_argument("products_left", type=int, required=True)

purchase_invoice_product_patch_parser = reqparse.RequestParser()
purchase_invoice_product_patch_parser.add_argument(
    "product_id", type=product_id, required=False
)
purchase_invoice_product_patch_parser.add_argument("quantity", type=int, required=False)
purchase_invoice_product_patch_parser.add_argument("price", type=int, required=False)
purchase_invoice_product_patch_parser.add_argument(
    "purchase_invoice_id", type=purchase_invoice_id, required=False
)
purchase_invoice_product_patch_parser.add_argument(
    "products_left", type=int, required=False
)

purchase_registry_parser = reqparse.RequestParser()
purchase_registry_parser.add_argument(
    "offset", type=int, required=False, location="args"
)
purchase_registry_parser.add_argument(
    "limit", type=int, required=False, location="args"
)
