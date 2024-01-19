"""Swagger models for sale base apps."""
from flask_restful import fields
from flask_restful_swagger import swagger

from api.common.common import CustomDateTimeFormat


@swagger.model
class SaleInvoiceFields(object):
    """SaleInvoiceRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "name": fields.String,
        "invoice_id": fields.Integer,
        "created_at": CustomDateTimeFormat,
        "done": fields.Boolean,
    }


@swagger.model
class SaleInvoiceProductFields(object):
    """SaleInvoiceProductRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "product_id": fields.Integer,
        "quantity": fields.Integer,
        "price": fields.Integer,
        "sale_invoice_id": fields.Integer,
    }
