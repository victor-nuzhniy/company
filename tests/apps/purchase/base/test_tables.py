"""Tests for base apps models."""
from api import PurchaseInvoice, PurchaseInvoiceProduct
from tests.apps.purchase.base.factories import (
    PurchaseInvoiceFactory,
    PurchaseInvoiceProductFactory,
)
from tests.bases import BaseModelFactory


class TestPurchaseInvoice:
    """Class for testing PurchaseInvoice model."""

    def test_factory(self) -> None:
        """Test PurchaseInvoice model instance creation."""
        BaseModelFactory.check_factory(
            factory_class=PurchaseInvoiceFactory, model=PurchaseInvoice
        )

    def test__repr__(self) -> None:
        """Test PurchaseInvoice __repr__ method."""
        obj: PurchaseInvoice = PurchaseInvoiceFactory()
        expected_result: str = str(obj.name)
        assert expected_result == obj.__repr__()


class TestPurchaseInvoiceProduct:
    """Class for testing PurchaseInvoiceProduct model."""

    def test_factory(self) -> None:
        """Test InvoiceProduct model instance creation."""
        BaseModelFactory.check_factory(
            factory_class=PurchaseInvoiceProductFactory, model=PurchaseInvoiceProduct
        )

    def test__repr__(self) -> None:
        """Test InvoiceProduct __repr__ method."""
        obj: PurchaseInvoiceProduct = PurchaseInvoiceProductFactory()
        expected_result: str = f"Purchase invoice product with id {obj.product_id}"
        assert expected_result == obj.__repr__()
