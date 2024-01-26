"""Base models for testing section."""
import random
from typing import Protocol, Type

import factory
from flask.testing import FlaskClient

from api.common.api_types import ModelType


class BaseModelFactory(factory.alchemy.SQLAlchemyModelFactory):
    """Base model for creating model factories."""

    class Meta:
        """Class Meta for BaseModelFactory."""

        abstract = True
        sqlalchemy_session_persistence = "commit"

    @staticmethod
    def check_factory(  # noqa WPS602
        factory_class: Type["BaseModelFactory"],
        model: ModelType,
    ) -> None:
        """Test, that factory creates successfully."""
        instance = factory_class()
        size = random.randint(2, 3)
        instances = factory_class.create_batch(size=size)

        assert isinstance(instance, model)
        assert size == len(instances)
        for index in instances:
            assert isinstance(index, model)


class TestType(Protocol):
    """Type for instance with client attr."""

    @property
    def client(self) -> FlaskClient:
        """Client attr."""
