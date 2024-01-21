"""Tests for base apps models."""
from api import Product, ProductType
from tests.apps.product.base.factories import ProductFactory, ProductTypeFactory
from tests.bases import BaseModelFactory


class TestProduct:
    """Class for testing Product model."""

    def test_factory(self) -> None:
        """Test Product model instance creation."""
        BaseModelFactory.check_factory(factory_class=ProductFactory, model=Product)

    def test__repr__(self) -> None:
        """Test Product __repr__ method."""
        obj: Product = ProductFactory()
        expected_result: str = str(obj.name)
        assert expected_result == obj.__repr__()


class TestProductType:
    """Class for testing ProductType model."""

    def test_factory(self) -> None:
        """Test ProductType model instance creation."""
        BaseModelFactory.check_factory(
            factory_class=ProductTypeFactory, model=ProductType
        )

    def test__repr__(self) -> None:
        """Test ProductType __repr__ method."""
        obj: ProductType = ProductTypeFactory()
        expected_result: str = str(obj.name)
        assert expected_result == obj.__repr__()
