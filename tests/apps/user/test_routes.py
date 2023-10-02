"""Module for testing user apps routes."""
from typing import Dict

from faker import Faker

from api import User
from tests.apps.user.conftest import create_user_data, create_user_put_data
from tests.apps.user.factories import UserFactory
from tests.testing_classes import SampleTestRoute


class TestUserRoutes(SampleTestRoute):
    """Class with methods for testing User routes."""

    model = User
    factory = UserFactory

    def get_fake_data(self, faker: Faker) -> Dict:
        """Get User fake data dict."""
        return create_user_data(faker)

    def get_fake_put_data(self, faker: Faker) -> Dict:
        """Get User fake data dict for put and patch methods."""
        return create_user_put_data(faker)
