"""Routes for base apps."""
from typing import Dict

from faker import Faker

from api import PurchaseInvoice, PurchaseInvoiceProduct
from tests.apps.purchase.base.factories import (
    PurchaseInvoiceFactory,
    PurchaseInvoiceProductFactory,
)
from tests.apps.purchase.base.testing_utilities import (
    create_purchase_invoice_data,
    create_purchase_invoice_product_data,
    create_purchase_invoice_put_data,
)
from tests.testing_classes import SampleTestRoute


class TestPurchaseInvoiceRoute(SampleTestRoute):
    """Class with methods for testing PurchaseInvoice routes."""

    model = PurchaseInvoice
    factory = PurchaseInvoiceFactory

    def get_fake_data(self, faker: Faker) -> Dict:
        """Get PurchaseInvoice fake data dict."""
        return create_purchase_invoice_data(faker)

    def get_fake_put_data(self, faker: Faker) -> Dict:
        """Get PurchaseInvoice fake data dict for put and patch methods."""
        return create_purchase_invoice_put_data(faker)


class TestPurchaseInvoiceProductRoute(SampleTestRoute):
    """Class with methods for testing PurhcaseInvoiceProduct routes."""

    model = PurchaseInvoiceProduct
    factory = PurchaseInvoiceProductFactory

    def get_fake_data(self, faker: Faker) -> Dict:
        """Get PurchaseInvoiceProduct fake data dict."""
        return create_purchase_invoice_product_data(faker)

    def get_fake_put_data(self, faker: Faker) -> Dict:
        """Get PurchaseInvoiceProduct fake data dict for put and patch methods."""
        return create_purchase_invoice_product_data(faker)
