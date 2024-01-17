"""Swagger models for user apps."""
from flask_restful import fields
from flask_restful_swagger import swagger


@swagger.model
class UserFields(object):
    """UserRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "username": fields.String,
        "email": fields.String,
    }
