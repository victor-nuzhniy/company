"""Parsers for user apps."""
from flask_restful import reqparse

from api.apps.user.validators import email, username

post_parser = reqparse.RequestParser()
post_parser.add_argument("username", type=username, required=True)
post_parser.add_argument("email", type=email, required=True)
post_parser.add_argument("password", required=False)

put_parser = reqparse.RequestParser()
put_parser.add_argument("username", type=username, required=True)
put_parser.add_argument("email", type=email, required=True)

patch_parser = reqparse.RequestParser()
patch_parser.add_argument("username", type=username, required=False)
patch_parser.add_argument("email", type=email, required=False)
