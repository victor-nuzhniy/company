"""Routes for user_specialized apps."""
import typing

from flask.typing import ResponseReturnValue
from flask_restful import Resource, marshal_with
from flask_restful_swagger import swagger

from api import User, api
from api.apps.user.parsers import user_admin_patch_parser
from api.apps.user.swagger_models import UserFields
from api.apps.user_specialized.schemas import user_admin_schema
from api.model_routes import token_required
from api.services import crud


class AdminUserRoute(Resource):
    """Admin user operations."""

    @swagger.operation(**user_admin_schema)
    @token_required(is_admin=True)
    @marshal_with(UserFields.resource_fields)
    def patch(
        self, user_id: int, *args: typing.Any, **kwargs: typing.Any,
    ) -> ResponseReturnValue:
        """Patch user instance."""
        arguments = user_admin_patch_parser.parse_args()
        arguments = {
            key: elem for key, elem in arguments.items() if elem is not None
        }
        return crud.update(User, arguments, {"id": user_id})


api.add_resource(AdminUserRoute, "/user/admin/<user_id>/")
