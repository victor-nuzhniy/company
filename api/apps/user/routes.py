"""User routers."""
import typing

from flask.typing import ResponseReturnValue
from flask_restful_swagger import swagger

from api import api
from api.apps.user import models
from api.apps.user.parsers import user_parser, user_patch_parser
from api.apps.user.schemas import (
    user_delete_schema,
    user_get_schema,
    user_patch_schema,
    user_post_schema,
    user_put_schema,
    users_get_schema,
)
from api.apps.user.swagger_models import UserFields
from api.model_routes import ModelRoute, ModelsRoute, token_required


class UserRoute(ModelRoute):
    """Operations with single User isntance."""

    model = models.User
    put_parser = user_parser
    patch_parser = user_patch_parser
    model_fields = UserFields.resource_fields

    @swagger.operation(**user_get_schema)
    @token_required()
    def get(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Get model instance by id."""
        return super().get(*args, **kwargs)

    @swagger.operation(**user_put_schema)
    @token_required(is_admin=True)
    def put(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Update instance by id."""
        return super().put(*args, **kwargs)

    @swagger.operation(**user_patch_schema)
    @token_required(is_admin=True)
    def patch(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Update instance bu id, partially."""
        return super().patch(*args, **kwargs)

    @swagger.operation(**user_delete_schema)
    @token_required(is_admin=True)
    def delete(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Delete instance by id."""
        return super().delete(*args, **kwargs)


class UsersRoute(ModelsRoute):
    """Operations with many User isntances and instance creation."""

    model = models.User
    post_parser = user_parser
    model_fields = UserFields.resource_fields

    @swagger.operation(**user_post_schema)
    @token_required(is_admin=True)
    def post(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Create model instance."""
        return super().post(*args, **kwargs)

    @swagger.operation(**users_get_schema)
    @token_required()
    def get(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Get model instance list."""
        return super().get(*args, **kwargs)


api.add_resource(UserRoute, "/user/<instance_id>/")
api.add_resource(UsersRoute, "/user/")
