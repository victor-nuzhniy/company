"""Parsers for auth apps."""
from flask_restful import reqparse

from api.apps.user.parsers import user_post_parser
from api.apps.user.validators import admin_password, email

login_parser = reqparse.RequestParser()
login_parser.add_argument("email", type=email, required=True)
login_parser.add_argument("password", required=True)

admin_parser = user_post_parser.copy()
admin_parser.add_argument("admin_password", type=admin_password, required=True)
