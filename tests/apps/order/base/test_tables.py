"""Tests for base apps models."""
from api import Order, OrderProduct
from tests.apps.order.base.factories import OrderFactory, OrderProductFactory
from tests.bases import BaseModelFactory


class TestOrder:
    """Class for testing Order model."""

    def test_factory(self) -> None:
        """Test Order model instance creation."""
        BaseModelFactory.check_factory(factory_class=OrderFactory, model=Order)

    def test_repr(self) -> None:
        """Test Order __repr__ method."""
        instance: Order = OrderFactory()
        expected_result: str = str(instance.name)
        assert expected_result == str(instance)


class TestOrderProduct:
    """Class for testing OrderProduct model."""

    def test_factory(self) -> None:
        """Test OrderProduct model instance creation."""
        BaseModelFactory.check_factory(
            factory_class=OrderProductFactory,
            model=OrderProduct,
        )

    def test_repr(self) -> None:
        """Test OrderProduct __repr__ method."""
        instance: OrderProduct = OrderProductFactory()
        expected_result: str = "Order product with id {id}".format(
            id=instance.product_id,
        )
        assert expected_result == str(instance)
