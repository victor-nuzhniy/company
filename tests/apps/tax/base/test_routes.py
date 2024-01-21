"""Module for testing base routes."""
from typing import Dict

from faker import Faker

from api import TaxInvoice, TaxInvoiceProduct
from tests.apps.tax.base.factories import TaxInvoiceFactory, TaxInvoiceProductFactory
from tests.apps.tax.base.testing_utilities import (
    create_tax_invoice_data,
    create_tax_invoice_product_data,
    create_tax_invoice_put_data,
)
from tests.testing_classes import SampleTestRoute


class TestTaxInvoiceRoute(SampleTestRoute):
    """Class with methods for testing TaxInvoice routes."""

    model = TaxInvoice
    factory = TaxInvoiceFactory

    def get_fake_data(self, faker: Faker) -> Dict:
        """Get TaxInvoice fake data dict."""
        return create_tax_invoice_data(faker)

    def get_fake_put_data(self, faker: Faker) -> Dict:
        """Get TaxInvoice fake data dict for put and patch methods."""
        return create_tax_invoice_put_data(faker)


class TestTaxInvoiceProductRoute(SampleTestRoute):
    """Class with methods for testing TaxInvoiceProduct routes."""

    model = TaxInvoiceProduct
    factory = TaxInvoiceProductFactory

    def get_fake_data(self, faker: Faker) -> Dict:
        """Get TaxInvoiceProduct fake data dict."""
        return create_tax_invoice_product_data(faker)

    def get_fake_put_data(self, faker: Faker) -> Dict:
        """Get TaxInvoiceProduct fake data dict for put and patch methods."""
        return create_tax_invoice_product_data(faker)
