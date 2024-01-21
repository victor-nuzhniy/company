"""Module for testing base routes."""
from typing import Dict

from faker import Faker

from api import Invoice, InvoiceProduct
from tests.apps.invoice.base.testing_utilities import (
    create_invoice_data,
    create_invoice_product_data,
    create_invoice_put_data,
)
from tests.apps.invoice.base.factories import InvoiceFactory, InvoiceProductFactory
from tests.testing_classes import SampleTestRoute


class TestInvoiceRoute(SampleTestRoute):
    """Class with methods for testing Invoice routes."""

    model = Invoice
    factory = InvoiceFactory

    def get_fake_data(self, faker: Faker) -> Dict:
        """Get Invoice fake data dict."""
        return create_invoice_data(faker)

    def get_fake_put_data(self, faker: Faker) -> Dict:
        """Get Invoice fake data dict for put and patch methods."""
        return create_invoice_put_data(faker)


class TestInvoiceProductRoute(SampleTestRoute):
    """Class with methods for testing InvoiceProduct routes."""

    model = InvoiceProduct
    factory = InvoiceProductFactory

    def get_fake_data(self, faker: Faker) -> Dict:
        """Get InvoiceProduct fake data dict."""
        return create_invoice_product_data(faker)

    def get_fake_put_data(self, faker: Faker) -> Dict:
        """Get InvoiceProduct fake data dict for put and patch methods."""
        return create_invoice_product_data(faker)
