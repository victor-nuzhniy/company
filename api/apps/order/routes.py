"""Routes for order apps."""
from flask_restful import fields
from flask_restful_swagger import swagger

from api import Order, OrderProduct, api
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
from api.common import CustomDateTimeFormat
from api.model_routes import ModelRoute, ModelsRoute, token_required


@swagger.model
class OrderFields:
    """OrderRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "user_id": fields.Integer,
        "name": fields.String,
        "created_at": CustomDateTimeFormat,
        "customer_id": fields.Integer,
    }


@swagger.model
class OrderProductFields:
    """OrderProductRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "product_id": fields.Integer,
        "quantity": fields.Integer,
        "price": fields.Integer,
        "order_id": fields.Integer,
    }


class OrderRoute(ModelRoute):
    """Operations with single Order instance."""

    model = Order
    put_parser = order_put_parser
    patch_parser = order_patch_parser
    model_fields = OrderFields.resource_fields

    @swagger.operation(**order_get_schema)
    @token_required()
    def get(self, *args, **kwargs):
        """Get model instance by id."""
        return super().get(*args, **kwargs)

    @swagger.operation(**order_put_schema)
    @token_required()
    def put(self, *args, **kwargs):
        """Update instance by id."""
        return super().put(*args, **kwargs)

    @swagger.operation(**order_patch_schema)
    @token_required()
    def patch(self, *args, **kwargs):
        """Update instance bu id, partially."""
        return super().patch(*args, **kwargs)

    @swagger.operation(**order_delete_schema)
    @token_required()
    def delete(self, *args, **kwargs):
        """Delete instance by id."""
        return super().delete(*args, **kwargs)


class OrdersRoute(ModelsRoute):
    """Operations with many Order instances and instance creation."""

    model = Order
    post_parser = order_post_parser
    model_fields = OrderFields.resource_fields

    @swagger.operation(**order_post_schema)
    @token_required()
    def post(self, *args, **kwargs):
        """Create model instance."""
        return super().post(*args, **kwargs)

    @swagger.operation(**orders_get_schema)
    @token_required()
    def get(self, *args, **kwargs):
        """Get model instance list."""
        return super().get(*args, **kwargs)


class OrderProductRoute(ModelRoute):
    """Operations with single OrderProducts instance."""

    model = OrderProduct
    put_parser = order_product_parser
    patch_parser = order_product_patch_parser
    model_fields = OrderProductFields.resource_fields

    @swagger.operation(**order_product_get_schema)
    @token_required()
    def get(self, *args, **kwargs):
        """Get model instance by id."""
        return super().get(*args, **kwargs)

    @swagger.operation(**order_product_put_schema)
    @token_required()
    def put(self, *args, **kwargs):
        """Update instance by id."""
        return super().put(*args, **kwargs)

    @swagger.operation(**order_product_patch_schema)
    @token_required()
    def patch(self, *args, **kwargs):
        """Update instance by id, partially."""
        return super().patch(*args, **kwargs)

    @swagger.operation(**order_product_delete_schema)
    @token_required()
    def delete(self, *args, **kwargs):
        """Delete instance by id."""
        return super().delete(*args, **kwargs)


class OrderProductsRoute(ModelsRoute):
    """Operations with many OrderProducts and instance creation."""

    model = OrderProduct
    post_parser = order_product_parser
    model_fields = OrderProductFields.resource_fields

    @swagger.operation(**order_product_post_schema)
    @token_required()
    def post(self, *args, **kwargs):
        """Create model instance."""
        return super().post(*args, **kwargs)

    @swagger.operation(**order_products_get_schema)
    @token_required()
    def get(self, *args, **kwargs):
        """Get model instance list."""
        return super().get(*args, **kwargs)


api.add_resource(OrderRoute, "/order/<instance_id>/")
api.add_resource(OrdersRoute, "/order/")
api.add_resource(OrderProductRoute, "/order-product/<instance_id>/")
api.add_resource(OrderProductsRoute, "/order-product/")
