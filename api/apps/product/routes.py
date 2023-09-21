"""Routes for product apps."""
from flask_restful import fields

from api import Product, api
from api.apps.product.models import ProductType
from api.apps.product.parsers import (
    product_parser,
    product_patch_parser,
    product_type_parser,
    product_type_patch_parser,
)
from api.model_routes import ModelRoute, ModelsRoute

product_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "code": fields.String,
    "units": fields.String,
    "currency": fields.String,
    "price": fields.Integer,
    "product_type_id": fields.Integer,
}

product_type_fields = {"id": fields.Integer, "name": fields.String}


class ProductRoute(ModelRoute):
    """Operations with single Product instance."""

    model = Product
    put_parser = product_parser
    patch_parser = product_patch_parser
    model_fields = product_fields


class ProductsRoute(ModelsRoute):
    """Operations with many Product instance and instance creation."""

    model = Product
    post_parser = product_parser
    model_fields = product_fields


class ProductTypeRoute(ModelRoute):
    """Operations with single ProductType instance."""

    model = ProductType
    put_parser = product_type_parser
    patch_parser = product_type_patch_parser
    model_fields = product_type_fields


class ProductTypesRoute(ModelsRoute):
    """Operations with many Product instance and instance creation."""

    model = ProductType
    post_parser = product_type_parser
    model_fields = product_type_fields


api.add_resource(ProductRoute, "/product/<instance_id>")
api.add_resource(ProductsRoute, "/product/")
api.add_resource(ProductTypeRoute, "/product-type/<instance_id>")
api.add_resource(ProductTypesRoute, "/product-type/")
