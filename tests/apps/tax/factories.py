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
    sale_invoice_id = factory.SubFactory(SaleInvoiceFactory)
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
        exclude = ("tax_invoice_products", "sale_invoices")
        sqlalchemy_get_or_create = ("sale_invoice_id",)


class TaxInvoiceProductFactory(BaseModelFactory):
    """Factory for PurchaseInvoiceProduct model."""

    id = factory.Sequence(lambda x: x)
    tax_invoice_id = factory.SubFactory(TaxInvoiceFactory)
    sale_invoice_product_id = factory.SubFactory(SaleInvoiceProductFactory)
    purchase_invoice_product_id = factory.SubFactory(PurchaseInvoiceProductFactory)
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
        exclude = ("tax_invoices", "sale_invoice_products", "purchase_invoice_products")
        sqlalchemy_get_or_create = (
            "tax_invoice_id",
            "sale_invoice_product_id",
            "purchase_invoice_product_id",
        )
