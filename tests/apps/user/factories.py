"""Factories for user apps."""

import factory

from api import User
from tests.bases import BaseModelFactory


class UserFactory(BaseModelFactory):
    """Factory for testing User model."""

    id = factory.Sequence(lambda x: x)
    username = factory.Faker("user_name")
    email = factory.Faker("email")
    password = factory.Faker("pystr", min_chars=1, max_chars=120)
    is_admin = factory.Faker("pybool")
    is_active = factory.Faker("pybool")
    # orders = factory.RelatedFactoryList(
    #     factory="tests.apps.order.factories.OrderFactory",
    #     factory_related_name="orders",
    #     size=0,
    # )

    @classmethod
    def _setup_next_sequence(cls):
        return 1

    class Meta:
        """Class Meta for UserFactory."""

        model = User
        # exclude = ("orders",)
