"""Tests for base apps models."""
from api import Product, ProductType
from tests.apps.product.base.factories import ProductFactory, ProductTypeFactory
from tests.bases import BaseModelFactory


class TestProduct:
    """Class for testing Product model."""

    def test_factory(self) -> None:
        """Test Product model instance creation."""
        BaseModelFactory.check_factory(factory_class=ProductFactory, model=Product)

    def test_repr(self) -> None:
        """Test Product __repr__ method."""
        instance: Product = ProductFactory()
        expected_result: str = str(instance.name)
        assert expected_result == str(instance)


class TestProductType:
    """Class for testing ProductType model."""

    def test_factory(self) -> None:
        """Test ProductType model instance creation."""
        BaseModelFactory.check_factory(
            factory_class=ProductTypeFactory,
            model=ProductType,
        )

    def test_repr(self) -> None:
        """Test ProductType __repr__ method."""
        instance: ProductType = ProductTypeFactory()
        expected_result: str = str(instance.name)
        assert expected_result == str(instance)
