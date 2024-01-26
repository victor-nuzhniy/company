"""Tests for base apps models."""
from api import Invoice, InvoiceProduct
from tests.apps.invoice.base.factories import InvoiceFactory, InvoiceProductFactory
from tests.bases import BaseModelFactory


class TestInvoice:
    """Class for testing Invoice model."""

    def test_factory(self) -> None:
        """Test Invoice model instance creation."""
        BaseModelFactory.check_factory(factory_class=InvoiceFactory, model=Invoice)

    def test_repr(self) -> None:
        """Test Invoice __repr__ method."""
        instance: Invoice = InvoiceFactory()
        expected_result: str = str(instance.name)
        assert expected_result == str(instance)


class TestInvoiceProduct:
    """Class for testing InvoiceProduct model."""

    def test_factory(self) -> None:
        """Test InvoiceProduct model instance creation."""
        BaseModelFactory.check_factory(
            factory_class=InvoiceProductFactory,
            model=InvoiceProduct,
        )

    def test_repr(self) -> None:
        """Test InvoiceProduct __repr__ method."""
        instance: InvoiceProduct = InvoiceProductFactory()
        expected_result: str = "Invoice product with id {id}".format(
            id=instance.product_id,
        )
        assert expected_result == str(instance)
