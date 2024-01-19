"""Swagger models for order base apps."""
from flask_restful import fields
from flask_restful_swagger import swagger

from api.common.common import CustomDateTimeFormat


@swagger.model
class OrderFields(object):
    """OrderRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "user_id": fields.Integer,
        "name": fields.String,
        "created_at": CustomDateTimeFormat,
        "customer_id": fields.Integer,
    }


@swagger.model
class OrderProductFields(object):
    """OrderProductRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "product_id": fields.Integer,
        "quantity": fields.Integer,
        "price": fields.Integer,
        "order_id": fields.Integer,
    }
