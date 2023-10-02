"""Factories for sale apps models."""
import factory

from api import SaleInvoice, SaleInvoiceProduct
from tests.apps.invoice.factories import InvoiceFactory
from tests.apps.product.factories import ProductFactory
from tests.bases import BaseModelFactory


class SaleInvoiceFactory(BaseModelFactory):
    """Factory for SaleInvoice model."""

    id = factory.Sequence(lambda x: x)
    name = factory.Faker("pystr", min_chars=1, max_chars=100)
    invoice = factory.SubFactory(InvoiceFactory)
    invoice_id = factory.SelfAttribute(attribute_name="invoice.id")
    created_at = factory.Faker("date_time")
    done = factory.Faker("pybool")
    tax_invoices = factory.RelatedFactoryList(
        factory="tests.apps.tax.factories.TaxInvoiceFactory",
        factory_related_name="tax_invoices",
        size=0,
    )
    sale_invoice_products = factory.RelatedFactoryList(
        factory="tests.apps.sale.factories.SaleInvoiceProductFactory",
        factory_related_name="sale_invoice_products",
        size=0,
    )
    invoices = factory.RelatedFactoryList(
        factory="tests.apps.invoice.factories.InvoiceFactory",
        factory_related_name="invoices",
        size=0,
    )

    @classmethod
    def _setup_next_sequence(cls):
        """Create id sequence."""
        return 1

    class Meta:
        """Class Meta for UserFactory."""

        model = SaleInvoice
        exclude = ("tax_invoices", "sale_invoice_products", "invoices", "invoice")
        sqlalchemy_get_or_create = ("invoice_id",)


class SaleInvoiceProductFactory(BaseModelFactory):
    """Factory for SaleInvoiceProduct model."""

    id = factory.Sequence(lambda x: x)
    product = factory.SubFactory(ProductFactory)
    product_id = factory.SelfAttribute(attribute_name="product.id")
    quantity = factory.Faker("pyint")
    price = factory.Faker("pyint")
    sale_invoice = factory.SubFactory(SaleInvoiceFactory)
    sale_invoice_id = factory.SelfAttribute(attribute_name="sale_invoice.id")
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
    sale_invoices = factory.RelatedFactoryList(
        factory="tests.apps.sale.factories.SaleInvoiceFactory",
        factory_related_name="sale_invoices",
        size=0,
    )

    @classmethod
    def _setup_next_sequence(cls):
        """Create id sequence."""
        return 1

    class Meta:
        """Class Meta for UserFactory."""

        model = SaleInvoiceProduct
        exclude = (
            "products",
            "product",
            "sale_invoice",
            "tax_invoice_products",
            "sale_invoices",
        )
        sqlalchemy_get_or_create = ("sale_invoice_id", "product_id")
