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
        factory_related_name="discount",
        size=0,
    )

    @classmethod
    def _setup_next_sequence(cls) -> int:
        """Set next sequence start value.."""
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
    discount = factory.SubFactory(factory=DiscountFactory)
    discount_id = factory.SelfAttribute(attribute_name="discount.id")
    discounts = factory.RelatedFactoryList(
        factory="tests.apps.counterparty.factories.DiscountFactory",
        factory_related_name="counterparty",
        size=0,
    )
    agreements = factory.RelatedFactoryList(
        factory="tests.apps.counterparty.factories.AgreementFactory",
        factory_related_name="counterparty",
        size=0,
    )
    orders = factory.RelatedFactoryList(
        factory="tests.apps.order.factories.OrderFactory",
        factory_related_name="counterparty",
        size=0,
    )

    @classmethod
    def _setup_next_sequence(cls) -> 1:
        """Set sequence next start type value."""
        return 1

    class Meta:
        """Class Meta for UserFactory."""

        model = Counterparty
        exclude = ("discounts", "discount", "agreements", "orders")
        sqlalchemy_get_or_create = ("discount_id",)


class AgreementFactory(BaseModelFactory):
    """Factory for Agreement model."""

    id = factory.Sequence(lambda x: x)
    name = factory.Faker("pystr", min_chars=1, max_chars=200)
    counterparty = factory.SubFactory(CounterpartyFactory)
    counterparty_id = factory.SelfAttribute(attribute_name="counterparty.id")
    counterparties = factory.RelatedFactoryList(
        factory="tests.apps.counterparty.factories.CounterpartyFactory",
        factory_related_name="agreement",
        size=0,
    )
    invoices = factory.RelatedFactoryList(
        factory="tests.apps.invoice.factories.InvoiceFactory",
        factory_related_name="agreement",
        size=0,
    )
    purchase_invoices = factory.RelatedFactoryList(
        factory="tests.apps.purchase.factories.PurchaseInvoiceFactory",
        factory_related_name="agreement",
        size=0,
    )

    @classmethod
    def _setup_next_sequence(cls) -> int:
        """Set sequence next start type value."""
        return 1

    class Meta:
        """Class Meta for UserFactory."""

        model = Agreement
        exclude = ("counterparties", "counterparty", "invoices", "purchase_invoices")
        sqlalchemy_get_or_create = ("counterparty_id",)
