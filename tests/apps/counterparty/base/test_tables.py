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

    def test_repr(self) -> None:
        """Test Agreement __repr__ method."""
        instance: Agreement = AgreementFactory()
        expected_result: str = str(instance.name)
        assert expected_result == instance.__repr__()  # noqa: WPS609


class TestCounterparty:
    """Class for testing Agreement model."""

    def test_factory(self) -> None:
        """Test Agreement model instance creation."""
        BaseModelFactory.check_factory(
            factory_class=CounterpartyFactory,
            model=Counterparty,
        )

    def test_repr(self) -> None:
        """Test Agreement __repr__ method."""
        instance: Counterparty = CounterpartyFactory()
        expected_result: str = str(instance.name)
        assert expected_result == instance.__repr__()  # noqa: WPS609


class TestDiscount:
    """Class for testing Agreement model."""

    def test_factory(self) -> None:
        """Test Agreement model instance creation."""
        BaseModelFactory.check_factory(factory_class=DiscountFactory, model=Discount)

    def test_repr(self) -> None:
        """Test Agreement __repr__ method."""
        instance: Discount = DiscountFactory()
        expected_result: str = str(instance.name)
        assert expected_result == instance.__repr__()  # noqa: WPS609
