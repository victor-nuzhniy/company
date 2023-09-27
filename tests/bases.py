"""Base models for testing section."""
import random
from typing import Type

import factory

from api import db


class BaseModelFactory(factory.alchemy.SQLAlchemyModelFactory):
    """Base model for creating model factories."""

    class Meta:
        """Class Meta for BaseModelFactory."""

        abstract = True
        sqlalchemy_session_persistence = "commit"

    @staticmethod
    def check_factory(factory_class: Type["BaseModelFactory"], model: db.Model) -> None:
        """Test, that factory creates successfully."""
        obj = factory_class()
        size = random.randint(2, 3)
        objs = factory_class.create_batch(size=size)

        assert isinstance(obj, model)
        assert size == len(objs)
        for i in objs:
            assert isinstance(i, model)
