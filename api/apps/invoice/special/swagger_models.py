"""Swagger models for invoice special apps."""
from flask_restful import fields
from flask_restful_swagger import swagger

from api.common.common import CustomDateTimeFormat


@swagger.model
class InvoiceRegistryFields(object):
    """InvoiceRegistry output fields."""

    resource_fields = {
        "id": fields.Integer,
        "created_at": CustomDateTimeFormat,
        "invoice_name": fields.String,
        "paid": fields.Boolean,
        "order": fields.String,
        "order_id": fields.Integer,
        "summ": fields.Integer,
        "currency": fields.String,
        "agreement": fields.String,
        "agreement_id": fields.Integer,
        "counterparty": fields.String,
        "counterparty_id": fields.Integer,
    }


@swagger.model
class InvoicesProductsFields(object):
    """InvoicesProductsRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "product_id": fields.Integer,
        "quantity": fields.Integer,
        "price": fields.Integer,
        "invoice_id": fields.Integer,
        "name": fields.String,
        "code": fields.String,
        "currency": fields.String,
        "units": fields.String,
    }
