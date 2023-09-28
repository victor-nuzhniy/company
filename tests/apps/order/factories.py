"""Factories for testing Order model."""
import factory

from api import Order, OrderProduct
from tests.apps.counterparty.factories import CounterpartyFactory
from tests.apps.product.factories import ProductFactory
from tests.apps.user.factories import UserFactory
from tests.bases import BaseModelFactory


class OrderFactory(BaseModelFactory):
    """Factory for testing Order model."""

    id = factory.Sequence(lambda x: x)
    user_id = factory.SubFactory(UserFactory)
    name = factory.Faker("pystr", min_chars=1, max_chars=100)
    created_at = factory.Faker("date_time")
    customer_id = factory.SubFactory(CounterpartyFactory)
    order_products = factory.RelatedFactoryList(
        factory="tests.apps.order.factory.OrderProductFactory",
        factory_related_name="order_products",
        size=0,
    )
    invoices = factory.RelatedFactoryList(
        factory="tests.apps.invoice.factories.InvoiceFactory",
        factory_related_name="invoices",
        size=0,
    )
    users = factory.RelatedFactoryList(
        factory="tests.apps.user.factories.UserFactory",
        factory_related_name="users",
        size=0,
    )
    counterparties = factory.RelatedFactoryList(
        factory="tests.apps.counterparty.factories.CounterpartyFactory",
        factory_related_name="counterparties",
        size=0,
    )

    @classmethod
    def _setup_next_sequence(cls):
        return 1

    class Meta:
        """Class Meta for UserFactory."""

        model = Order
        exclude = ("order_products", "invoices", "users", "counterparties")
        sqlalchemy_get_or_create = ("user_id", "customer_id")


class OrderProductFactory(BaseModelFactory):
    """Factory for OrderProduct model."""

    id = factory.Sequence(lambda x: x)
    product_id = factory.SubFactory(ProductFactory)
    quantity = factory.Faker("pyint")
    price = factory.Faker("pyint")
    order_id = factory.SubFactory(OrderFactory)
    products = factory.RelatedFactoryList(
        factory="tests.apps.product.factories.ProductFactory",
        factory_related_name="products",
        size=0,
    )
    orders = factory.RelatedFactoryList(
        factory="tests.apps.order.factories.OrderFactory",
        factory_related_name="orders",
        size=0,
    )

    @classmethod
    def _setup_next_sequence(cls):
        return 1

    class Meta:
        """Class Meta for UserFactory."""

        model = OrderProduct
        exclude = ("products", "orders")
        sqlalchemy_get_or_create = ("product_id", "order_id")
