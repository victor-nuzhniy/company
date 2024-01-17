"""Routes for order apps."""
import typing

from flask.typing import ResponseReturnValue
from flask_restful_swagger import swagger

from api import Order, OrderProduct, api, model_routes
from api.apps.order.parsers import (
    order_patch_parser,
    order_post_parser,
    order_product_parser,
    order_product_patch_parser,
    order_put_parser,
)
from api.apps.order.schemas import (
    order_delete_schema,
    order_get_schema,
    order_patch_schema,
    order_post_schema,
    order_product_delete_schema,
    order_product_get_schema,
    order_product_patch_schema,
    order_product_post_schema,
    order_product_put_schema,
    order_products_get_schema,
    order_put_schema,
    orders_get_schema,
)
from api.apps.order.swagger_models import OrderFields, OrderProductFields


class OrderRoute(model_routes.ModelRoute):
    """Operations with single Order instance."""

    model = Order
    put_parser = order_put_parser
    patch_parser = order_patch_parser
    model_fields = OrderFields.resource_fields

    @swagger.operation(**order_get_schema)
    @model_routes.token_required()
    def get(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Get model instance by id."""
        return super().get(*args, **kwargs)

    @swagger.operation(**order_put_schema)
    @model_routes.token_required()
    def put(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Update instance by id."""
        return super().put(*args, **kwargs)

    @swagger.operation(**order_patch_schema)
    @model_routes.token_required()
    def patch(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Update instance bu id, partially."""
        return super().patch(*args, **kwargs)

    @swagger.operation(**order_delete_schema)
    @model_routes.token_required()
    def delete(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Delete instance by id."""
        return super().delete(*args, **kwargs)


class OrdersRoute(model_routes.ModelsRoute):
    """Operations with many Order instances and instance creation."""

    model = Order
    post_parser = order_post_parser
    model_fields = OrderFields.resource_fields

    @swagger.operation(**order_post_schema)
    @model_routes.token_required()
    def post(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Create model instance."""
        return super().post(*args, **kwargs)

    @swagger.operation(**orders_get_schema)
    @model_routes.token_required()
    def get(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Get model instance list."""
        return super().get(*args, **kwargs)


class OrderProductRoute(model_routes.ModelRoute):
    """Operations with single OrderProducts instance."""

    model = OrderProduct
    put_parser = order_product_parser
    patch_parser = order_product_patch_parser
    model_fields = OrderProductFields.resource_fields

    @swagger.operation(**order_product_get_schema)
    @model_routes.token_required()
    def get(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Get model instance by id."""
        return super().get(*args, **kwargs)

    @swagger.operation(**order_product_put_schema)
    @model_routes.token_required()
    def put(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Update instance by id."""
        return super().put(*args, **kwargs)

    @swagger.operation(**order_product_patch_schema)
    @model_routes.token_required()
    def patch(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Update instance by id, partially."""
        return super().patch(*args, **kwargs)

    @swagger.operation(**order_product_delete_schema)
    @model_routes.token_required()
    def delete(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Delete instance by id."""
        return super().delete(*args, **kwargs)


class OrderProductsRoute(model_routes.ModelsRoute):
    """Operations with many OrderProducts and instance creation."""

    model = OrderProduct
    post_parser = order_product_parser
    model_fields = OrderProductFields.resource_fields

    @swagger.operation(**order_product_post_schema)
    @model_routes.token_required()
    def post(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Create model instance."""
        return super().post(*args, **kwargs)

    @swagger.operation(**order_products_get_schema)
    @model_routes.token_required()
    def get(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Get model instance list."""
        return super().get(*args, **kwargs)


api.add_resource(OrderRoute, "/order/<instance_id>/")
api.add_resource(OrdersRoute, "/order/")
api.add_resource(OrderProductRoute, "/order-product/<instance_id>/")
api.add_resource(OrderProductsRoute, "/order-product/")
