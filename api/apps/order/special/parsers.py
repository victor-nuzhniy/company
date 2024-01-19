"""Parsers for order special apps."""
from datetime import datetime

from flask_restful import reqparse

from api.apps.counterparty.base.validators import counterparty_id_valid
from api.apps.invoice.base.validators import str_hundred

order_registry_parser = reqparse.RequestParser()
order_registry_parser.add_argument("offset", type=int, required=False, location="args")
order_registry_parser.add_argument("limit", type=int, required=False, location="args")
order_registry_parser.add_argument(
    "date_from",
    type=lambda arg: datetime.strptime(arg, "%Y-%m-%d"),
    required=False,
    location="args",
)
order_registry_parser.add_argument(
    "date_to",
    type=lambda arg: datetime.strptime(arg, "%Y-%m-%d"),
    required=False,
    location="args",
)

user_order_parser = reqparse.RequestParser()
user_order_parser.add_argument("name", type=str_hundred, required=True)
user_order_parser.add_argument("customer_id", type=counterparty_id_valid, required=True)
