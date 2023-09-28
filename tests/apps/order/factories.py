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
    user = factory.SubFactory(UserFactory)
    user_id = factory.SelfAttribute(attribute_name="user.id")
    name = factory.Faker("pystr", min_chars=1, max_chars=100)
    created_at = factory.Faker("date_time")
    customer = factory.SubFactory(CounterpartyFactory)
    customer_id = factory.SelfAttribute(attribute_name="customer.id")
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
    customers = factory.RelatedFactoryList(
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
        exclude = (
            "order_products",
            "invoices",
            "users",
            "user",
            "customer",
            "customers",
        )
        sqlalchemy_get_or_create = ("user_id", "customer_id")


class OrderProductFactory(BaseModelFactory):
    """Factory for OrderProduct model."""

    id = factory.Sequence(lambda x: x)
    product = factory.SubFactory(ProductFactory)
    product_id = factory.SelfAttribute(attribute_name="product.id")
    quantity = factory.Faker("pyint")
    price = factory.Faker("pyint")
    order = factory.SubFactory(OrderFactory)
    order_id = factory.SelfAttribute(attribute_name="order.id")
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
        exclude = ("products", "product", "order", "orders")
        sqlalchemy_get_or_create = ("product_id", "order_id")
