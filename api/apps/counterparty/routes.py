"""Module for counterparty rounters."""
from flask_restful import fields

from api import Agreement, Counterparty, Discount, api
from api.apps.counterparty.parsers import (
    agreement_parser,
    counterparty_parser,
    counterparty_patch_parser,
    discount_parser,
    discount_patch_parser,
)
from api.services import ModelRoute, ModelsRoute

discount_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "rate": fields.Integer,
}

counterparty_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "postal_code": fields.String,
    "country": fields.String,
    "city": fields.String,
    "address": fields.String,
    "phone_number": fields.String,
    "discount_id": fields.Integer,
}

agreement_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "counterparty_id": fields.Integer,
}


class DiscountRoute(ModelRoute):
    """Operations with single Agreement instance."""

    model = Discount
    put_parser = discount_parser
    patch_parser = discount_patch_parser
    model_fields = discount_fields


class DiscountsRoute(ModelsRoute):
    """Operations with many Discounts instances and instance creation."""

    model = Discount
    post_parser = discount_parser
    model_fields = discount_fields


class CounterpartyRoute(ModelRoute):
    """Operations with single Counterparty instance."""

    model = Counterparty
    put_parser = counterparty_parser
    patch_parser = counterparty_patch_parser
    model_fields = counterparty_fields


class CounterpartiesRoute(ModelsRoute):
    """Operations with many Counterparty instances and instance creation."""

    model = Counterparty
    post_parser = counterparty_parser
    model_fields = counterparty_fields


class AgreementRoute(ModelRoute):
    """Operations with single Agreement instance."""

    model = Agreement
    put_parser = agreement_parser
    patch_parser = agreement_parser
    model_fields = agreement_fields


class AgreementsRoute(ModelsRoute):
    """Operations with many Agreement instances and instance creation."""

    model = Agreement
    post_parser = agreement_parser
    model_fields = agreement_fields


api.add_resource(DiscountRoute, "/discount/<discount_id>")
api.add_resource(DiscountsRoute, "/discount/")
api.add_resource(CounterpartyRoute, "/counterpary/,<counterparty_id>")
api.add_resource(CounterpartiesRoute, "/counterparty/")
api.add_resource(AgreementRoute, "/agreement/<agreement_id>")
api.add_resource(AgreementsRoute, "/agreement/")
