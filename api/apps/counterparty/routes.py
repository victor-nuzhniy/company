"""Module for counterparty rounters."""
from flask_restful import Resource, fields, marshal
from flask_restful_swagger import swagger

from api import Agreement, Counterparty, Discount, api
from api.apps.counterparty.parsers import (
    agreement_parser,
    agreement_patch_parser,
    counterparty_parser,
    counterparty_patch_parser,
    discount_parser,
    discount_patch_parser,
)
from api.apps.counterparty.schemas import (
    agreement_delete_schema,
    agreement_get_schema,
    agreement_patch_schema,
    agreement_post_schema,
    agreement_put_schema,
    agreements_get_schema,
    counterparties_get_schema,
    counterparty_agreements_get_schema,
    counterparty_delete_schema,
    counterparty_get_schema,
    counterparty_patch_schema,
    counterparty_post_schema,
    counterparty_put_schema,
    discount_delete_schema,
    discount_get_schema,
    discount_patch_schema,
    discount_post_schema,
    discount_put_schema,
    discounts_get_schema,
)
from api.apps.counterparty.validators import counterparty_id
from api.model_routes import ModelRoute, ModelsRoute, token_required
from api.services import crud


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

    @swagger.operation(**discount_get_schema)
    @token_required()
    def get(self, *args, **kwargs):
        """Get model instance by id."""
        return super().get(*args, **kwargs)

    @swagger.operation(**discount_put_schema)
    @token_required()
    def put(self, *args, **kwargs):
        """Update instance by id."""
        return super().put(*args, **kwargs)

    @swagger.operation(**discount_patch_schema)
    @token_required()
    def patch(self, *args, **kwargs):
        """Update instance bu id, partially."""
        return super().patch(*args, **kwargs)

    @swagger.operation(**discount_delete_schema)
    @token_required()
    def delete(self, *args, **kwargs):
        """Delete instance by id."""
        return super().delete(*args, **kwargs)


class DiscountsRoute(ModelsRoute):
    """Operations with many Discounts instances and instance creation."""

    model = Discount
    post_parser = discount_parser
    model_fields = DiscountFields.resource_fields

    @swagger.operation(**discount_post_schema)
    @token_required()
    def post(self, *args, **kwargs):
        """Create model instance."""
        return super().post(*args, **kwargs)

    @swagger.operation(**discounts_get_schema)
    @token_required()
    def get(self, *args, **kwargs):
        """Get model instance list."""
        return super().get(*args, **kwargs)


class CounterpartyRoute(ModelRoute):
    """Operations with single Counterparty instance."""

    model = Counterparty
    put_parser = counterparty_parser
    patch_parser = counterparty_patch_parser
    model_fields = CounterpartyFields.resource_fields

    @swagger.operation(**counterparty_get_schema)
    @token_required()
    def get(self, *args, **kwargs):
        """Get model instance by id."""
        return super().get(*args, **kwargs)

    @swagger.operation(**counterparty_put_schema)
    @token_required()
    def put(self, *args, **kwargs):
        """Update instance by id."""
        return super().put(*args, **kwargs)

    @swagger.operation(**counterparty_patch_schema)
    @token_required()
    def patch(self, *args, **kwargs):
        """Update instance bu id, partially."""
        return super().patch(*args, **kwargs)

    @swagger.operation(**counterparty_delete_schema)
    @token_required()
    def delete(self, *args, **kwargs):
        """Delete instance by id."""
        return super().delete(*args, **kwargs)


class CounterpartysRoute(ModelsRoute):
    """Operations with many Counterparty instances and instance creation."""

    model = Counterparty
    post_parser = counterparty_parser
    model_fields = CounterpartyFields.resource_fields

    @swagger.operation(**counterparty_post_schema)
    @token_required()
    def post(self, *args, **kwargs):
        """Create model instance."""
        return super().post(*args, **kwargs)

    @swagger.operation(**counterparties_get_schema)
    @token_required()
    def get(self, *args, **kwargs):
        """Get model instance list."""
        return super().get(*args, **kwargs)


class AgreementRoute(ModelRoute):
    """Operations with single Agreement instance."""

    model = Agreement
    put_parser = agreement_parser
    patch_parser = agreement_patch_parser
    model_fields = AgreementFields.resource_fields

    @swagger.operation(**agreement_get_schema)
    @token_required()
    def get(self, *args, **kwargs):
        """Get model instance by id."""
        return super().get(*args, **kwargs)

    @swagger.operation(**agreement_put_schema)
    @token_required()
    def put(self, *args, **kwargs):
        """Update instance by id."""
        return super().put(*args, **kwargs)

    @swagger.operation(**agreement_patch_schema)
    @token_required()
    def patch(self, *args, **kwargs):
        """Update instance bu id, partially."""
        return super().patch(*args, **kwargs)

    @swagger.operation(**agreement_delete_schema)
    @token_required()
    def delete(self, *args, **kwargs):
        """Delete instance by id."""
        return super().delete(*args, **kwargs)


class AgreementsRoute(ModelsRoute):
    """Operations with many Agreement instances and instance creation."""

    model = Agreement
    post_parser = agreement_parser
    model_fields = AgreementFields.resource_fields

    @swagger.operation(**agreement_post_schema)
    @token_required()
    def post(self, *args, **kwargs):
        """Create model instance."""
        return super().post(*args, **kwargs)

    @swagger.operation(**agreements_get_schema)
    @token_required()
    def get(self, *args, **kwargs):
        """Get model instance list."""
        return super().get(*args, **kwargs)


class CounterpartyAgreementsRoute(Resource):
    """Get Counterparty Agreements list by counterparty id."""

    @swagger.operation(**counterparty_agreements_get_schema)
    @token_required()
    def get(self, company_id, *args, **kwargs):
        """Get Agreements list by counterparty id."""
        company_id = counterparty_id(company_id)
        return marshal(
            crud.read_many(Agreement, {"counterparty_id": company_id}),
            AgreementFields.resource_fields,
        )


api.add_resource(DiscountRoute, "/discount/<instance_id>/")
api.add_resource(DiscountsRoute, "/discount/")
api.add_resource(CounterpartyRoute, "/counterpary/,<instance_id>/")
api.add_resource(CounterpartysRoute, "/counterparty/")
api.add_resource(AgreementRoute, "/agreement/<instance_id>/")
api.add_resource(AgreementsRoute, "/agreement/")
api.add_resource(CounterpartyAgreementsRoute, "/agreements/<company_id>/")
