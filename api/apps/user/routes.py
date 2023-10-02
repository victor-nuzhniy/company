"""User routers."""
from flask_restful import Resource, fields, marshal_with
from flask_restful_swagger import swagger

from api import User, api
from api.apps.user.parsers import (
    user_admin_patch_parser,
    user_parser,
    user_patch_parser,
)
from api.apps.user.schemas import (
    user_admin_schema,
    user_delete_schema,
    user_get_schema,
    user_patch_schema,
    user_post_schema,
    user_put_schema,
    users_get_schema,
)
from api.model_routes import ModelRoute, ModelsRoute, token_required
from api.services import crud


@swagger.model
class UserFields:
    """UserRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "username": fields.String,
        "email": fields.String,
    }


class UserRoute(ModelRoute):
    """Operations with single User isntance."""

    model = User
    put_parser = user_parser
    patch_parser = user_patch_parser
    model_fields = UserFields.resource_fields

    @swagger.operation(**user_get_schema)
    @token_required()
    def get(self, *args, **kwargs):
        """Get model instance by id."""
        return super().get(*args, **kwargs)

    @swagger.operation(**user_put_schema)
    @token_required(is_admin=True)
    def put(self, *args, **kwargs):
        """Update instance by id."""
        return super().put(*args, **kwargs)

    @swagger.operation(**user_patch_schema)
    @token_required(is_admin=True)
    def patch(self, *args, **kwargs):
        """Update instance bu id, partially."""
        return super().patch(*args, **kwargs)

    @swagger.operation(**user_delete_schema)
    @token_required(is_admin=True)
    def delete(self, *args, **kwargs):
        """Delete instance by id."""
        return super().delete(*args, **kwargs)


class UsersRoute(ModelsRoute):
    """Operations with many User isntances and instance creation."""

    model = User
    post_parser = user_parser
    model_fields = UserFields.resource_fields

    @swagger.operation(**user_post_schema)
    @token_required(is_admin=True)
    def post(self, *args, **kwargs):
        """Create model instance."""
        return super().post(*args, **kwargs)

    @swagger.operation(**users_get_schema)
    @token_required()
    def get(self, *args, **kwargs):
        """Get model instance list."""
        return super().get(*args, **kwargs)


class AdminUserRoute(Resource):
    """Admin user operations."""

    @swagger.operation(**user_admin_schema)
    @token_required(is_admin=True)
    @marshal_with(UserFields.resource_fields)
    def patch(self, user_id, *args, **kwargs):
        """Patch user instance."""
        args = user_admin_patch_parser.parse_args()
        args = {key: value for key, value in args.items() if value is not None}
        return crud.update(User, args, {"id": user_id})


api.add_resource(UserRoute, "/user/<instance_id>")
api.add_resource(UsersRoute, "/user/")
api.add_resource(AdminUserRoute, "/user/admin/<user_id>")
