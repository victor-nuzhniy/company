"""Routes for order_specialized apps."""
import typing

from flask.typing import ResponseReturnValue
from flask_restful import Resource, marshal
from flask_restful_swagger import swagger

from api import Order, User, api, model_routes, services
from api.apps.counterparty.validators import counterparty_id_valid
from api.apps.invoice.validators import order_id_valid
from api.apps.order.swagger_models import OrderFields
from api.apps.order_specialized.parsers import order_registry_parser, user_order_parser
from api.apps.order_specialized.schemas import (
    counterparty_orders_get_schema,
    order_registry_get_schema,
    orders_products_get_schema,
    user_order_post_schema,
)
from api.apps.order_specialized.services import (
    get_order_products_by_order_id,
    get_order_registry_data,
)
from api.apps.order_specialized.swagger_models import (
    OrderRegistryFields,
    OrdersProductsFields,
)


class OrderRegistryRoute(Resource):
    """Order registry information."""

    @swagger.operation(**order_registry_get_schema)
    @model_routes.token_required()
    def get(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Get order registry list."""
        arguments = order_registry_parser.parse_args()
        return marshal(
            get_order_registry_data(**arguments),
            OrderRegistryFields.resource_fields,
        )


class OrdersProductsRoute(Resource):
    """Getting Orders products list by order id."""

    @swagger.operation(**orders_products_get_schema)
    @model_routes.token_required()
    def get(
        self,
        order_id: int,
        *args: typing.Any,
        **kwargs: typing.Any,
    ) -> ResponseReturnValue:
        """Get Orders products list by order id."""
        order_id = order_id_valid(order_id)
        return marshal(
            get_order_products_by_order_id(order_id),
            OrdersProductsFields.resource_fields,
        )


class UserOrderRoute(Resource):
    """Create Order by authorized user."""

    @swagger.operation(**user_order_post_schema)
    @model_routes.token_required()
    def post(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Create Order by authorized user."""
        arguments = user_order_parser.parse_args()
        current_user: typing.Optional[User] = kwargs.get("current_user")
        if current_user:
            arguments["user_id"] = current_user.id
            return marshal(
                services.crud.create(Order, arguments),
                OrderFields.resource_fields,
            )
        return {
            "message": "Authentication token is invalid",
            "data": None,
            "error": "error",
        }, 400


class CounterpartyOrdersRoute(Resource):
    """Get Counterparty Orders list by counterparty id."""

    @swagger.operation(**counterparty_orders_get_schema)
    @model_routes.token_required()
    def get(
        self,
        company_id: int,
        *args: typing.Any,
        **kwargs: typing.Any,
    ) -> ResponseReturnValue:
        """Get Orders list by counterparty id."""
        company_id = counterparty_id_valid(company_id)
        return marshal(
            services.crud.read_many(Order, {"customer_id": company_id}, rev=True),
            OrderFields.resource_fields,
        )


api.add_resource(OrderRegistryRoute, "/order-registry/")
api.add_resource(OrdersProductsRoute, "/orders-products/<order_id>/")
api.add_resource(UserOrderRoute, "/user-order/")
api.add_resource(CounterpartyOrdersRoute, "/orders/<company_id>/")
