"""Module for testing account apps routes."""
import json
from typing import Dict, List, Sequence

import pytest
from faker import Faker
from flask import url_for

from api import Product, SaleInvoice
from tests.apps.common.account.testing_utilities import (
    get_purchase_products,
    get_tax_products,
)
from tests.apps.product.factories import ProductFactory
from tests.apps.purchase.factories import PurchaseInvoiceProductFactory
from tests.apps.sale.factories import SaleInvoiceFactory, SaleInvoiceProductFactory
from tests.testing_utilities import InstanceWithClient


@pytest.mark.usefixtures("client_class")
class TestProcessSaleInvoiceRoute:
    """Class for testing ProcessSaleInvoiceRoute."""

    def test_post_route(  # noqa: WPS218
        self: InstanceWithClient, auth_header: Dict, faker: Faker,
    ) -> None:
        """Test ProcessSaleInvoiceRoute post route."""
        products: List[Product] = ProductFactory.create_batch(size=5)
        sale_invoice: SaleInvoice = SaleInvoiceFactory(done=False)
        sale_invoice_products: List = []
        purchase_invoice_products: List = []
        for product in products:
            quantity = faker.random_int(min=100)
            price = faker.random_int(min=1000)
            sale_invoice_products.append(
                SaleInvoiceProductFactory(
                    product_id=product.id,
                    quantity=quantity,
                    price=price,
                    sale_invoice_id=sale_invoice.id,
                ),
            )
            purchase_invoice_products.append(
                PurchaseInvoiceProductFactory(
                    product_id=product.id,
                    quantity=quantity + 100,
                    price=price - 20,
                    products_left=quantity + 100,
                ),
            )
        response = self.client.post(
            url_for("processsaleinvoiceroute"),
            headers=auth_header,
            data=json.dumps({"sale_invoice_id": sale_invoice.id}),
        )
        response_result = response.get_json()
        expected_purchase_products: Sequence = get_purchase_products(sale_invoice.id)
        for index, tax_product in enumerate(get_tax_products(sale_invoice.id)):
            assert (
                sale_invoice_products[index].id == tax_product.sale_invoice_products_id
            )
            assert (
                purchase_invoice_products[index].id
                == tax_product.purchase_invoice_products_id
            )
            assert tax_product.quantity == sale_invoice_products[index].quantity
            assert expected_purchase_products[index].products_left == 100
        assert response.status_code == 200
        assert response_result.get("message") == "Operation successfully performed"

    def test_post_route_sale_invoice_done(
        self: InstanceWithClient, auth_header: dict[str, str],
    ) -> None:
        """Test ProcessSaleInvoiceRoute post method, sale_invoice is done."""
        sale_invoice: SaleInvoice = SaleInvoiceFactory(done=True)
        response = self.client.post(
            url_for("processsaleinvoiceroute"),
            headers=auth_header,
            data=json.dumps({"sale_invoice_id": sale_invoice.id}),
        )
        response_result = response.get_json()
        assert response.status_code == 406
        assert response_result.get(
            "message",
        ) == "Sale_invoice with id {id} is already done!".format(id=sale_invoice.id)
