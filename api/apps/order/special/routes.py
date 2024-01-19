"""Routes for order special apps."""
import typing

from flask.typing import ResponseReturnValue
from flask_restful import Resource, marshal
from flask_restful_swagger import swagger

from api import Order, User
from api.app import api
from api.apps.counterparty.base.validators import counterparty_id_valid
from api.apps.invoice.base.validators import order_id_valid
from api.apps.order.base.swagger_models import OrderFields
from api.apps.order.special import parsers, schemas, services, swagger_models
from api.common import model_routes
from api.common import services as api_services


class OrderRegistryRoute(Resource):
    """Order registry information."""

    @swagger.operation(**schemas.order_registry_get_schema)
    @model_routes.token_required()
    def get(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Get base registry list."""
        arguments = parsers.order_registry_parser.parse_args()
        return marshal(
            services.get_order_registry_data(**arguments),
            swagger_models.OrderRegistryFields.resource_fields,
        )


class OrdersProductsRoute(Resource):
    """Getting Orders products list by base id."""

    @swagger.operation(**schemas.orders_products_get_schema)
    @model_routes.token_required()
    def get(
        self,
        order_id: int,
        *args: typing.Any,
        **kwargs: typing.Any,
    ) -> ResponseReturnValue:
        """Get Orders products list by base id."""
        order_id = order_id_valid(order_id)
        return marshal(
            services.get_order_products_by_order_id(order_id),
            swagger_models.OrdersProductsFields.resource_fields,
        )


class UserOrderRoute(Resource):
    """Create Order by authorized base."""

    @swagger.operation(**schemas.user_order_post_schema)
    @model_routes.token_required()
    def post(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Create Order by authorized base."""
        arguments = parsers.user_order_parser.parse_args()
        current_user: typing.Optional[User] = kwargs.get("current_user")
        if current_user:
            arguments["user_id"] = current_user.id
            return marshal(
                api_services.crud.create(Order, arguments),
                OrderFields.resource_fields,
            )
        return {
            "message": "Authentication token is invalid",
            "data": None,
            "error": "error",
        }, 400


class CounterpartyOrdersRoute(Resource):
    """Get Counterparty Orders list by base id."""

    @swagger.operation(**schemas.counterparty_orders_get_schema)
    @model_routes.token_required()
    def get(
        self,
        company_id: int,
        *args: typing.Any,
        **kwargs: typing.Any,
    ) -> ResponseReturnValue:
        """Get Orders list by base id."""
        company_id = counterparty_id_valid(company_id)
        return marshal(
            api_services.crud.read_many(
                Order,
                {"customer_id": company_id},
                rev=True,
            ),
            OrderFields.resource_fields,
        )


api.add_resource(OrderRegistryRoute, "/order-registry/")
api.add_resource(OrdersProductsRoute, "/orders-products/<order_id>/")
api.add_resource(UserOrderRoute, "/user-order/")
api.add_resource(CounterpartyOrdersRoute, "/orders/<company_id>/")
