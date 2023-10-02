"""Fixtures for order apps."""
from typing import Dict

from faker import Faker

from api import Counterparty, Order, Product, User
from tests.apps.counterparty.factories import CounterpartyFactory
from tests.apps.order.factories import OrderFactory
from tests.apps.product.factories import ProductFactory
from tests.apps.user.factories import UserFactory


def create_order_data(faker: Faker) -> Dict:
    """Create Order fake data."""
    user: User = UserFactory()
    counterparty: Counterparty = CounterpartyFactory()
    return {
        "user_id": user.id,
        "name": faker.user_name(),
        "customer_id": counterparty.id,
    }


def create_order_put_data(faker: Faker) -> Dict:
    """Create Order fake data for put and patch methods.."""
    user: User = UserFactory()
    counterparty: Counterparty = CounterpartyFactory()
    return {
        "user_id": user.id,
        "name": faker.user_name(),
        "created_at": faker.date_time().strftime("%Y-%m-%dT%H:%M:%S"),
        "customer_id": counterparty.id,
    }


def create_order_product_data(faker: Faker) -> Dict:
    """Create OrderProduct fake data."""
    product: Product = ProductFactory()
    order: Order = OrderFactory()
    return {
        "product_id": product.id,
        "quantity": faker.pyint(),
        "price": faker.pyint(),
        "order_id": order.id,
    }
