"""Module for testing base routes."""
from typing import Dict

from faker import Faker

from api import Order, OrderProduct
from tests.apps.order.base.factories import OrderFactory, OrderProductFactory
from tests.apps.order.base.testing_utilities import (
    create_order_data,
    create_order_product_data,
    create_order_put_data,
)
from tests.testing_classes import SampleTestRoute


class TestOrderRoute(SampleTestRoute):
    """Class with methods for testing Order routes."""

    model = Order
    factory = OrderFactory

    def get_fake_data(self, faker: Faker) -> Dict:
        """Get Order fake data dict."""
        return create_order_data(faker)

    def get_fake_put_data(self, faker: Faker) -> Dict:
        """Get Oder fake data dict for put and patch methods."""
        return create_order_put_data(faker)


class TestOrderProductRoute(SampleTestRoute):
    """Class with methods for testing OrderProduct routes."""

    model = OrderProduct
    factory = OrderProductFactory

    def get_fake_data(self, faker: Faker) -> Dict:
        """Get OrderProduct fake data dict."""
        return create_order_product_data(faker)

    def get_fake_put_data(self, faker: Faker) -> Dict:
        """Get OderProduct fake data dict for put and patch methods."""
        return create_order_product_data(faker)
