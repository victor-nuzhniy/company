"""Utilities for auth apps."""
from typing import Optional

import jwt
from flask.typing import ResponseReturnValue
from sqlalchemy import Row
from werkzeug.security import check_password_hash, generate_password_hash

from api import User, app
from api.apps.common.auth.parsers import login_parser
from api.common.services import crud


def login(email: str, password: str) -> Optional[Row]:
    """Login and return base."""
    user = crud.read(User, {"email": email})
    if not user or not check_password_hash(user.password, password):
        return None
    return user


def disable_account(user_id: int) -> Row:
    """Disable base account - is_active to False."""
    return crud.update(User, {"is_active": False}, {"id": user_id})


def encrypt_password(password: str) -> str:
    """Encrypt password."""
    return generate_password_hash(password)


def get_auth_token_response(user: Row) -> dict[str, str]:
    """Get response with token data."""
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


def get_auth_response() -> ResponseReturnValue:
    """Get response with token data or message error."""
    parsed_data = login_parser.parse_args()
    user = login(parsed_data["email"], parsed_data["password"])
    if user:
        try:
            return get_auth_token_response(user)
        except Exception as ex:
            return {"error": "Something went wrong", "message": str(ex)}, 500
    return {
        "message": "Error fetching auth token!, invalid email or password",
        "data": None,
        "error": "Unauthorized",
    }, 404
