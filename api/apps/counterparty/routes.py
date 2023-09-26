"""Module for counterparty rounters."""
from flask_restful import fields
from flask_restful_swagger import swagger

from api import Agreement, Counterparty, Discount, api
from api.apps.counterparty.parsers import (
    agreement_parser,
    counterparty_parser,
    counterparty_patch_parser,
    discount_parser,
    discount_patch_parser,
)
from api.model_routes import ModelRoute, ModelsRoute


@swagger.model
class DiscountFields:
    """DiscountRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "name": fields.String,
        "rate": fields.Integer,
    }


@swagger.model
class CounterpartyFields:
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
class AgreementFields:
    """AgreementRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "name": fields.String,
        "counterparty_id": fields.Integer,
    }


class DiscountRoute(ModelRoute):
    """Operations with single Agreement instance."""

    model = Discount
    put_parser = discount_parser
    patch_parser = discount_patch_parser
    model_fields = DiscountFields.resource_fields

    @swagger.operation()
    def get(self, *args, **kwargs):
        """Get model instance by id."""
        return super().get(*args, **kwargs)

    @swagger.operation()
    def put(self, *args, **kwargs):
        """Update instance by id."""
        return super().put(*args, **kwargs)

    @swagger.operation()
    def patch(self, *args, **kwargs):
        """Update instance bu id, partially."""
        return super().patch(*args, **kwargs)

    @swagger.operation()
    def delete(self, *args, **kwargs):
        """Delete instance by id."""
        return super().delete(*args, **kwargs)


class DiscountsRoute(ModelsRoute):
    """Operations with many Discounts instances and instance creation."""

    model = Discount
    post_parser = discount_parser
    model_fields = DiscountFields.resource_fields

    @swagger.operation()
    def post(self, *args, **kwargs):
        """Create model instance."""
        return super().post(*args, **kwargs)

    @swagger.operation()
    def get(self, *args, **kwargs):
        """Get model instance list."""
        return super().get(*args, **kwargs)


class CounterpartyRoute(ModelRoute):
    """Operations with single Counterparty instance."""

    model = Counterparty
    put_parser = counterparty_parser
    patch_parser = counterparty_patch_parser
    model_fields = CounterpartyFields.resource_fields

    @swagger.operation()
    def get(self, *args, **kwargs):
        """Get model instance by id."""
        return super().get(*args, **kwargs)

    @swagger.operation()
    def put(self, *args, **kwargs):
        """Update instance by id."""
        return super().put(*args, **kwargs)

    @swagger.operation()
    def patch(self, *args, **kwargs):
        """Update instance bu id, partially."""
        return super().patch(*args, **kwargs)

    @swagger.operation()
    def delete(self, *args, **kwargs):
        """Delete instance by id."""
        return super().delete(*args, **kwargs)


class CounterpartiesRoute(ModelsRoute):
    """Operations with many Counterparty instances and instance creation."""

    model = Counterparty
    post_parser = counterparty_parser
    model_fields = CounterpartyFields.resource_fields

    @swagger.operation()
    def post(self, *args, **kwargs):
        """Create model instance."""
        return super().post(*args, **kwargs)

    @swagger.operation()
    def get(self, *args, **kwargs):
        """Get model instance list."""
        return super().get(*args, **kwargs)


class AgreementRoute(ModelRoute):
    """Operations with single Agreement instance."""

    model = Agreement
    put_parser = agreement_parser
    patch_parser = agreement_parser
    model_fields = AgreementFields.resource_fields

    @swagger.operation()
    def get(self, *args, **kwargs):
        """Get model instance by id."""
        return super().get(*args, **kwargs)

    @swagger.operation()
    def put(self, *args, **kwargs):
        """Update instance by id."""
        return super().put(*args, **kwargs)

    @swagger.operation()
    def patch(self, *args, **kwargs):
        """Update instance bu id, partially."""
        return super().patch(*args, **kwargs)

    @swagger.operation()
    def delete(self, *args, **kwargs):
        """Delete instance by id."""
        return super().delete(*args, **kwargs)


class AgreementsRoute(ModelsRoute):
    """Operations with many Agreement instances and instance creation."""

    model = Agreement
    post_parser = agreement_parser
    model_fields = AgreementFields.resource_fields

    @swagger.operation()
    def post(self, *args, **kwargs):
        """Create model instance."""
        return super().post(*args, **kwargs)

    @swagger.operation()
    def get(self, *args, **kwargs):
        """Get model instance list."""
        return super().get(*args, **kwargs)


api.add_resource(DiscountRoute, "/discount/<instance_id>")
api.add_resource(DiscountsRoute, "/discount/")
api.add_resource(CounterpartyRoute, "/counterpary/,<instance_id>")
api.add_resource(CounterpartiesRoute, "/counterparty/")
api.add_resource(AgreementRoute, "/agreement/<instance_id>")
api.add_resource(AgreementsRoute, "/agreement/")
