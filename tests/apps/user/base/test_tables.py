"""Tests for base apps models."""
from api import User
from tests.apps.user.base.factories import UserFactory
from tests.bases import BaseModelFactory


class TestUser:
    """Class for testing User model."""

    def test_factory(self) -> None:
        """Test User model instance creation."""
        BaseModelFactory.check_factory(factory_class=UserFactory, model=User)

    def test_repr(self) -> None:
        """Test base __repr__ method."""
        instance: User = UserFactory()
        expected_result: str = str(instance.username)
        assert expected_result == str(instance)
