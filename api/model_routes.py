"""Model routes and its functionality."""
from functools import wraps
from typing import Any, Callable, Dict, Optional

from flask import request
from flask.typing import ResponseReturnValue
from flask_restful import Resource, marshal
from flask_restful.reqparse import RequestParser
from sqlalchemy import Row

from api import ModelType
from api.api_utilities import (
    check_current_user,
    check_unique,
    get_current_user,
    get_token,
    raise_forbidden_error,
)
from api.constants import server_error
from api.services import crud


def token_required(is_admin: bool = False) -> Callable:
    """Check token presence decorator."""

    def decorator_factory(func: Callable) -> Callable:  # noqa WPS430
        @wraps(func)
        def decorated(*args: Any, **kwargs: Any) -> ResponseReturnValue:  # noqa WPS430
            """Perform token checking."""
            token = get_token(request)
            current_user: Optional[Row] = None
            try:
                current_user = get_current_user(token)
            except Exception as ex:
                raise_forbidden_error(str(ex))
            check_current_user(current_user, is_admin)
            return func(*args, current_user=current_user, **kwargs)

        return decorated

    return decorator_factory


class ModelRoute(Resource):
    """Operations with single model instance."""

    model: Optional[ModelType] = None
    put_parser: Optional[RequestParser] = None
    patch_parser: Optional[RequestParser] = None
    model_fields: Optional[Dict] = None

    def get(self, instance_id: int, *args: Any, **kwargs: Any) -> ResponseReturnValue:
        """Get model instance by id."""
        if self.model:
            return marshal(
                crud.read(self.model, {"id": instance_id}),
                self.model_fields,
            )
        return server_error

    def put(self, instance_id: int, *args: Any, **kwargs: Any) -> ResponseReturnValue:
        """Update instance by id."""
        if self.put_parser and self.model:
            arguments = self.put_parser.parse_args()
            check_unique(self.model, arguments, instance_id)
            return marshal(
                crud.update(self.model, arguments, {"id": instance_id}),
                self.model_fields,
            )
        return server_error

    def patch(
        self,
        instance_id: int,
        *args: Any,
        **kwargs: Any,
    ) -> ResponseReturnValue:  # TODO add token_decorator to all
        """Update instance by id, partially."""
        if self.patch_parser and self.model:
            arguments = self.patch_parser.parse_args()
            arguments = {
                key: elem for key, elem in arguments.items() if elem is not None
            }
            check_unique(self.model, arguments, instance_id)
            return marshal(
                crud.update(self.model, arguments, {"id": instance_id}),
                self.model_fields,
            )
        return server_error

    def delete(
        self,
        instance_id: int,
        *args: Any,
        **kwargs: Any,
    ) -> ResponseReturnValue:
        """Delete instance by id."""
        if self.model:
            crud.delete(self.model, {"id": instance_id})
            return {
                "message": "Deleted {name} instance with id {id}".format(
                    name=self.model.__name__,
                    id=instance_id,
                ),
            }
        return server_error


class ModelsRoute(Resource):
    """Operations with multiple model instance and instance creation."""

    model: Optional[ModelType] = None
    post_parser: Optional[RequestParser] = None
    model_fields: Optional[Dict] = None

    def post(self, *args: Any, **kwargs: Any) -> ResponseReturnValue:
        """Create model instance."""
        if self.post_parser and self.model:
            arguments = self.post_parser.parse_args()
            check_unique(self.model, arguments)
            return marshal(crud.create(self.model, arguments), self.model_fields)
        return server_error

    def get(self, *args: Any, **kwargs: Any) -> ResponseReturnValue:
        """Get model instance list."""
        if self.model:
            return marshal(crud.read_many(self.model, rev=True), self.model_fields)
        return server_error
