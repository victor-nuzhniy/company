"""Routes for product apps."""
import typing

from flask.typing import ResponseReturnValue
from flask_restful_swagger import swagger

from api import Product, api
from api.apps.product.models import ProductType
from api.apps.product.parsers import (
    product_parser,
    product_patch_parser,
    product_type_parser,
    product_type_patch_parser,
)
from api.apps.product.schemas import (
    product_delete_schema,
    product_get_schema,
    product_patch_schema,
    product_post_schema,
    product_put_schema,
    product_type_delete_schema,
    product_type_get_schema,
    product_type_patch_schema,
    product_type_post_schema,
    product_type_put_schema,
    product_types_get_schema,
    products_get_schema,
)
from api.apps.product.swagger_models import ProductFields, ProductTypeFields
from api.model_routes import ModelRoute, ModelsRoute, token_required


class ProductRoute(ModelRoute):
    """Operations with single Product instance."""

    model = Product
    put_parser = product_parser
    patch_parser = product_patch_parser
    model_fields = ProductFields.resource_fields

    @swagger.operation(**product_get_schema)
    @token_required()
    def get(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Get model instance by id."""
        return super().get(*args, **kwargs)

    @swagger.operation(**product_put_schema)
    @token_required()
    def put(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Update instance by id."""
        return super().put(*args, **kwargs)

    @swagger.operation(**product_patch_schema)
    @token_required()
    def patch(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Update instance bu id, partially."""
        return super().patch(*args, **kwargs)

    @swagger.operation(**product_delete_schema)
    @token_required()
    def delete(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Delete instance by id."""
        return super().delete(*args, **kwargs)


class ProductsRoute(ModelsRoute):
    """Operations with many Product instance and instance creation."""

    model = Product
    post_parser = product_parser
    model_fields = ProductFields.resource_fields

    @swagger.operation(**product_post_schema)
    @token_required()
    def post(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Create model instance."""
        return super().post(*args, **kwargs)

    @swagger.operation(**products_get_schema)
    @token_required()
    def get(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Get model instance list."""
        return super().get(*args, **kwargs)


class ProductTypeRoute(ModelRoute):
    """Operations with single ProductType instance."""

    model = ProductType
    put_parser = product_type_parser
    patch_parser = product_type_patch_parser
    model_fields = ProductTypeFields.resource_fields

    @swagger.operation(**product_type_get_schema)
    @token_required()
    def get(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Get model instance by id."""
        return super().get(*args, **kwargs)

    @swagger.operation(**product_type_put_schema)
    @token_required()
    def put(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Update instance by id."""
        return super().put(*args, **kwargs)

    @swagger.operation(**product_type_patch_schema)
    @token_required()
    def patch(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Update instance bu id, partially."""
        return super().patch(*args, **kwargs)

    @swagger.operation(**product_type_delete_schema)
    @token_required()
    def delete(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Delete instance by id."""
        return super().delete(*args, **kwargs)


class ProductTypesRoute(ModelsRoute):
    """Operations with many Product instance and instance creation."""

    model = ProductType
    post_parser = product_type_parser
    model_fields = ProductTypeFields.resource_fields

    @swagger.operation(**product_type_post_schema)
    @token_required()
    def post(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Create model instance."""
        return super().post(*args, **kwargs)

    @swagger.operation(**product_types_get_schema)
    @token_required()
    def get(self, *args: typing.Any, **kwargs: typing.Any) -> ResponseReturnValue:
        """Get model instance list."""
        return super().get(*args, **kwargs)


api.add_resource(ProductRoute, "/product/<instance_id>/")
api.add_resource(ProductsRoute, "/product/")
api.add_resource(ProductTypeRoute, "/product-type/<instance_id>/")
api.add_resource(ProductTypesRoute, "/product-type/")
