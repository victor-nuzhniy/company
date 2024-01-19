"""Routes for common special apps."""
import typing

from flask.typing import ResponseReturnValue
from flask_restful import Resource, marshal
from flask_restful_swagger import swagger
from sqlalchemy import Row

from api import api
from api.apps.common.account.account_utilities import get_last_string_digits_number
from api.apps.common.special.schemas import name_number_schema
from api.apps.common.special.services import get_last_name
from api.apps.common.special.swagger_models import NameNumber
from api.common.model_routes import token_required


class NameNumberRoute(Resource):
    """Get last model name number."""

    @swagger.operation(**name_number_schema)
    @token_required()
    def get(
        self,
        model_name: str,
        *args: typing.Any,
        **kwargs: typing.Any,
    ) -> ResponseReturnValue:
        """Get last model name number."""
        last_row: Row = get_last_name(model_name)
        return marshal(
            {"number": get_last_string_digits_number(last_row.name) + 1},
            NameNumber.resource_fields,
        )


api.add_resource(NameNumberRoute, "/account/<model_name>/")
