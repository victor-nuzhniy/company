"""Tests for tax apps models."""
from api import TaxInvoice, TaxInvoiceProduct
from tests.apps.tax.factories import TaxInvoiceFactory, TaxInvoiceProductFactory
from tests.bases import BaseModelFactory


class TestTaxInvoice:
    """Class for testing TaxInvoice model."""

    def test_factory(self) -> None:
        """Test TaxInvoice model instance creation."""
        BaseModelFactory.check_factory(
            factory_class=TaxInvoiceFactory, model=TaxInvoice
        )

    def test__repr__(self) -> None:
        """Test TaxInvoice __repr__ method."""
        obj: TaxInvoice = TaxInvoiceFactory()
        expected_result: str = str(obj.name)
        assert expected_result == obj.__repr__()


class TestTaxInvoiceProduct:
    """Class for testing TaxInvoiceProduct model."""

    def test_factory(self) -> None:
        """Test TaxInvoiceProduct model instance creation."""
        BaseModelFactory.check_factory(
            factory_class=TaxInvoiceProductFactory, model=TaxInvoiceProduct
        )

    def test__repr__(self) -> None:
        """Test TaxInvoiceProduct __repr__ method."""
        obj: TaxInvoiceProduct = TaxInvoiceProductFactory()
        expected_result: str = f"Tax invoice id {obj.tax_invoice_id}"
        assert expected_result == obj.__repr__()
