"""Swagger models for common special apps."""
from flask_restful import fields
from flask_restful_swagger import swagger


@swagger.model
class NameNumber(object):
    """NameRoute output fields."""

    resource_fields = {"number": fields.Integer}
