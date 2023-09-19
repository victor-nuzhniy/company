"""Parsers for invoice apps."""
from flask_restful import reqparse
from flask_restful.inputs import boolean, datetime_from_iso8601

invoice_parser = reqparse.RequestParser()
invoice_parser.add_argument("name", required=True)
invoice_parser.add_argument("order_id", type=int, required=True)
invoice_parser.add_argument("agreement_id", type=int, required=True)

invoice_patch_parser = reqparse.RequestParser()
invoice_parser.add_argument("name", required=False)
invoice_patch_parser.add_argument("order_id", type=int, required=False)
invoice_patch_parser.add_argument(
    "created_at", type=datetime_from_iso8601, required=False
)
invoice_patch_parser.add_argument("paid", type=boolean, required=False)
invoice_patch_parser.add_argument("agreement_id", type=int, required=False)
