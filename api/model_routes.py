"""Model routes and its functionality."""
from functools import wraps
from typing import Dict, Optional

import jwt
from flask import abort, current_app, request
from flask_restful import Resource, marshal_with
from flask_restful.reqparse import RequestParser

from api import User, db
from api.services import crud


def token_required(is_admin: bool = False):
    """Check token presence decorator."""

    def decorator_factory(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            """Perform token checking."""
            token: Optional[str] = None
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
                current_user = crud.read(User, {"id": data.get("user_id")})
            except Exception as e:
                return {
                    "message": "Something went wrong",
                    "data": None,
                    "error": str(e),
                }, 500
            if current_user is None:
                return {
                    "message": "Invalid Authentication token!",
                    "data": None,
                    "error": "Unauthorized",
                }, 401
            if not current_user.is_active:
                abort(403, "Current user is not active.")
            if is_admin and not current_user.is_admin:
                abort(403, "Current user is not admin.")
            return f(*args, current_user=current_user, **kwargs)

        return decorated

    return decorator_factory


class ModelRoute(Resource):
    """Operations with single model instance."""

    model: Optional[db.Model] = None
    put_parser: Optional[RequestParser] = None
    patch_parser: Optional[RequestParser] = None
    model_fields: Optional[Dict] = None

    def __init__(self):
        """Add model_fields attribute and apply decorator to methods."""
        super().__init__()
        ModelRoute.get = marshal_with(self.model_fields)(ModelRoute.get)
        ModelRoute.put = marshal_with(self.model_fields)(ModelRoute.put)
        ModelRoute.patch = marshal_with(self.model_fields)(ModelRoute.patch)

    def get(self, instance_id, *args, **kwargs):
        """Get model instance by id."""
        return crud.read(self.model, {"id": instance_id})

    @token_required
    def put(self, instance_id, *args, **kwargs):
        """Update instance by id."""
        args = self.put_parser.parse_args()
        return crud.update(self.model, args, {"id": instance_id})

    def patch(self, instance_id, *args, **kwargs):  # TODO add token_decorator to all
        """Update instance bu id, partially."""
        args = self.patch_parser.parse_args()
        args = {key: value for key, value in args.items() if value is not None}
        return crud.update(self.model, args, {"id": instance_id})

    def delete(self, instance_id, *args, **kwargs):
        """Delete instance by id."""
        crud.delete(self.model, {"id": instance_id})
        return {
            "message": f"Deleted {self.model.__name__} instance with id {instance_id}"
        }


class ModelsRoute(Resource):
    """Operations with multiple model instance and instance creation."""

    model: Optional[db.Model] = None
    post_parser: Optional[RequestParser] = None
    model_fields: Optional[Dict] = None

    def __init__(self):
        """Add model_fields attribute and apply decorator to methods."""
        super().__init__()
        ModelsRoute.post = marshal_with(self.model_fields)(ModelsRoute.post)
        ModelsRoute.get = marshal_with(self.model_fields)(ModelsRoute.get)

    def post(self, *args, **kwargs):
        """Create model instance."""
        args = self.post_parser.parse_args()
        return crud.create(self.model, args)

    def get(self, *args, **kwargs):
        """Get model instance list."""
        return crud.read_many(self.model)