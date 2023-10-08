"""Parsers for order apps."""
from datetime import datetime

from flask_restful import reqparse

from api.apps.counterparty.validators import counterparty_id
from api.apps.invoice.validators import order_id, product_id, str_length_100
from api.apps.order.validators import user_id

order_post_parser = reqparse.RequestParser()
order_post_parser.add_argument("user_id", type=user_id, required=True)
order_post_parser.add_argument("name", type=str_length_100, required=True)
order_post_parser.add_argument("customer_id", type=counterparty_id, required=True)

order_put_parser = reqparse.RequestParser()
order_put_parser.add_argument("user_id", type=user_id, required=True)
order_put_parser.add_argument("name", type=str_length_100, required=True)
order_put_parser.add_argument(
    "created_at",
    type=lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S"),
    required=True,
)
order_put_parser.add_argument("customer_id", type=counterparty_id, required=True)


order_patch_parser = reqparse.RequestParser()
order_patch_parser.add_argument("user_id", type=user_id, required=False)
order_patch_parser.add_argument("name", type=str_length_100, required=False)
order_patch_parser.add_argument(
    "created_at",
    type=lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S"),
    required=False,
)
order_patch_parser.add_argument("customer_id", type=counterparty_id, required=False)


order_product_parser = reqparse.RequestParser()
order_product_parser.add_argument("product_id", type=product_id, required=True)
order_product_parser.add_argument("quantity", type=int, required=True)
order_product_parser.add_argument("price", type=int, required=True)
order_product_parser.add_argument("order_id", type=order_id, required=True)

order_product_patch_parser = reqparse.RequestParser()
order_product_patch_parser.add_argument("product_id", type=product_id, required=False)
order_product_patch_parser.add_argument("quantity", type=int, required=False)
order_product_patch_parser.add_argument("price", type=int, required=False)
order_product_patch_parser.add_argument("order_id", type=order_id, required=False)

order_registry_parser = reqparse.RequestParser()
order_registry_parser.add_argument("offset", type=int, required=False, location="args")
order_registry_parser.add_argument("limit", type=int, required=False, location="args")
order_registry_parser.add_argument(
    "date_from",
    type=lambda x: datetime.strptime(x, "%Y-%m-%d"),
    required=False,
    location="args",
)
order_registry_parser.add_argument(
    "date_to",
    type=lambda x: datetime.strptime(x, "%Y-%m-%d"),
    required=False,
    location="args",
)
