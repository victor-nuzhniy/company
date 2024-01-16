"""Swagger models for account apps."""
from flask_restful import fields
from flask_restful_swagger import swagger


@swagger.model
class PeriodReport(object):
    """PeriodReportRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "quantity": fields.String,
        "price": fields.String,
        "sale_invoice_name": fields.String,
        "created_at": fields.DateTime,
        "name": fields.String,
        "units": fields.String,
        "code": fields.String,
        "currency": fields.String,
    }


@swagger.model
class ProductLeftovers(object):
    """ProductLeftoversRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "name": fields.String,
        "units": fields.String,
        "currency": fields.String,
        "quantity": fields.Integer,
    }


@swagger.model
class IncomeForPeriod(object):
    """IncomeForPeriodRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "name": fields.String,
        "code": fields.String,
        "currency": fields.String,
        "product_type": fields.String,
        "income": fields.Integer,
    }
