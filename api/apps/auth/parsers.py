"""Parsers for auth apps."""
from flask_restful import reqparse

from api.apps.user.validators import email

login_parser = reqparse.RequestParser()
login_parser.add_argument("email", type=email, required=True)
login_parser.add_argument("password", required=True)
