"""Parsers for account apps."""
from flask_restful import reqparse

from api.apps.sale.validators import sale_invoice_id

account_parser = reqparse.RequestParser()
account_parser.add_argument("sale_invoice_id", type=sale_invoice_id, required=True)
