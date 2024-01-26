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
            factory_class=PurchaseInvoiceFactory,
            model=PurchaseInvoice,
        )

    def test_repr(self) -> None:
        """Test PurchaseInvoice __repr__ method."""
        instance: PurchaseInvoice = PurchaseInvoiceFactory()
        expected_result: str = str(instance.name)
        assert expected_result == str(instance)


class TestPurchaseInvoiceProduct:
    """Class for testing PurchaseInvoiceProduct model."""

    def test_factory(self) -> None:
        """Test InvoiceProduct model instance creation."""
        BaseModelFactory.check_factory(
            factory_class=PurchaseInvoiceProductFactory,
            model=PurchaseInvoiceProduct,
        )

    def test_repr(self) -> None:
        """Test InvoiceProduct __repr__ method."""
        instance: PurchaseInvoiceProduct = PurchaseInvoiceProductFactory()
        expected_result: str = "Purchase invoice product with id {id}".format(
            id=instance.product_id,
        )
        assert expected_result == str(instance)
