"""Swagger models for product base apps."""
from flask_restful import fields
from flask_restful_swagger import swagger


@swagger.model
class ProductFields(object):
    """ProfudctFieldsRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "name": fields.String,
        "code": fields.String,
        "units": fields.String,
        "currency": fields.String,
        "price": fields.Integer,
        "product_type_id": fields.Integer,
    }


@swagger.model
class ProductTypeFields(object):
    """ProductTypeRoute output fields."""

    resource_fields = {"id": fields.Integer, "name": fields.String}
