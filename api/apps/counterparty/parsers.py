"""Parsers for counterparty apps."""
from flask_restful import reqparse
from flask_restful.inputs import int_range

from api.apps.counterparty.validators import (
    counterparty_id,
    discount_id,
    str_hundred_fifty,
    str_hundred_fifty_five,
    str_ten,
    str_thirty,
)
from api.apps.invoice.validators import str_hundred
from api.apps.product.validators import str_length_200

discount_parser = reqparse.RequestParser()
discount_parser.add_argument("name", type=str_thirty, required=True)
discount_parser.add_argument("rate", type=int_range(low=0, high=100), required=True)

discount_patch_parser = reqparse.RequestParser()
discount_patch_parser.add_argument("name", type=str_thirty)
discount_patch_parser.add_argument("rate", type=int_range(low=0, high=100))


counterparty_parser = reqparse.RequestParser()
counterparty_parser.add_argument("name", type=str_hundred_fifty, required=True)
counterparty_parser.add_argument("postal_code", type=str_ten)
counterparty_parser.add_argument("country", type=str_hundred)
counterparty_parser.add_argument("city", type=str_hundred)
counterparty_parser.add_argument("address", type=str_hundred_fifty_five)
counterparty_parser.add_argument("phone_number", type=str_thirty)
counterparty_parser.add_argument("discount_id", type=discount_id, required=True)

counterparty_patch_parser = counterparty_parser.copy()
counterparty_patch_parser.replace_argument("name", type=str_hundred_fifty)
counterparty_patch_parser.replace_argument("discount_id", type=discount_id)


agreement_parser = reqparse.RequestParser()
agreement_parser.add_argument("name", type=str_length_200, required=True)
agreement_parser.add_argument("counterparty_id", type=counterparty_id, required=True)

agreement_patch_parser = reqparse.RequestParser()
agreement_patch_parser.add_argument("name", type=str_length_200, required=False)
agreement_patch_parser.add_argument(
    "counterparty_id",
    type=counterparty_id,
    required=False,
)
