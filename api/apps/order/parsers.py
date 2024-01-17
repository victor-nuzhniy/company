"""Parsers for order apps."""
from datetime import datetime

from flask_restful import reqparse

from api.apps.counterparty.validators import counterparty_id_valid
from api.apps.invoice.validators import order_id_valid, product_id_valid, str_hundred
from api.apps.order.validators import user_id_valid

order_post_parser = reqparse.RequestParser()
order_post_parser.add_argument("user_id", type=user_id_valid, required=True)
order_post_parser.add_argument("name", type=str_hundred, required=True)
order_post_parser.add_argument("customer_id", type=counterparty_id_valid, required=True)

order_put_parser = reqparse.RequestParser()
order_put_parser.add_argument("user_id", type=user_id_valid, required=True)
order_put_parser.add_argument("name", type=str_hundred, required=True)
order_put_parser.add_argument(
    "created_at",
    type=lambda arg: datetime.strptime(arg, "%Y-%m-%d %H:%M:%S"),
    required=True,
)
order_put_parser.add_argument("customer_id", type=counterparty_id_valid, required=True)


order_patch_parser = reqparse.RequestParser()
order_patch_parser.add_argument("user_id", type=user_id_valid, required=False)
order_patch_parser.add_argument("name", type=str_hundred, required=False)
order_patch_parser.add_argument(
    "created_at",
    type=lambda arg: datetime.strptime(arg, "%Y-%m-%d %H:%M:%S"),
    required=False,
)
order_patch_parser.add_argument(
    "customer_id", type=counterparty_id_valid, required=False,
)


order_product_parser = reqparse.RequestParser()
order_product_parser.add_argument("product_id", type=product_id_valid, required=True)
order_product_parser.add_argument("quantity", type=int, required=True)
order_product_parser.add_argument("price", type=int, required=True)
order_product_parser.add_argument("order_id", type=order_id_valid, required=True)

order_product_patch_parser = reqparse.RequestParser()
order_product_patch_parser.add_argument(
    "product_id", type=product_id_valid, required=False,
)
order_product_patch_parser.add_argument("quantity", type=int, required=False)
order_product_patch_parser.add_argument("price", type=int, required=False)
order_product_patch_parser.add_argument("order_id", type=order_id_valid, required=False)
