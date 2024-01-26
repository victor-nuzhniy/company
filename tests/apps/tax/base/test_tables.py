"""Tests for base apps models."""
from api import TaxInvoice, TaxInvoiceProduct
from tests.apps.tax.base.factories import TaxInvoiceFactory, TaxInvoiceProductFactory
from tests.bases import BaseModelFactory


class TestTaxInvoice:
    """Class for testing TaxInvoice model."""

    def test_factory(self) -> None:
        """Test TaxInvoice model instance creation."""
        BaseModelFactory.check_factory(
            factory_class=TaxInvoiceFactory,
            model=TaxInvoice,
        )

    def test_repr(self) -> None:
        """Test TaxInvoice __repr__ method."""
        instance: TaxInvoice = TaxInvoiceFactory()
        expected_result: str = str(instance.name)
        assert expected_result == str(instance)


class TestTaxInvoiceProduct:
    """Class for testing TaxInvoiceProduct model."""

    def test_factory(self) -> None:
        """Test TaxInvoiceProduct model instance creation."""
        BaseModelFactory.check_factory(
            factory_class=TaxInvoiceProductFactory,
            model=TaxInvoiceProduct,
        )

    def test_repr(self) -> None:
        """Test TaxInvoiceProduct __repr__ method."""
        instance: TaxInvoiceProduct = TaxInvoiceProductFactory()
        expected_result: str = "Tax invoice product id {id}".format(
            id=instance.tax_invoice_id,
        )
        assert expected_result == str(instance)
