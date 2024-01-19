"""Swagger models for purchase special apps."""
from flask_restful import fields
from flask_restful_swagger import swagger

from api.common.common import CustomDateTimeFormat


@swagger.model
class PurchaseRegistryFields(object):
    """PurchaseRegistry output fields."""

    resource_fields = {
        "id": fields.Integer,
        "created_at": CustomDateTimeFormat,
        "purchase_name": fields.String,
        "summ": fields.Integer,
        "currency": fields.String,
        "counterparty": fields.String,
        "agreement": fields.String,
    }


@swagger.model
class PurchaseInvoicesProductsFields(object):
    """PurchaseInvoicesProductsRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "product_id": fields.Integer,
        "quantity": fields.Integer,
        "price": fields.Integer,
        "products_left": fields.Integer,
        "purchase_invoice_id": fields.Integer,
        "name": fields.String,
        "code": fields.String,
        "currency": fields.String,
        "units": fields.String,
    }


class PurchaseInvoiceProductsLeftFields(object):
    """PurchaseInvoiceProductsLeftRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "product_id": fields.Integer,
        "products_left": fields.Integer,
        "name": fields.String,
        "code": fields.String,
    }
