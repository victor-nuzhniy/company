"""Parsers for user apps."""
from flask_restful import reqparse
from flask_restful.inputs import boolean

from api.apps.user.validators import email, password, username

user_post_parser = reqparse.RequestParser()
user_post_parser.add_argument("username", type=username, required=True)
user_post_parser.add_argument("email", type=email, required=True)
user_post_parser.add_argument("password", type=password, required=False)

user_put_parser = reqparse.RequestParser()
user_put_parser.add_argument("username", type=username, required=True)
user_put_parser.add_argument("email", type=email, required=True)

user_patch_parser = reqparse.RequestParser()
user_patch_parser.add_argument("username", type=username, required=False)
user_patch_parser.add_argument("email", type=email, required=False)

user_admin_patch_parser = reqparse.RequestParser()
user_admin_patch_parser.add_argument("is_active", type=boolean, required=False)
user_admin_patch_parser.add_argument("is_admin", type=boolean, required=False)
