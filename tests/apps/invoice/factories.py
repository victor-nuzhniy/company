"""Factories for invoice apps."""

import factory

from api import Invoice, InvoiceProduct
from tests.apps.counterparty.factories import AgreementFactory
from tests.apps.order.factories import OrderFactory
from tests.apps.product.factories import ProductFactory
from tests.bases import BaseModelFactory


class InvoiceFactory(BaseModelFactory):
    """Factory for testing Invoice model."""

    id = factory.Sequence(lambda x: x)
    name = factory.Faker("pystr", min_chars=1, max_chars=100)
    order_id = factory.SubFactory(OrderFactory)
    created_at = factory.Faker("date_time")
    paid = factory.Faker("boolean")
    agreement_id = factory.SubFactory(AgreementFactory)
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
    invoice_products = factory.RelatedFactoryList(
        factory="tests.apps.invoice.factories.InvoiceProductFactory",
        factory_related_name="invoice_products",
        size=0,
    )
    sale_invoices = factory.RelatedFactoryList(
        factory="tests.apps.sale.factories.SaleInvoiceFactory",
        factory_related_name="sale_invoices",
        size=0,
    )

    @classmethod
    def _setup_next_sequence(cls):
        return 1

    class Meta:
        """Class Meta for UserFactory."""

        model = Invoice
        exclude = ("orders", "agreements", "invoice_products", "sale_invoices")
        sqlalchemy_get_or_create = ("agreement_id",)


class InvoiceProductFactory(BaseModelFactory):
    """Factory for testing InvoiceProduct model."""

    id = factory.Sequence(lambda x: x)
    product_id = factory.SubFactory(ProductFactory)
    quantity = factory.Faker("pyint")
    price = factory.Faker("pyint")
    invoice_id = factory.SubFactory(InvoiceFactory)
    products = factory.RelatedFactoryList(
        factory="tests.apps.product.factories.ProductFactory",
        factory_related_name="products",
        size=0,
    )
    invoices = factory.RelatedFactoryList(
        factory="tests.apps.invoice.factories.InvoiceFactory",
        factory_related_name="invoices",
        size=0,
    )

    @classmethod
    def _setup_next_sequence(cls):
        return 1

    class Meta:
        """Class Meta for UserFactory."""

        model = InvoiceProduct
        exclude = ("products", "invoices")
        sqlalchemy_get_or_create = ("product_id", "invoice_id")
