"""Validators for product base apps."""
from api import ProductType
from api.common.services import db_utils


def str_two_hundred(name_str: str) -> str:
    """Validate discount_name."""
    if len(name_str) > 200:
        raise ValueError(
            "{name} length should be lower than 200 character.".format(name=name_str),
        )
    return name_str


def str_fifteen(name_str: str) -> str:
    """Validate discount_name."""
    if len(name_str) > 15:
        raise ValueError(
            "{name} length should be lower than 15 character.".format(name=name_str),
        )
    return name_str


def product_type_id(product_type_id_int: int) -> int:
    """Validate product_type_id."""
    if db_utils.is_exists(ProductType, {"id": product_type_id_int}):
        return product_type_id_int
    raise ValueError(
        "Product type with id {id} does not exist.".format(
            id=product_type_id_int,
        ),
    )
