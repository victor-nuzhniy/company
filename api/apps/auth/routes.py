"""Auth routes."""
import jwt
from flask_restful import Resource

from api import app
from api.apps.auth.parsers import login_parser
from api.apps.auth.utils import login


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
                        {"user_id": user["_id"]},
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
