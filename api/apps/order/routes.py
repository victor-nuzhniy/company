"""Routes for order apps."""
from flask_restful import Resource, fields, marshal
from flask_restful_swagger import swagger

from api import Order, OrderProduct, api
from api.apps.invoice.validators import order_id as order_id_validator
from api.apps.order.parsers import (
    order_patch_parser,
    order_post_parser,
    order_product_parser,
    order_product_patch_parser,
    order_put_parser,
    order_registry_parser,
    user_order_parser,
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
    order_registry_get_schema,
    orders_get_schema,
    orders_products_get_schema,
    user_order_post_schema,
)
from api.apps.order.services import (
    get_order_products_by_order_id,
    get_order_registry_data,
)
from api.common import CustomDateTimeFormat
from api.model_routes import ModelRoute, ModelsRoute, token_required
from api.services import crud


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


@swagger.model
class OrderRegistryFields:
    """OrderRegistryRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "username": fields.String,
        "order_name": fields.String,
        "created_at": CustomDateTimeFormat,
        "customer": fields.String,
        "summ": fields.Integer,
        "currency": fields.String,
    }


@swagger.model
class OrdersProductsFields:
    """OrdersProductsRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "product_id": fields.Integer,
        "quantity": fields.Integer,
        "price": fields.Integer,
        "order_id": fields.Integer,
        "name": fields.String,
        "code": fields.String,
        "currency": fields.String,
        "units": fields.String,
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


class OrderRegistryRoute(Resource):
    """Order registry information."""

    @swagger.operation(**order_registry_get_schema)
    @token_required()
    def get(self, *args, **kwargs):
        """Get order registry list."""
        args = order_registry_parser.parse_args()
        return marshal(
            get_order_registry_data(**args),
            OrderRegistryFields.resource_fields,
        )


class OrdersProductsRoute(Resource):
    """Getting Orders products list by order id."""

    @swagger.operation(**orders_products_get_schema)
    @token_required()
    def get(self, order_id, *args, **kwargs):
        """Get Orders products list by order id."""
        order_id = order_id_validator(order_id)
        return marshal(
            get_order_products_by_order_id(order_id),
            OrdersProductsFields,
        )


class UserOrderRoute(Resource):
    """Create Order by authorized user."""

    @swagger.operation(**user_order_post_schema)
    @token_required()
    def post(self, *args, **kwargs):
        """Create Order by authorized user."""
        args = user_order_parser.parse_args()
        args["user_id"] = kwargs.get("current_user").id
        return marshal(crud.create(Order, args), OrderFields.resource_fields)


api.add_resource(OrderRoute, "/order/<instance_id>/")
api.add_resource(OrdersRoute, "/order/")
api.add_resource(OrderProductRoute, "/order-product/<instance_id>/")
api.add_resource(OrderProductsRoute, "/order-product/")
api.add_resource(OrderRegistryRoute, "/order-registry/")
api.add_resource(OrdersProductsRoute, "/orders-products/<order_id>/")
api.add_resource(UserOrderRoute, "/user-order/")
