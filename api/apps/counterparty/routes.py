"""Module for counterparty rounters."""
from flask_restful import Resource, fields, marshal_with

from api import api
from api.apps.counterparty.parsers import discount_parser
from api.services import crud

discount_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "rate": fields.Integer,
}


class Discount(Resource):
    """Operations with single Discount instance."""

    @marshal_with(discount_fields)
    def get(self, discount_id):
        """Get discount by id."""
        discount = crud.read(Discount, {"id": discount_id})
        return discount

    @marshal_with(discount_fields)
    def put(self, discount_id):
        """Update discount by id."""
        args = discount_parser.parse_args()
        discount = crud.update(Discount, args, {"id": discount_id})
        return discount

    @marshal_with(discount_fields)
    def patch(self, discount_id):
        """Update discount by id, partially."""
        args = discount_parser.parse_args()
        args = {key: value for key, value in args.items() if value}
        discount = crud.update(Discount, args, {"id": discount_id})
        return discount

    def delete(self, discount_id):
        """Delete discount by id."""
        crud.delete(Discount, {"id": discount_id})
        return {"message": f"Deleted Discount with id {discount_id}"}


class Discounts(Resource):
    """Operations with many Discounts instances."""

    @marshal_with(discount_fields)
    def post(self):
        """Create discount."""
        args = discount_parser.parse_args()
        discount = crud.create(Discount, args)
        return discount

    @marshal_with(discount_fields)
    def get(self):
        """Get discount list."""
        discounts = crud.read_many(Discount)
        return discounts


api.add_resource(Discount, "/discount/<discount_id>/")
api.add_resource(Discounts, "/discount/")
