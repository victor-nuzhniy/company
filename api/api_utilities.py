"""Utilities for api."""
from typing import Dict, List, Optional

import jwt
from flask import Request, abort, current_app
from sqlalchemy import Row

from api import ModelType, User
from api.services import crud, db_utils


def get_model_unique_fields_name(model: ModelType) -> List:
    """Get model unique fields names list."""
    names: List = []
    for column in model.__table__.columns:
        if column.unique:
            names.append(column.name)
    return names


def check_unique(
    model: ModelType,
    data_values: Dict,
    instance_id: Optional[int] = None,
) -> None:
    """Check data_values for uniqueness."""
    unique_names: List = get_model_unique_fields_name(model)
    for name in unique_names:
        condition: bool = db_utils.check_unique_constraits(
            model,
            name,
            data_values.get(name),
            instance_id,
        )
        if name in data_values and condition:
            abort(
                409,
                "".join(
                    (
                        "Field {name} already has {data_value} value in ".format(
                            name=name,
                            data_value=data_values.get(name),
                        ),
                        "{table_name} table".format(table_name=model.__table__),
                    ),
                ),
            )


def get_token(req: Request) -> str:
    """Get token from request headers."""
    auth_data: Optional[str] = req.headers.get("Authorization")
    if auth_data:
        token = auth_data.split(" ")[1]
        if token:
            return token
    abort(401, "Authentication Token is missing! Unauthorized.")


def get_current_user(token: str) -> Row:
    """Get current user from token data."""
    data_values = jwt.decode(
        token,
        current_app.config["SECRET_KEY"],
        algorithms=["HS256"],
    )
    return crud.read(User, {"id": data_values.get("user_id")})


def check_current_user(current_user: Row, is_admin: bool) -> None:
    """Check current_user status."""
    if current_user is None:
        abort(401, "Invalid Authentication token!")
    if not current_user.is_active:
        abort(403, "Current user is not active.")
    if is_admin and not current_user.is_admin:
        abort(403, "Current user is not admin.")


def raise_forbidden_error(ex: str):
    """Raise forbidden error."""
    abort(
        403,
        "Authentication token is invalid. Error - {ex}".format(
            ex=ex,
        ),
    )
