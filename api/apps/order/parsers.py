"""Parsers for order apps."""
from flask_restful import reqparse
from flask_restful.inputs import datetime_from_iso8601

from api.apps.counterparty.validators import counterparty_id
from api.apps.invoice.validators import order_id, product_id, str_length_100
from api.apps.order.validators import user_id

order_parser = reqparse.RequestParser()
order_parser.add_argument("user_id", type=user_id, required=True)
order_parser.add_argument("name", type=str_length_100, required=True)
order_parser.add_argument("customer_id", type=counterparty_id, required=True)

order_patch_parser = reqparse.RequestParser()
order_patch_parser.add_argument("user_id", type=user_id, required=False)
order_patch_parser.add_argument("name", type=str_length_100, required=False)
order_patch_parser.add_argument(
    "created_at", type=datetime_from_iso8601, required=False
)
order_patch_parser.add_argument("customer_id", type=counterparty_id, required=False)


order_products_parser = reqparse.RequestParser()
order_products_parser.add_argument("product_id", type=product_id, required=True)
order_products_parser.add_argument("quantity", type=int, required=True)
order_products_parser.add_argument("price", type=int, required=True)
order_products_parser.add_argument("order_id", type=order_id, required=True)

order_products_patch_parser = reqparse.RequestParser()
order_products_parser.add_argument("product_id", type=product_id, required=False)
order_products_parser.add_argument("quantity", type=int, required=False)
order_products_parser.add_argument("price", type=int, required=False)
order_products_parser.add_argument("order_id", type=order_id, required=False)
