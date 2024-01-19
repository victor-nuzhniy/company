"""Parsers for tax base apps."""
from datetime import datetime

from flask_restful import reqparse

from api.apps.invoice.base.validators import str_hundred
from api.apps.sale.base.validators import sale_invoice_id_valid
from api.apps.tax.base.validators import (
    purchase_invoice_products_id_valid,
    sale_invoice_products_id_valid,
    tax_invoice_id_valid,
)

tax_invoice_post_parser = reqparse.RequestParser()
tax_invoice_post_parser.add_argument("name", type=str_hundred, required=True)
tax_invoice_post_parser.add_argument(
    "sale_invoice_id",
    type=sale_invoice_id_valid,
    required=True,
)

tax_invoice_put_parser = reqparse.RequestParser()
tax_invoice_put_parser.add_argument("name", type=str_hundred, required=True)
tax_invoice_put_parser.add_argument(
    "sale_invoice_id",
    type=sale_invoice_id_valid,
    required=True,
)
tax_invoice_put_parser.add_argument(
    "created_at",
    type=lambda arg: datetime.strptime(arg, "%Y-%m-%d %H:%M:%S"),
    required=True,
)

tax_invoice_patch_parser = reqparse.RequestParser()
tax_invoice_patch_parser.add_argument("name", type=str_hundred, required=False)
tax_invoice_patch_parser.add_argument(
    "sale_invoice_id",
    type=sale_invoice_id_valid,
    required=False,
)
tax_invoice_patch_parser.add_argument(
    "created_at",
    type=lambda arg: datetime.strptime(arg, "%Y-%m-%d %H:%M:%S"),
    required=False,
)

tax_invoice_product_parser = reqparse.RequestParser()
tax_invoice_product_parser.add_argument(
    "tax_invoice_id",
    type=tax_invoice_id_valid,
    required=True,
)
tax_invoice_product_parser.add_argument(
    "sale_invoice_product_id",
    type=sale_invoice_products_id_valid,
    required=True,
)
tax_invoice_product_parser.add_argument(
    "purchase_invoice_product_id",
    type=purchase_invoice_products_id_valid,
    required=True,
)
tax_invoice_product_parser.add_argument("quantity", type=int, required=True)

tax_invoice_product_patch_parser = reqparse.RequestParser()
tax_invoice_product_patch_parser.add_argument(
    "tax_invoice_id",
    type=tax_invoice_id_valid,
    required=False,
)
tax_invoice_product_patch_parser.add_argument(
    "sale_invoice_product_id",
    type=sale_invoice_products_id_valid,
    required=False,
)
tax_invoice_product_patch_parser.add_argument(
    "purchase_invoice_product_id",
    type=purchase_invoice_products_id_valid,
    required=False,
)
tax_invoice_product_patch_parser.add_argument("quantity", type=int, required=False)
