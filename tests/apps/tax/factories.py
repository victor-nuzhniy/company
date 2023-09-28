"""Factories for tax apps models."""
import factory

from api import TaxInvoice, TaxInvoiceProduct
from tests.apps.purchase.factories import PurchaseInvoiceProductFactory
from tests.apps.sale.factories import SaleInvoiceFactory, SaleInvoiceProductFactory
from tests.bases import BaseModelFactory


class TaxInvoiceFactory(BaseModelFactory):
    """Factory for TaxInvoice model."""

    id = factory.Sequence(lambda x: x)
    name = factory.Faker("pystr", min_chars=1, max_chars=100)
    sale_invoice = factory.SubFactory(SaleInvoiceFactory)
    sale_invoice_id = factory.SelfAttribute(attribute_name="sale_invoice.id")
    created_at = factory.Faker("date_time")
    tax_invoice_products = factory.RelatedFactoryList(
        factory="tests.apps.tax.factories.TaxInvoiceProductFactory",
        factory_related_name="tax_invoice_products",
        size=0,
    )
    sale_invoices = factory.RelatedFactoryList(
        factory="tests.apps.sale.factories.SaleInvoieFactory",
        factory_related_name="sale_invoices",
        size=0,
    )

    @classmethod
    def _setup_next_sequence(cls):
        return 1

    class Meta:
        """Class Meta for UserFactory."""

        model = TaxInvoice
        exclude = ("tax_invoice_products", "sale_invoice", "sale_invoices")
        sqlalchemy_get_or_create = ("sale_invoice_id",)


class TaxInvoiceProductFactory(BaseModelFactory):
    """Factory for PurchaseInvoiceProduct model."""

    id = factory.Sequence(lambda x: x)
    tax_invoice = factory.SubFactory(TaxInvoiceFactory)
    tax_invoice_id = factory.SelfAttribute(attribute_name="tax_invoice.id")
    sale_invoice_product = factory.SubFactory(SaleInvoiceProductFactory)
    sale_invoice_product_id = factory.SelfAttribute(
        attribute_name="sale_invoice_product.id"
    )
    purchase_invoice_product = factory.SubFactory(PurchaseInvoiceProductFactory)
    purchase_invoice_product_id = factory.SelfAttribute(
        attribute_name="purchase_invoice_product.id"
    )
    quantity = factory.Faker("pyint")
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
    purchase_invoice_products = factory.RelatedFactoryList(
        factory="tests.apps.purchase.factories.PurchaseInvoiceProductFactory",
        factory_related_name="purchase_invoice_products",
        size=0,
    )

    @classmethod
    def _setup_next_sequence(cls):
        return 1

    class Meta:
        """Class Meta for UserFactory."""

        model = TaxInvoiceProduct
        exclude = (
            "tax_invoices",
            "tax_invoice",
            "sale_invoice_product",
            "sale_invoice_products",
            "purchase_invoice_products",
            "purchase_invoice_product",
        )
        sqlalchemy_get_or_create = (
            "tax_invoice_id",
            "sale_invoice_product_id",
            "purchase_invoice_product_id",
        )
