"""Parsers for account apps."""
from flask_restful import reqparse
from flask_restful.inputs import date

from api.apps.sale.base.validators import sale_invoice_id_valid

account_parser = reqparse.RequestParser()
account_parser.add_argument(
    "sale_invoice_id",
    type=sale_invoice_id_valid,
    required=True,
)

period_parser = reqparse.RequestParser()
period_parser.add_argument("date_from", type=date, required=True)
period_parser.add_argument("date_to", type=date, required=True)

product_leftovers_parser = reqparse.RequestParser()
product_leftovers_parser.add_argument("date", type=date, required=True)
