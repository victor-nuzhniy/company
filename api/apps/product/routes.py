"""Routes for product apps."""
from flask_restful import fields
from flask_restful_swagger import swagger

from api import Product, api
from api.apps.product.models import ProductType
from api.apps.product.parsers import (
    product_parser,
    product_patch_parser,
    product_type_parser,
    product_type_patch_parser,
)
from api.model_routes import ModelRoute, ModelsRoute


@swagger.model
class ProductFields:
    """ProfudctFieldsRoute output fields."""

    resource_fields = {
        "id": fields.Integer,
        "name": fields.String,
        "code": fields.String,
        "units": fields.String,
        "currency": fields.String,
        "price": fields.Integer,
        "product_type_id": fields.Integer,
    }


@swagger.model
class ProductTypeFields:
    """ProductTypeRoute output fields."""

    resource_fields = {"id": fields.Integer, "name": fields.String}


class ProductRoute(ModelRoute):
    """Operations with single Product instance."""

    model = Product
    put_parser = product_parser
    patch_parser = product_patch_parser
    model_fields = ProductFields.resource_fields

    @swagger.operation()
    def get(self, *args, **kwargs):
        """Get model instance by id."""
        return super().get(*args, **kwargs)

    @swagger.operation()
    def put(self, *args, **kwargs):
        """Update instance by id."""
        return super().put(*args, **kwargs)

    @swagger.operation()
    def patch(self, *args, **kwargs):
        """Update instance bu id, partially."""
        return super().patch(*args, **kwargs)

    @swagger.operation()
    def delete(self, *args, **kwargs):
        """Delete instance by id."""
        return super().delete(*args, **kwargs)


class ProductsRoute(ModelsRoute):
    """Operations with many Product instance and instance creation."""

    model = Product
    post_parser = product_parser
    model_fields = ProductFields.resource_fields

    @swagger.operation()
    def post(self, *args, **kwargs):
        """Create model instance."""
        return super().post(*args, **kwargs)

    @swagger.operation()
    def get(self, *args, **kwargs):
        """Get model instance list."""
        return super().get(*args, **kwargs)


class ProductTypeRoute(ModelRoute):
    """Operations with single ProductType instance."""

    model = ProductType
    put_parser = product_type_parser
    patch_parser = product_type_patch_parser
    model_fields = ProductTypeFields.resource_fields

    @swagger.operation()
    def get(self, *args, **kwargs):
        """Get model instance by id."""
        return super().get(*args, **kwargs)

    @swagger.operation()
    def put(self, *args, **kwargs):
        """Update instance by id."""
        return super().put(*args, **kwargs)

    @swagger.operation()
    def patch(self, *args, **kwargs):
        """Update instance bu id, partially."""
        return super().patch(*args, **kwargs)

    @swagger.operation()
    def delete(self, *args, **kwargs):
        """Delete instance by id."""
        return super().delete(*args, **kwargs)


class ProductTypesRoute(ModelsRoute):
    """Operations with many Product instance and instance creation."""

    model = ProductType
    post_parser = product_type_parser
    model_fields = ProductTypeFields.resource_fields

    @swagger.operation()
    def post(self, *args, **kwargs):
        """Create model instance."""
        return super().post(*args, **kwargs)

    @swagger.operation()
    def get(self, *args, **kwargs):
        """Get model instance list."""
        return super().get(*args, **kwargs)


api.add_resource(ProductRoute, "/product/<instance_id>")
api.add_resource(ProductsRoute, "/product/")
api.add_resource(ProductTypeRoute, "/product-type/<instance_id>")
api.add_resource(ProductTypesRoute, "/product-type/")
