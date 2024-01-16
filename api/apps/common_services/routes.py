"""Routes for common_services apps."""
import typing

from flask.typing import ResponseReturnValue
from flask_restful import Resource, fields, marshal
from flask_restful_swagger import swagger
from sqlalchemy import Row

from api import api
from api.apps.account.account_utilities import get_last_string_digits_number
from api.apps.common_services.schemas import name_number_schema
from api.apps.common_services.services import get_last_name
from api.model_routes import token_required


@swagger.model
class NameNumber(object):
    """NameRoute output fields."""

    resource_fields = {"number": fields.Integer}


class NameNumberRoute(Resource):
    """Get last model name number."""

    @swagger.operation(**name_number_schema)
    @token_required()
    def get(
        self, model_name: str, *args: typing.Any, **kwargs: typing.Any,
    ) -> ResponseReturnValue:
        """Get last model name number."""
        last_row: Row = get_last_name(model_name)
        return marshal(
            {"number": get_last_string_digits_number(last_row.name) + 1},
            NameNumber.resource_fields,
        )


api.add_resource(NameNumberRoute, "/account/<model_name>/")
