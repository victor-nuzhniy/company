"""Tests for base apps tables."""
from api import SaleInvoice, SaleInvoiceProduct
from tests.apps.sale.base.factories import SaleInvoiceFactory, SaleInvoiceProductFactory
from tests.bases import BaseModelFactory


class TestSaleInvoice:
    """Class for testing SaleInvoice model."""

    def test_factory(self) -> None:
        """Test SaleInvoice model instance creation."""
        BaseModelFactory.check_factory(
            factory_class=SaleInvoiceFactory,
            model=SaleInvoice,
        )

    def test_repr(self) -> None:
        """Test SaleInvoice __repr__ method."""
        instance: SaleInvoice = SaleInvoiceFactory()
        expected_result: str = str(instance.name)
        assert expected_result == str(instance)


class TestSaleInvoiceProduct:
    """Class for testing SaleInvoiceProduct model."""

    def test_factory(self) -> None:
        """Test SaleInvoiceProduct model instance creation."""
        BaseModelFactory.check_factory(
            factory_class=SaleInvoiceProductFactory,
            model=SaleInvoiceProduct,
        )

    def test_repr(self) -> None:
        """Test SaleInvoiceProduct __repr__ method."""
        instance: SaleInvoiceProduct = SaleInvoiceProductFactory()
        expected_result: str = "Sale_invoice product with id {id}".format(
            id=instance.product_id,
        )
        assert expected_result == str(instance)
