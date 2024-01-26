"""Module for testing base routes."""
from typing import Dict

from faker import Faker

from api import SaleInvoice, SaleInvoiceProduct
from tests.apps.sale.base.factories import SaleInvoiceFactory, SaleInvoiceProductFactory
from tests.apps.sale.base.testing_utilities import (
    create_sale_invoice_data,
    create_sale_invoice_product_data,
    create_sale_invoice_put_data,
)
from tests.testing_classes import SampleTestRoute


class TestSaleInvoiceRoute(SampleTestRoute):
    """Class with methods for testing SaleInvoice routes."""

    model = SaleInvoice
    factory = SaleInvoiceFactory

    def get_fake_data(self, faker: Faker) -> Dict:
        """Get SaleInvoice fake data dict."""
        return create_sale_invoice_data(faker)

    def get_fake_put_data(self, faker: Faker) -> Dict:
        """Get SaleInvoice fake data dict for put and patch methods."""
        return create_sale_invoice_put_data(faker)


class TestSaleInvoiceProductRoute(SampleTestRoute):
    """Class with methods for testing SaleInvoiceProduct routes."""

    model = SaleInvoiceProduct
    factory = SaleInvoiceProductFactory

    def get_fake_data(self, faker: Faker) -> Dict:
        """Get SaleInvoiceProduct fake data dict."""
        return create_sale_invoice_product_data(faker)

    def get_fake_put_data(self, faker: Faker) -> Dict:
        """Get SaleInvoiceProduct fake data dict for put and patch methods."""
        return create_sale_invoice_product_data(faker)
