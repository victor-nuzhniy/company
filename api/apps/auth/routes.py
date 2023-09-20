"""Auth routes."""
import jwt
from flask_restful import Resource, marshal

from api import User, api, app
from api.apps.auth.parsers import admin_parser, login_parser
from api.apps.auth.utils import login
from api.apps.user.routes import user_fields
from api.services import crud


class Login(Resource):
    """Login routes."""

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


class Admin(Resource):
    """Admin routes."""

    def post(self):
        """Handle post request."""
        args = admin_parser.parse_args()
        args.update({"is_active": True, "is_admin": True})
        args.pop("admin_password")
        return marshal(crud.create(User, args), user_fields)


api.add_resource(Login, "/login/")
api.add_resource(Admin, "/create-admin/")
