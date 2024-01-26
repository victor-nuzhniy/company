"""Fixtures for tax apps."""
from typing import Dict

from faker import Faker

from api import PurchaseInvoiceProduct, SaleInvoice, SaleInvoiceProduct, TaxInvoice
from tests.apps.purchase.base.factories import PurchaseInvoiceProductFactory
from tests.apps.sale.base.factories import SaleInvoiceFactory, SaleInvoiceProductFactory
from tests.apps.tax.base.factories import TaxInvoiceFactory


def create_tax_invoice_data(faker: Faker) -> Dict:
    """Create TaxInvoice fake data."""
    sale_invoice: SaleInvoice = SaleInvoiceFactory()
    return {
        "name": faker.pystr(min_chars=1, max_chars=100),
        "sale_invoice_id": sale_invoice.id,
    }


def create_tax_invoice_put_data(faker: Faker) -> Dict:
    """Create TaxInvoice fake data."""
    sale_invoice: SaleInvoice = SaleInvoiceFactory()
    return {
        "name": faker.pystr(min_chars=1, max_chars=100),
        "sale_invoice_id": sale_invoice.id,
        "created_at": faker.date_time().strftime("%Y-%m-%d %H:%M:%S"),
    }


def create_tax_invoice_product_data(faker: Faker) -> Dict:
    """Create TaxInvoiceProduct data."""
    tax_invoice: TaxInvoice = TaxInvoiceFactory()
    sale_invoice_product: SaleInvoiceProduct = SaleInvoiceProductFactory()
    purchase_invoice_product: PurchaseInvoiceProduct = PurchaseInvoiceProductFactory()
    return {
        "tax_invoice_id": tax_invoice.id,
        "sale_invoice_product_id": sale_invoice_product.id,
        "purchase_invoice_product_id": purchase_invoice_product.id,
        "quantity": faker.pyint(),
    }
