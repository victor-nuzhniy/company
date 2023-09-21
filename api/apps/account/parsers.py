"""Parsers for account apps."""
from flask_restful import reqparse

from api.apps.invoice.validators import invoice_id

account_parser = reqparse.RequestParser()
account_parser.add_argument("invoice_id", type=invoice_id, required=True)
