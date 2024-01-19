"""Auth routes."""
from flask.typing import ResponseReturnValue
from flask_restful import Resource, marshal
from flask_restful_swagger import swagger

from api.app import api
from api.apps.common.auth.auth_utilities import get_auth_response
from api.apps.common.auth.parsers import admin_parser
from api.apps.common.auth.schemas import admin_schema, login_schema
from api.apps.user.base import models
from api.apps.user.base.swagger_models import UserFields
from api.common.api_utilities import check_unique
from api.common.services import crud


class LoginRoute(Resource):
    """Login routes."""

    @swagger.operation(**login_schema)
    def post(self) -> ResponseReturnValue:
        """Handle post request."""
        try:
            return get_auth_response()
        except Exception as ex:
            return {
                "message": "Something went wrong!",
                "error": str(ex),
                "data": None,
            }, 500


class AdminRoute(Resource):
    """
    Admin routes.

    Create active admin base.
    """

    @swagger.operation(**admin_schema)
    def post(self) -> ResponseReturnValue:
        """Handle post request."""
        args = admin_parser.parse_args()
        args.update({"is_active": True, "is_admin": True})
        args.pop("admin_password", None)
        check_unique(models.User, args)
        return marshal(crud.create(models.User, args), UserFields.resource_fields)


api.add_resource(LoginRoute, "/auth/login/")
api.add_resource(AdminRoute, "/auth/create-admin/")
