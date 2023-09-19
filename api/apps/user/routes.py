"""User routers."""
from flask_restful import fields

from api import User, api
from api.apps.user.parsers import user_patch_parser, user_post_parser, user_put_parser
from api.services import ModelRoute, ModelsRoute

user_fields = {
    "id": fields.Integer,
    "username": fields.String,
    "email": fields.String,
}


class UserRoute(ModelRoute):
    """Operations with single User isntance."""

    model = User
    put_parser = user_put_parser
    patch_parser = user_patch_parser
    model_fields = user_fields


class UsersRoute(ModelsRoute):
    """Operations with many User isntances and instance creation."""

    model = User
    post_parser = user_post_parser
    model_fields = user_fields


api.add_resource(UserRoute, "/user/<instance_id>")
api.add_resource(UsersRoute, "/user/")
