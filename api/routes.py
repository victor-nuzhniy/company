"""Module for api app routes."""
from flask_restful import Resource, fields, marshal_with, reqparse

from api import User, api
from api.services import crud

post_parser = reqparse.RequestParser()
post_parser.add_argument("username", required=True)
post_parser.add_argument("email", required=True)
post_parser.add_argument("password", required=False)

patch_parameters = reqparse.RequestParser()
patch_parameters.add_argument("username", required=False)
patch_parameters.add_argument("email", required=False)

user_fields = {
    "id": fields.Integer,
    "username": fields.String,
    "email": fields.String,
}


class UserRoute(Resource):
    """Operations with single User isntance."""

    @marshal_with(user_fields)
    def get(self, user_id):
        """Get user by user id."""
        user = crud.read(User, {"id": user_id})
        return user

    @marshal_with(user_fields)
    def put(self, user_id):
        """Update user by user id."""
        args = post_parser.parse_args()
        user = crud.update(User, args, {"id": user_id})
        return user

    @marshal_with(user_fields)
    def patch(self, user_id):
        """Update user by user id, partially."""
        args = patch_parameters.parse_args()
        user = crud.update(User, args, {"id": user_id})
        return user

    def delete(self, user_id):
        """Delete user by id."""
        crud.delete(User, {"id": user_id})
        return {"message": f"Deleted User with id {user_id}"}


class UserListRoute(Resource):
    """Operations with many User isntances."""

    @marshal_with(user_fields)
    def post(self):
        """Create user."""
        args = post_parser.parse_args()
        user = crud.create(User, args)
        return user

    @marshal_with(user_fields)
    def get(self):
        """Get users list."""
        users = crud.read_many(User)
        return users


api.add_resource(UserRoute, "/user/<user_id>")
api.add_resource(UserListRoute, "/user/")
