"""Fixtures for counterparty apps."""
from typing import Dict

from faker import Faker

from api import Counterparty, Discount
from tests.apps.counterparty.factories import CounterpartyFactory, DiscountFactory


def create_discount_data(faker: Faker) -> Dict:
    """Create Discount fake data."""
    return {
        "name": faker.pystr(min_chars=4, max_chars=10),
        "rate": faker.random_int(min=0, max=100),
    }


def create_agreement_data(faker: Faker) -> Dict:
    """Create Agreement fake data."""
    counterparty: Counterparty = CounterpartyFactory()
    return {
        "name": faker.pystr(min_chars=1, max_chars=200),
        "counterparty_id": counterparty.id,
    }


def create_counterparty_data(faker: Faker) -> Dict:
    """Create Counterparty fake data."""
    discount: Discount = DiscountFactory()
    return {
        "name": faker.pystr(min_chars=1, max_chars=150),
        "postal_code": faker.pystr(max_chars=10),
        "country": faker.country(),
        "city": faker.city(),
        "address": faker.address(),
        "phone_number": faker.phone_number(),
        "discount_id": discount.id,
    }
