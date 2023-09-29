"""Validators for product apps."""
from api.apps.product.models import ProductType
from api.services import db_utils


def str_length_200(name_str):
    """Validate discount_name."""
    if len(name_str) > 200:
        raise ValueError(f"{name_str} length should be lower than 200 character.")
    return name_str


def str_length_15(name_str):
    """Validate discount_name."""
    if len(name_str) > 15:
        raise ValueError(f"{name_str} length should be lower than 15 character.")
    return name_str


def product_type_id(product_type_id_int: int) -> int:
    """Validate product_type_id."""
    if db_utils.is_exists(ProductType, {"id": product_type_id_int}):
        return product_type_id_int
    raise ValueError(f"SaleInvoice with id {product_type_id_int} does not exist.")
