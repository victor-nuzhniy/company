"""Tests for base apps models."""
from api import Agreement, Counterparty, Discount
from tests.apps.counterparty.base.factories import (
    AgreementFactory,
    CounterpartyFactory,
    DiscountFactory,
)
from tests.bases import BaseModelFactory


class TestAgreement:
    """Class for testing Agreement model."""

    def test_factory(self) -> None:
        """Test Agreement model instance creation."""
        BaseModelFactory.check_factory(factory_class=AgreementFactory, model=Agreement)

    def test__repr__(self) -> None:
        """Test Agreement __repr__ method."""
        obj: Agreement = AgreementFactory()
        expected_result: str = str(obj.name)
        assert expected_result == obj.__repr__()


class TestCounterparty:
    """Class for testing Agreement model."""

    def test_factory(self) -> None:
        """Test Agreement model instance creation."""
        BaseModelFactory.check_factory(
            factory_class=CounterpartyFactory, model=Counterparty
        )

    def test__repr__(self) -> None:
        """Test Agreement __repr__ method."""
        obj: Counterparty = CounterpartyFactory()
        expected_result: str = str(obj.name)
        assert expected_result == obj.__repr__()


class TestDiscount:
    """Class for testing Agreement model."""

    def test_factory(self) -> None:
        """Test Agreement model instance creation."""
        BaseModelFactory.check_factory(factory_class=DiscountFactory, model=Discount)

    def test__repr__(self) -> None:
        """Test Agreement __repr__ method."""
        obj: Discount = DiscountFactory()
        expected_result: str = str(obj.name)
        assert expected_result == obj.__repr__()
