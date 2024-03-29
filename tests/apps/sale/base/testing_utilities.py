"""Fixtures for sale apps."""
from typing import Dict

from faker import Faker

from api import Invoice, Product, SaleInvoice
from tests.apps.invoice.base.factories import InvoiceFactory
from tests.apps.product.base.factories import ProductFactory
from tests.apps.sale.base.factories import SaleInvoiceFactory


def create_sale_invoice_data(faker: Faker) -> Dict:
    """Create SaleInvoice fake data."""
    invoice: Invoice = InvoiceFactory()
    return {
        "name": faker.pystr(min_chars=1, max_chars=100),
        "invoice_id": invoice.id,
    }


def create_sale_invoice_put_data(faker: Faker) -> Dict:
    """Create SaleInvoice fake data."""
    invoice: Invoice = InvoiceFactory()
    return {
        "name": faker.pystr(min_chars=1, max_chars=100),
        "invoice_id": invoice.id,
        "created_at": faker.date_time().strftime("%Y-%m-%d %H:%M:%S"),
        "done": faker.pybool(),
    }


def create_sale_invoice_product_data(faker: Faker) -> Dict:
    """Create SaleInvoiceProduct fake data."""
    product: Product = ProductFactory()
    sale_invoice: SaleInvoice = SaleInvoiceFactory()
    return {
        "product_id": product.id,
        "quantity": faker.pyint(),
        "price": faker.pyint(),
        "sale_invoice_id": sale_invoice.id,
    }
