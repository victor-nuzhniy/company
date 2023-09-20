"""Routes for product apps."""
from flask_restful import fields

from api import Product, api
from api.apps.product.parsers import product_parser, product_patch_parser
from api.model_routes import ModelRoute, ModelsRoute

product_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "code": fields.String,
    "units": fields.String,
    "price": fields.Integer,
}


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


api.add_resource(ProductRoute, "/product/<instance_id>")
api.add_resource(ProductsRoute, "/product/")
