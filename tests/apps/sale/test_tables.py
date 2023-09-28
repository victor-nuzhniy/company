"""Tests for sale apps tables."""
from api import SaleInvoice, SaleInvoiceProduct
from tests.apps.sale.factories import SaleInvoiceFactory, SaleInvoiceProductFactory
from tests.bases import BaseModelFactory


class TestSaleInvoice:
    """Class for testing SaleInvoice model."""

    def test_factory(self) -> None:
        """Test SaleInvoice model instance creation."""
        BaseModelFactory.check_factory(
            factory_class=SaleInvoiceFactory, model=SaleInvoice
        )

    def test__repr__(self) -> None:
        """Test SaleInvoice __repr__ method."""
        obj: SaleInvoice = SaleInvoiceFactory()
        expected_result: str = str(obj.name)
        assert expected_result == obj.__repr__()


class TestSaleInvoiceProduct:
    """Class for testing SaleInvoiceProduct model."""

    def test_factory(self) -> None:
        """Test SaleInvoiceProduct model instance creation."""
        BaseModelFactory.check_factory(
            factory_class=SaleInvoiceProductFactory, model=SaleInvoiceProduct
        )

    def test__repr__(self) -> None:
        """Test SaleInvoiceProduct __repr__ method."""
        obj: SaleInvoiceProduct = SaleInvoiceProductFactory()
        expected_result: str = f"Sale_invoice product with id {obj.product_id}"
        assert expected_result == obj.__repr__()
