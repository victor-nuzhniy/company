"""Parsers for user apps."""
from flask_restful import reqparse
from flask_restful.inputs import boolean

from api.apps.user.validators import email, password, username

user_parser = reqparse.RequestParser()
user_parser.add_argument("username", type=username, required=True)
user_parser.add_argument("email", type=email, required=True)
user_parser.add_argument("password", type=password, required=True)
user_parser.add_argument("is_admin", type=boolean, required=False)
user_parser.add_argument("is_active", type=boolean, required=False)


user_patch_parser = reqparse.RequestParser()
user_patch_parser.add_argument("username", type=username, required=False)
user_patch_parser.add_argument("email", type=email, required=False)
user_patch_parser.add_argument("password", type=password, required=False)
user_patch_parser.add_argument("is_admin", type=boolean, required=False)
user_patch_parser.add_argument("is_active", type=boolean, required=False)

user_admin_patch_parser = reqparse.RequestParser()
user_admin_patch_parser.add_argument("is_active", type=boolean, required=False)
user_admin_patch_parser.add_argument("is_admin", type=boolean, required=False)
