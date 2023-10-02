"""Fixtures for purchase apps."""
from typing import Dict

from faker import Faker

from api import Agreement, Product, PurchaseInvoice
from tests.apps.counterparty.factories import AgreementFactory
from tests.apps.product.factories import ProductFactory
from tests.apps.purchase.factories import PurchaseInvoiceFactory


def create_purchase_invoice_data(faker: Faker) -> Dict:
    """Create PurchaseInvoice fake data."""
    agreement: Agreement = AgreementFactory()
    return {
        "name": faker.pystr(min_chars=1, max_chars=100),
        "agreement_id": agreement.id,
    }


def create_purchase_invoice_put_data(faker: Faker) -> Dict:
    """Create PurchaseInvoice fake data."""
    agreement: Agreement = AgreementFactory()
    return {
        "name": faker.pystr(min_chars=1, max_chars=100),
        "agreement_id": agreement.id,
        "created_at": faker.date_time().strftime("%Y-%m-%dT%H:%M:%S"),
    }


def create_purchase_invoice_product_data(faker: Faker) -> Dict:
    """Create PurchaseInvoiceProduct fake data."""
    product: Product = ProductFactory()
    purchase_invoice: PurchaseInvoice = PurchaseInvoiceFactory()
    return {
        "product_id": product.id,
        "quantity": faker.pyint(),
        "price": faker.pyint(),
        "purchase_invoice_id": purchase_invoice.id,
        "products_left": faker.pyint(),
    }
