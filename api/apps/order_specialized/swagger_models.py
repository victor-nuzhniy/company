"""Swagger models for order_specialized apps."""
from flask_restful import fields
from flask_restful_swagger import swagger

from api.common import CustomDateTimeFormat


@swagger.model
class OrderRegistryFields(object):
    """OrderRegistryRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "username": fields.String,
        "order_name": fields.String,
        "created_at": CustomDateTimeFormat,
        "customer": fields.String,
        "summ": fields.Integer,
        "currency": fields.String,
    }


@swagger.model
class OrdersProductsFields(object):
    """OrdersProductsRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "product_id": fields.Integer,
        "quantity": fields.Integer,
        "price": fields.Integer,
        "order_id": fields.Integer,
        "name": fields.String,
        "code": fields.String,
        "currency": fields.String,
        "units": fields.String,
    }
