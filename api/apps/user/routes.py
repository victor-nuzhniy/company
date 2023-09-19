"""User routers."""
from flask_restful import Resource, fields, marshal_with

from api import User, api
from api.apps.user.parsers import (
    user_admin_patch_parser,
    user_patch_parser,
    user_post_parser,
    user_put_parser,
)
from api.model_routes import ModelRoute, ModelsRoute, token_required
from api.services import crud

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


class AdminUserRoute(Resource):
    """Admin user operations."""

    @token_required(is_admin=True)
    @marshal_with(user_fields)
    def patch(self, user_id, *args, **kwargs):
        """Patch user instance."""
        args = user_admin_patch_parser.parse_args()
        args = {key: value for key, value in args.items() if value is not None}
        return crud.update(User, args, {"id": user_id})


api.add_resource(UserRoute, "/user/<instance_id>")
api.add_resource(UsersRoute, "/user/")
api.add_resource(AdminUserRoute, "/user/admin/<user_id>")
