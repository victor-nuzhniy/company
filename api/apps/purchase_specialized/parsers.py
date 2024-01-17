"""Parsers for purchase_specialized apps."""
from datetime import datetime

from flask_restful import reqparse

purchase_registry_parser = reqparse.RequestParser()
purchase_registry_parser.add_argument(
    "offset", type=int, required=False, location="args",
)
purchase_registry_parser.add_argument(
    "limit", type=int, required=False, location="args",
)
purchase_registry_parser.add_argument(
    "date_from",
    type=lambda arg: datetime.strptime(arg, "%Y-%m-%d"),
    required=False,
    location="args",
)
purchase_registry_parser.add_argument(
    "date_to",
    type=lambda arg: datetime.strptime(arg, "%Y-%m-%d"),
    required=False,
    location="args",
)
