"""Factories for counterparty apps."""
import factory

from api import Agreement, Counterparty, Discount
from tests.bases import BaseModelFactory


class DiscountFactory(BaseModelFactory):
    """Factory for testing Discount model."""

    id = factory.Sequence(lambda x: x)
    name = factory.Faker("pystr", min_chars=1, max_chars=30)
    rate = factory.Faker("random_int", min=0, max=100)
    counterparties = factory.RelatedFactoryList(
        factory="tests.apps.counterparty.CounterpartyFactory",
        factory_related_name="counterparties",
        size=0,
    )

    @classmethod
    def _setup_next_sequence(cls):
        """Create id sequence."""
        return 1

    class Meta:
        """Class Meta for UserFactory."""

        model = Discount
        exclude = ("counterparties",)


class CounterpartyFactory(BaseModelFactory):
    """Factory for Counterparty model."""

    id = factory.Sequence(lambda x: x)
    name = factory.Faker("pystr", min_chars=1, max_chars=150)
    postal_code = factory.Faker("postcode")
    country = factory.Faker("country")
    city = factory.Faker("city")
    address = factory.Faker("address")
    phone_number = factory.Faker("phone_number")
    discount_id = factory.SubFactory(factory=DiscountFactory)
    discounts = factory.RelatedFactoryList(
        factory="tests.apps.counterparty.factories.DiscountFactory",
        factory_related_name="discounts",
        size=0,
    )
    agreements = factory.RelatedFactoryList(
        factory="tests.apps.counterparty.factories.AgreementFactory",
        factory_related_name="agreements",
        size=0,
    )
    orders = factory.RelatedFactoryList(
        factory="tests.apps.order.factories.OrderFactory",
        factory_related_name="orders",
        size=0,
    )

    @classmethod
    def _setup_next_sequence(cls):
        """Create id sequence."""
        return 1

    class Meta:
        """Class Meta for UserFactory."""

        model = Counterparty
        exclude = ("discounts", "agreements", "orders")
        sqlalchemy_get_or_create = ("discount_id",)


class AgreementFactory(BaseModelFactory):
    """Factory for Agreement model."""

    id = factory.Sequence(lambda x: x)
    name = factory.Faker("pystr", min_chars=1, max_chars=200)
    counterparty_id = factory.SubFactory(CounterpartyFactory)
    counterparties = factory.RelatedFactoryList(
        factory="tests.apps.counterparty.factories.CounterpartyFactory",
        factory_related_name="counterparties",
        size=0,
    )
    invoices = factory.RelatedFactoryList(
        factory="tests.apps.invoice.factories.InvoiceFactory",
        factory_related_name="invoices",
        size=0,
    )
    purchase_invoices = factory.RelatedFactoryList(
        factory="tests.apps.purchase.factories.PurchaseInvoiceFactory",
        factory_related_name="purchase_invoices",
        size=0,
    )

    @classmethod
    def _setup_next_sequence(cls):
        """Create id sequence."""
        return 1

    class Meta:
        """Class Meta for UserFactory."""

        model = Agreement
        exclude = ("counterparties", "invoices", "purchase_invoices")
        sqlalchemy_get_or_create = ("counterparty_id",)
