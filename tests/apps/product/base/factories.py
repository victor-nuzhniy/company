"""Factories for product apps models."""
import factory

from api import Product, ProductType
from tests.bases import BaseModelFactory


class ProductTypeFactory(BaseModelFactory):
    """Factory for testing ProdutType model."""

    id = factory.Sequence(lambda x: x)
    name = factory.Faker("pystr", min_chars=1, max_chars=100)
    products = factory.RelatedFactoryList(
        factory="tests.apps.product.factories.ProductFactory",
        factory_related_name="agreements",
        size=0,
    )

    @classmethod
    def _setup_next_sequence(cls) -> int:
        """Create id sequence."""
        return 1

    class Meta:
        """Class Meta for UserFactory."""

        model = ProductType
        exclude = ("products",)


class ProductFactory(BaseModelFactory):
    """Factory for testing Product model."""

    id = factory.Sequence(lambda x: x)
    name = factory.Faker("pystr", min_chars=1, max_chars=200)
    code = factory.Faker("pystr", min_chars=1, max_chars=100)
    units = factory.Faker("pystr", min_chars=1, max_chars=100)
    currency = factory.Faker("pystr", min_chars=1, max_chars=15)
    price = factory.Faker("pyint")
    product_type = factory.SubFactory(ProductTypeFactory)
    product_type_id = factory.SelfAttribute(attribute_name="product_type.id")
    order_products = factory.RelatedFactoryList(
        factory="tests.apps.order.factories.OrderProductFactory",
        factory_related_name="order_products",
        size=0,
    )
    invoice_products = factory.RelatedFactoryList(
        factory="tests.apps.invoice.factories.InvoiceProductFactory",
        factory_related_name="agreements",
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
    product_types = factory.RelatedFactoryList(
        factory="tests.apps.product.factories.ProductTypeFactory",
        factory_related_name="product_types",
        size=0,
    )

    @classmethod
    def _setup_next_sequence(cls):
        """Create id sequence."""
        return 1

    class Meta:
        """Class Meta for UserFactory."""

        model = Product
        exclude = (
            "order_products",
            "invoice_products",
            "sale_invoice_products",
            "purchase_invoice_products",
            "product_types",
            "product_type",
        )
        sqlalchemy_get_or_create = ("product_type_id",)
