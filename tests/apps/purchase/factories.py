"""Factories for purchase apps models."""
import factory

from api import PurchaseInvoice, PurchaseInvoiceProduct
from tests.apps.counterparty.factories import AgreementFactory
from tests.apps.product.factories import ProductFactory
from tests.bases import BaseModelFactory


class PurchaseInvoiceFactory(BaseModelFactory):
    """Factory for PurchaseInvoice model."""

    id = factory.Sequence(lambda x: x)
    name = factory.Faker("pystr", min_chars=1, max_chars=100)
    agreement_id = factory.SubFactory(AgreementFactory)
    created_at = factory.Faker("date_time")
    purchase_invoice_products = factory.RelatedFactoryList(
        factory="tests.apps.purchase.factories.PurchaseInvoiceProductFactory",
        factory_related_name="purchase_invoice_products",
        size=0,
    )
    agreements = factory.RelatedFactoryList(
        factory="tests.apps.counterparty.factories.AgreementFactory",
        factory_related_name="agreements",
        size=0,
    )

    @classmethod
    def _setup_next_sequence(cls):
        return 1

    class Meta:
        """Class Meta for UserFactory."""

        model = PurchaseInvoice
        exclude = ("purchase_invoice_products", "agreements")
        sqlalchemy_get_or_create = ("agreement_id",)


class PurchaseInvoiceProductFactory(BaseModelFactory):
    """Factory for PurchaseInvoiceProduct model."""

    id = factory.Sequence(lambda x: x)
    product_id = factory.SubFactory(ProductFactory)
    quantity = factory.Faker("pyint")
    price = factory.Faker("pyint")
    purchase_invoice_id = factory.SubFactory(PurchaseInvoiceFactory)
    products_left = factory.Faker("pyint")
    products = factory.RelatedFactoryList(
        factory="tests.apps.product.factories.ProductFactory",
        factory_related_name="products",
        size=0,
    )
    tax_invoice_products = factory.RelatedFactoryList(
        factory="tests.apps.tax.factories.TaxInvoiceProductFactory",
        factory_related_name="tax_invoice_products",
        size=0,
    )
    purchase_invoices = factory.RelatedFactoryList(
        factory="tests.apps.purchase.factories.PurchaseInvoiceFactory",
        factory_related_name="purchase_invoices",
        size=0,
    )

    @classmethod
    def _setup_next_sequence(cls):
        return 1

    class Meta:
        """Class Meta for UserFactory."""

        model = PurchaseInvoiceProduct
        exclude = ("products", "tax_invoice_products", "purchase_invoices")
        sqlalchemy_get_or_create = ("product_id", "purchase_invoice_id")
