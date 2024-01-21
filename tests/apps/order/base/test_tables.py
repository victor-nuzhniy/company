"""Tests for base apps models."""
from api import Order, OrderProduct
from tests.apps.order.base.factories import OrderFactory, OrderProductFactory
from tests.bases import BaseModelFactory


class TestOrder:
    """Class for testing Order model."""

    def test_factory(self) -> None:
        """Test Order model instance creation."""
        BaseModelFactory.check_factory(factory_class=OrderFactory, model=Order)

    def test__repr__(self) -> None:
        """Test Order __repr__ method."""
        obj: Order = OrderFactory()
        expected_result: str = str(obj.name)
        assert expected_result == obj.__repr__()


class TestOrderProduct:
    """Class for testing OrderProduct model."""

    def test_factory(self) -> None:
        """Test OrderProduct model instance creation."""
        BaseModelFactory.check_factory(
            factory_class=OrderProductFactory, model=OrderProduct
        )

    def test__repr__(self) -> None:
        """Test OrderProduct __repr__ method."""
        obj: OrderProduct = OrderProductFactory()
        expected_result: str = f"Order product with id {obj.product_id}"
        assert expected_result == obj.__repr__()
