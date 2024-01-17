"""Swagger models for purchase apps."""
from flask_restful import fields
from flask_restful_swagger import swagger

from api.common import CustomDateTimeFormat


@swagger.model
class PurchaseInvoiceFields(object):
    """PurchaseInvoiceRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "name": fields.String,
        "agreement_id": fields.Integer,
        "created_at": CustomDateTimeFormat,
    }


@swagger.model
class PurchaseInvoiceProductFields(object):
    """PurchaseInvoiceProductRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "product_id": fields.Integer,
        "quantity": fields.Integer,
        "price": fields.Integer,
        "purchase_invoice_id": fields.Integer,
        "products_left": fields.Integer,
    }
