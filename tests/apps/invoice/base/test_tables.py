"""Tests for base apps models."""
from api import Invoice, InvoiceProduct
from tests.apps.invoice.base.factories import InvoiceFactory, InvoiceProductFactory
from tests.bases import BaseModelFactory


class TestInvoice:
    """Class for testing Invoice model."""

    def test_factory(self) -> None:
        """Test Invoice model instance creation."""
        BaseModelFactory.check_factory(factory_class=InvoiceFactory, model=Invoice)

    def test__repr__(self) -> None:
        """Test Invoice __repr__ method."""
        obj: Invoice = InvoiceFactory()
        expected_result: str = str(obj.name)
        assert expected_result == obj.__repr__()


class TestInvoiceProduct:
    """Class for testing InvoiceProduct model."""

    def test_factory(self) -> None:
        """Test InvoiceProduct model instance creation."""
        BaseModelFactory.check_factory(
            factory_class=InvoiceProductFactory, model=InvoiceProduct
        )

    def test__repr__(self) -> None:
        """Test InvoiceProduct __repr__ method."""
        obj: InvoiceProduct = InvoiceProductFactory()
        expected_result: str = f"Invoice product with id {obj.product_id}"
        assert expected_result == obj.__repr__()
