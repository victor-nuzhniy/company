"""Tests for base apps models."""
from api import User
from tests.apps.user.base.factories import UserFactory
from tests.bases import BaseModelFactory


class TestUser:
    """Class for testing User model."""

    def test_factory(self) -> None:
        """Test User model instance creation."""
        BaseModelFactory.check_factory(factory_class=UserFactory, model=User)

    def test__repr__(self) -> None:
        """Test base __repr__ method."""
        obj: User = UserFactory()
        expected_result: str = str(obj.username)
        assert expected_result == obj.__repr__()
