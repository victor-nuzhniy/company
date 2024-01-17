"""Swagger models for tax_specialized apps."""
from flask_restful import fields
from flask_restful_swagger import swagger

from api.common import CustomDateTimeFormat


@swagger.model
class TaxRegistryFields:
    """TaxRegistryRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "created_at": CustomDateTimeFormat,
        "tax_invoice_name": fields.String,
        "invoice": fields.String,
        "invoice_id": fields.Integer,
        "sale_invoice": fields.String,
        "sale_invoice_id": fields.Integer,
        "purchase_invoice": fields.String,
        "purchase_invoice_id": fields.Integer,
        "agreement": fields.String,
        "agreement_id": fields.Integer,
        "counterparty": fields.String,
        "counterparty_id": fields.Integer,
        "sale_summ": fields.Integer,
        "purchase_summ": fields.Integer,
    }


@swagger.model
class TaxInvoicesProductsFields:
    """InvoicesProductsRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "product_id": fields.Integer,
        "quantity": fields.Integer,
        "sale_price": fields.Integer,
        "purchase_price": fields.Integer,
        "tax_invoice_id": fields.Integer,
        "sale_invoice_product_id": fields.Integer,
        "purchase_invoice_product_id": fields.Integer,
        "name": fields.String,
        "code": fields.String,
        "currency": fields.String,
        "units": fields.String,
    }

