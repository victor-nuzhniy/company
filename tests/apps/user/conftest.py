"""Fixtures for user apps."""
from typing import Dict

from faker import Faker


def create_user_data(faker: Faker) -> Dict:
    """Create User fake data."""
    return {
        "username": faker.user_name(),
        "email": faker.email(),
        "password": faker.pystr(min_chars=40, max_chars=104),
    }


def create_user_put_data(faker: Faker) -> Dict:
    """Create User fake data."""
    return {
        "username": faker.user_name(),
        "email": faker.email(),
        "password": faker.pystr(min_chars=1, max_chars=10),
        "is_active": faker.pybool(),
        "is_admin": faker.pybool(),
    }
