"""Swager models for invoice base apps."""
from flask_restful import fields
from flask_restful_swagger import swagger

from api.common.common import CustomDateTimeFormat


@swagger.model
class InvoiceFields(object):
    """InvoiceRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "name": fields.String,
        "order_id": fields.Integer,
        "created_at": CustomDateTimeFormat,
        "paid": fields.Boolean,
        "agreement_id": fields.Integer,
    }


@swagger.model
class InvoiceProductFields(object):
    """InvoiceProductRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "product_id": fields.Integer,
        "quantity": fields.Integer,
        "price": fields.Integer,
        "invoice_id": fields.Integer,
    }
