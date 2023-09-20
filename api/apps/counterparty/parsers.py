"""Parsers for counterparty apps."""
from flask_restful import reqparse
from flask_restful.inputs import int_range

from api.apps.counterparty.validators import counterparty_id, discount_id, discount_name

discount_parser = reqparse.RequestParser()
discount_parser.add_argument("name", type=discount_name, required=True)
discount_parser.add_argument("rate", type=int_range(low=0, high=100), required=True)

discount_patch_parser = reqparse.RequestParser()
discount_patch_parser.add_argument("name", type=discount_name)
discount_patch_parser.add_argument("rate", type=int_range(low=0, high=100))

counterparty_parser = reqparse.RequestParser()
counterparty_parser.add_argument("name", required=True)
counterparty_parser.add_argument("postal_code")
counterparty_parser.add_argument("country")
counterparty_parser.add_argument("city")
counterparty_parser.add_argument("address")
counterparty_parser.add_argument("phone_number")
counterparty_parser.add_argument("discount_id", type=discount_id, required=True)

counterparty_patch_parser = counterparty_parser.copy()
counterparty_patch_parser.replace_argument("name")
counterparty_patch_parser.replace_argument("discount_id", type=discount_id)


agreement_parser = reqparse.RequestParser()
agreement_parser.add_argument("name", required=True)
agreement_parser.add_argument("counterparty_id", type=counterparty_id, required=True)

agreement_patch_parser = reqparse.RequestParser()
agreement_patch_parser.add_argument("name")
agreement_patch_parser.add_argument("counterparty_id", type=counterparty_id)
