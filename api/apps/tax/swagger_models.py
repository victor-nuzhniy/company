"""Swagger models for tax apps."""
from flask_restful import fields
from flask_restful_swagger import swagger

from api.common import CustomDateTimeFormat


@swagger.model
class TaxInvoiceFields(object):
    """TaxInvoiceRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "name": fields.String,
        "sale_invoice_id": fields.Integer,
        "created_at": CustomDateTimeFormat,
    }


@swagger.model
class TaxInvoiceProductFields(object):
    """TaxInvoiceProductRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "tax_invoice_id": fields.Integer,
        "sale_invoice_product_id": fields.Integer,
        "purchase_invoice_product_id": fields.Integer,
        "quantity": fields.Integer,
    }
