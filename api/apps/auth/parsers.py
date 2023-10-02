"""Parsers for auth apps."""
from flask_restful import reqparse

from api.apps.user.validators import admin_password, email, password, username

login_parser = reqparse.RequestParser()
login_parser.add_argument("email", type=email, required=True)
login_parser.add_argument("password", required=True)

admin_parser = reqparse.RequestParser()
admin_parser.add_argument("username", type=username, required=True)
admin_parser.add_argument("email", type=email, required=True)
admin_parser.add_argument("password", type=password, required=True)
admin_parser.add_argument("admin_password", type=admin_password, required=True)
