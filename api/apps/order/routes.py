"""Routes for order apps."""
from flask_restful import fields

from api import Order, OrderProducts, api
from api.apps.order.parsers import (
    order_parser,
    order_patch_parser,
    order_products_parser,
    order_products_patch_parser,
)
from api.model_routes import ModelRoute, ModelsRoute

order_fields = {
    "id": fields.Integer,
    "user_id": fields.Integer,
    "name": fields.String,
    "created_at": fields.DateTime,
    "customer_id": fields.Integer,
}

order_products_fields = {
    "id": fields.Integer,
    "product_id": fields.Integer,
    "quantity": fields.Integer,
    "price": fields.Integer,
    "order_id": fields.Integer,
}


class OrderRoute(ModelRoute):
    """Operations with single Order instance."""

    model = Order
    put_parser = order_parser
    patch_parser = order_patch_parser
    model_fields = order_fields


class OrdersRoute(ModelsRoute):
    """Operations with many Order instances and instance creation."""

    model = Order
    post_parser = order_parser
    model_fields = order_fields


class OrderProductsRoute(ModelRoute):
    """Operations with single OrderProducts instance."""

    model = OrderProducts
    put_parser = order_products_parser
    patch_parser = order_products_patch_parser
    model_fields = order_products_fields


class ManyOrderProductsRoute(ModelsRoute):
    """Operations with many OrderProducts and instance creation."""

    model = OrderProducts
    post_parser = order_products_parser
    model_fields = order_products_fields


api.add_resource(OrderRoute, "/order/<instance_id>")
api.add_resource(OrdersRoute, "/order/")
api.add_resource(OrderProductsRoute, "/order-products/<instance_id>")
api.add_resource(ManyOrderProductsRoute, "/order-products/")
