"""Swagger models for counterparty base apps."""
from flask_restful import fields
from flask_restful_swagger import swagger


@swagger.model
class DiscountFields(object):
    """DiscountRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "name": fields.String,
        "rate": fields.Integer,
    }


@swagger.model
class CounterpartyFields(object):
    """CounterpartyRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "name": fields.String,
        "postal_code": fields.String,
        "country": fields.String,
        "city": fields.String,
        "address": fields.String,
        "phone_number": fields.String,
        "discount_id": fields.Integer,
    }


@swagger.model
class AgreementFields(object):
    """AgreementRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "name": fields.String,
        "counterparty_id": fields.Integer,
    }
