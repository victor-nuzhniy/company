"""Module for auth middleware functionality."""
from functools import wraps
from typing import Optional

import jwt
from flask import abort, current_app, request

from api import User
from api.services import crud


def token_required(f):
    """Check token presence decorator."""

    @wraps(f)
    def decorated(*args, **kwargs):
        """Perform token checking."""
        token: Optional[str] = None
        is_admin: bool = kwargs.get("is_amdmin", False)
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]
        if not token:
            return {
                "message": "Authentication Token is missing!",
                "data": None,
                "error": "Unauthorized",
            }, 401
        try:
            data = jwt.decode(
                token, current_app.config["SECRET_KEY"], algorithms=["HS256"]
            )
            current_user = crud.read(User, {"id": data["user_id"]})
            if current_user is None:
                return {
                    "message": "Invalid Authentication token!",
                    "data": None,
                    "error": "Unauthorized",
                }, 401
            if not current_user["is_active"]:
                abort(403)
            if is_admin and not current_user.is_admin:
                abort(403, {"message": "Only for admin user."})
        except Exception as e:
            return {
                "message": "Something went wrong",
                "data": None,
                "error": str(e),
            }, 500
        return f(current_user, *args, **kwargs)

    return decorated
