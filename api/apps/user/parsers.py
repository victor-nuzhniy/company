"""Parsers for user apps."""
from flask_restful import reqparse

from api.apps.user.validators import email, username

user_post_parser = reqparse.RequestParser()
user_post_parser.add_argument("username", type=username, required=True)
user_post_parser.add_argument("email", type=email, required=True)
user_post_parser.add_argument("password", required=False)

user_put_parser = reqparse.RequestParser()
user_put_parser.add_argument("username", type=username, required=True)
user_put_parser.add_argument("email", type=email, required=True)

user_patch_parser = reqparse.RequestParser()
user_patch_parser.add_argument("username", type=username, required=False)
user_patch_parser.add_argument("email", type=email, required=False)
