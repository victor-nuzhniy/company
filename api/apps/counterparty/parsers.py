"""Parsers for counterparty apps."""
from flask_restful import reqparse
from flask_restful.inputs import int_range

from api.apps.counterparty.validators import discount_name

discount_parser = reqparse.RequestParser()
discount_parser.add_argument("name", type=discount_name, required=True)
discount_parser.add_argument("rate", type=int_range(low=0, high=100), required=True)
