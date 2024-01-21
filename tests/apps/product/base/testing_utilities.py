"""Fixtures for product apps."""
from typing import Dict

from faker import Faker

from api import ProductType
from tests.apps.product.base.factories import ProductTypeFactory


def create_product_type_data(faker: Faker) -> Dict:
    """Create ProductType fake data."""
    return {"name": faker.pystr(min_chars=1, max_chars=100)}


def create_product_data(faker: Faker) -> Dict:
    """Create Product fake data."""
    product_type: ProductType = ProductTypeFactory()
    return {
        "name": faker.pystr(min_chars=1, max_chars=200),
        "code": faker.pystr(min_chars=1, max_chars=100),
        "units": faker.pystr(min_chars=1, max_chars=100),
        "currency": faker.currency_code(),
        "price": faker.pyint(),
        "product_type_id": product_type.id,
    }
