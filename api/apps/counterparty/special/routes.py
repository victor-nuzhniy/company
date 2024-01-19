"""Routes for counterparty special apps."""
import typing

from flask.typing import ResponseReturnValue
from flask_restful import Resource, marshal
from flask_restful_swagger import swagger

from api.app import api
from api.apps.counterparty.base import models
from api.apps.counterparty.base.swagger_models import AgreementFields
from api.apps.counterparty.base.validators import counterparty_id_valid
from api.apps.counterparty.special.schemas import counterparty_agreements_get_schema
from api.common.model_routes import token_required
from api.common.services import crud


class CounterpartyAgreementsRoute(Resource):
    """Get Counterparty Agreements list by base id."""

    @swagger.operation(**counterparty_agreements_get_schema)
    @token_required()
    def get(
        self,
        company_id: int,
        *args: typing.Any,
        **kwargs: typing.Any,
    ) -> ResponseReturnValue:
        """Get Agreements list by base id."""
        company_id = counterparty_id_valid(company_id)
        return marshal(
            crud.read_many(models.Agreement, {"counterparty_id": company_id}),
            AgreementFields.resource_fields,
        )


api.add_resource(CounterpartyAgreementsRoute, "/agreements/<company_id>/")
