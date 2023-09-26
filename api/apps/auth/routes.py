"""Auth routes."""
import jwt
from flask import abort
from flask_restful import Resource, marshal
from flask_restful_swagger import swagger

from api import User, api, app
from api.apps.auth.parsers import admin_parser, login_parser
from api.apps.auth.schemas import admin_schema, login_schema
from api.apps.auth.utils import login
from api.apps.user.routes import UserFields
from api.services import crud


class LoginRoute(Resource):
    """Login routes."""

    @swagger.operation(**login_schema)
    def post(self):
        """Handle post request."""
        try:
            data = login_parser.parse_args()
            user = login(data["email"], data["password"])
            if user:
                try:
                    # token should expire after 24 hrs
                    token = jwt.encode(
                        {"user_id": user.id},
                        app.config["SECRET_KEY"],
                        algorithm="HS256",
                    )
                    return {
                        "message": "Successfully fetched auth token",
                        "data": token,
                    }
                except Exception as e:
                    return {"error": "Something went wrong", "message": str(e)}, 500
            return {
                "message": "Error fetching auth token!, invalid email or password",
                "data": None,
                "error": "Unauthorized",
            }, 404
        except Exception as e:
            return {
                "message": "Something went wrong!",
                "error": str(e),
                "data": None,
            }, 500


class AdminRoute(Resource):
    """
    Admin routes.

    Create active admin user.
    """

    @swagger.operation(**admin_schema)
    def post(self):
        """Handle post request."""
        args = admin_parser.parse_args()
        args.update({"is_active": True, "is_admin": True})
        args.pop("admin_password")
        try:
            return marshal(crud.create(User, args), UserFields.resource_fields)
        except Exception as ex:
            abort(409, getattr(ex, "orig"))


api.add_resource(LoginRoute, "/auth/login/")
api.add_resource(AdminRoute, "/auth/create-admin/")
