"""Swagger models for sale special apps."""
from flask_restful import fields
from flask_restful_swagger import swagger

from api.common.common import CustomDateTimeFormat


@swagger.model
class SaleRegistryFields(object):
    """SaleRegistryRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "created_at": CustomDateTimeFormat,
        "name": fields.String,
        "summ": fields.Integer,
        "currency": fields.String,
        "counterparty": fields.String,
        "agreement": fields.String,
        "invoice": fields.String,
        "done": fields.Boolean,
    }


@swagger.model
class SaleInvoicesProductsFields(object):
    """SaleInvoicesProductsRoute output fields."""

    resourse_fields = {
        "id": fields.Integer,
        "product_id": fields.Integer,
        "quantity": fields.Integer,
        "price": fields.Integer,
        "sale_invoice_id": fields.Integer,
        "name": fields.String,
        "code": fields.String,
        "currency": fields.String,
        "units": fields.String,
    }
