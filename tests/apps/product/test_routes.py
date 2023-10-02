"""Module for testing product routes."""
from typing import Dict

from faker import Faker

from api import Product, ProductType
from tests.apps.product.conftest import create_product_data, create_product_type_data
from tests.apps.product.factories import ProductFactory, ProductTypeFactory
from tests.testing_classes import SampleTestRoute


class TestProductTypeRoute(SampleTestRoute):
    """Class with methods for testing ProductType routes."""

    model = ProductType
    factory = ProductTypeFactory

    def get_fake_data(self, faker: Faker) -> Dict:
        """Get ProductType fake data dict."""
        return create_product_type_data(faker)

    def get_fake_put_data(self, faker: Faker) -> Dict:
        """Get ProductType fake data dict for put and patch methods."""
        return create_product_type_data(faker)


class TestProductRoute(SampleTestRoute):
    """Class with methods for testing Product routes."""

    model = Product
    factory = ProductFactory

    def get_fake_data(self, faker: Faker) -> Dict:
        """Get Product fake ddta dict."""
        return create_product_data(faker)

    def get_fake_put_data(self, faker: Faker) -> Dict:
        """Get Product fake data dict for put and patch methods."""
        return create_product_data(faker)
