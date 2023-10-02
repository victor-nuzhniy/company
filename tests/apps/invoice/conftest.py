"""Fixtures for invoice apps."""
from typing import Dict

from faker import Faker

from api import Agreement, Invoice, Order, Product
from tests.apps.counterparty.factories import AgreementFactory
from tests.apps.invoice.factories import InvoiceFactory
from tests.apps.order.factories import OrderFactory
from tests.apps.product.factories import ProductFactory


def create_invoice_data(faker: Faker) -> Dict:
    """Create Invoice fake data."""
    order: Order = OrderFactory()
    agreement: Agreement = AgreementFactory()
    return {
        "name": faker.pystr(min_chars=1, max_chars=100),
        "order_id": order.id,
        "agreement_id": agreement.id,
    }


def create_invoice_put_data(faker: Faker) -> Dict:
    """Create Invoice data for patch method."""
    order: Order = OrderFactory()
    agreement: Agreement = AgreementFactory()
    return {
        "name": faker.pystr(min_chars=1, max_chars=100),
        "order_id": order.id,
        "created_at": faker.date_time().strftime("%Y-%m-%dT%H:%M:%S"),
        "paid": faker.pybool(),
        "agreement_id": agreement.id,
    }


def create_invoice_product_data(faker: Faker) -> Dict:
    """Create InvoiceProduct fake data."""
    product: Product = ProductFactory()
    invoice: Invoice = InvoiceFactory()
    return {
        "product_id": product.id,
        "quantity": faker.pyint(),
        "price": faker.pyint(),
        "invoice_id": invoice.id,
    }
