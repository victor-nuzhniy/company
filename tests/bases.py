"""Base models for testing section."""
import random
from typing import Type

import factory

from api.common.api_types import ModelType


class BaseModelFactory(factory.alchemy.SQLAlchemyModelFactory):
    """Base model for creating model factories."""

    class Meta:
        """Class Meta for BaseModelFactory."""

        abstract = True
        sqlalchemy_session_persistence = "commit"

    def check_factory(
        self,
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
