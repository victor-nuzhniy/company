"""Parsers for tax apps."""
from flask_restful import reqparse
from flask_restful.inputs import datetime_from_iso8601

from api.apps.invoice.validators import invoice_id, str_length_100
from api.apps.tax.validators import (
    purchase_invoice_products_id,
    sale_invoice_products_id,
    tax_invoice_id,
)

tax_invoice_post_parser = reqparse.RequestParser()
tax_invoice_post_parser.add_argument("name", type=str_length_100, required=True)
tax_invoice_post_parser.add_argument("sale_invoice_id", type=invoice_id, required=True)

tax_invoice_put_parser = reqparse.RequestParser()
tax_invoice_put_parser.add_argument("name", type=str_length_100, required=True)
tax_invoice_put_parser.add_argument("sale_invoice_id", type=invoice_id, required=True)
tax_invoice_put_parser.add_argument(
    "created_at", type=datetime_from_iso8601, required=True
)

tax_invoice_patch_parser = reqparse.RequestParser()
tax_invoice_patch_parser.add_argument("name", type=str_length_100, required=False)
tax_invoice_patch_parser.add_argument(
    "sale_invoice_id", type=invoice_id, required=False
)
tax_invoice_patch_parser.add_argument(
    "created_at", type=datetime_from_iso8601, required=False
)

tax_invoice_product_parser = reqparse.RequestParser()
tax_invoice_product_parser.add_argument(
    "tax_invoice_id", type=tax_invoice_id, required=True
)
tax_invoice_product_parser.add_argument(
    "sale_invoice_product_id", type=sale_invoice_products_id, required=True
)
tax_invoice_product_parser.add_argument(
    "purchase_invoice_product_id", type=purchase_invoice_products_id, required=True
)
tax_invoice_product_parser.add_argument("quantity", type=int, required=True)

tax_invoice_product_patch_parser = reqparse.RequestParser()
tax_invoice_product_patch_parser.add_argument(
    "tax_invoice_id", type=tax_invoice_id, required=False
)
tax_invoice_product_patch_parser.add_argument(
    "sale_invoice_product_id", type=sale_invoice_products_id, required=False
)
tax_invoice_product_patch_parser.add_argument(
    "purchase_invoice_product_id", type=purchase_invoice_products_id, required=False
)
tax_invoice_product_patch_parser.add_argument("quantity", type=int, required=False)
