"""Pytest fixtures."""
import os
import random
import typing

import jwt
import pytest
from flask import Flask
from flask_restful import Api

from api import User, db
from api.apps.common.account import routes as account_routes
from api.apps.common.auth import routes as auth_routes
from api.apps.common.auth.auth_utilities import encrypt_password
from api.apps.common.special import routes as common_special_routes
from api.apps.counterparty.base import routes as counterparty_base_routes
from api.apps.counterparty.special import routes as counterparty_special_routes
from api.apps.invoice.base import routes as invoice_base_routes
from api.apps.invoice.special import routes as invoice_special_routes
from api.apps.order.base import routes as order_base_routes
from api.apps.order.special import routes as order_special_routes
from api.apps.product.base import routes as product_base_routes
from api.apps.purchase.base import routes as purchase_base_routes
from api.apps.purchase.special import routes as purchase_special_routes
from api.apps.sale.base import routes as sale_base_routes
from api.apps.sale.special import routes as sale_special_routes
from api.apps.tax.base import routes as tax_base_routes
from api.apps.tax.special import routes as tax_special_routes
from api.apps.user.base import routes as user_base_routes
from api.apps.user.special import routes as user_special_routes
from api.common.api_types import ModelType
from api.common.services import crud
from tests.apps.counterparty.factories import (
    AgreementFactory,
    CounterpartyFactory,
    DiscountFactory,
)
from tests.apps.invoice.factories import InvoiceFactory, InvoiceProductFactory
from tests.apps.order.factories import OrderFactory, OrderProductFactory
from tests.apps.product.factories import ProductFactory, ProductTypeFactory
from tests.apps.purchase.factories import (
    PurchaseInvoiceFactory,
    PurchaseInvoiceProductFactory,
)
from tests.apps.sale.factories import SaleInvoiceFactory, SaleInvoiceProductFactory
from tests.apps.tax.factories import TaxInvoiceFactory, TaxInvoiceProductFactory
from tests.apps.user.factories import UserFactory
from tests.bases import BaseModelFactory

FixtureValue = typing.TypeVar("FixtureValue")

# The type of the fixture function (type variable).
FixtureFunction = typing.TypeVar("FixtureFunction", bound=typing.Callable[..., object])

# The type of a fixture function (type alias generic in fixture value).
FixtureFunc = typing.Union[
    typing.Callable[..., FixtureValue],
    typing.Callable[..., typing.Generator[FixtureValue, None, None]],
]


@pytest.fixture(scope="function", autouse=True)
def faker_seed() -> None:
    """Generate random seed for Faker instance."""
    return random.seed(version=3)


@pytest.fixture(scope="session", autouse=True)
def app() -> typing.Generator[Flask, None, None]:  # noqa WPS213
    """Override dependencies for Flask and return flask instance."""
    application = Flask(__name__)
    application.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    application.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
    application.config["TESTING"] = True
    application.config["DEBUG"] = False
    application.testing = True
    api = Api(application)

    api.add_resource(
        account_routes.ProcessSaleInvoiceRoute,
        "/account/process-base-base/",
    )
    api.add_resource(account_routes.PeriodReportRoute, "/account/base-report/")
    api.add_resource(account_routes.ProductsLeftoversRoute, "/account/base-leftovers/")
    api.add_resource(account_routes.IncomeForPeriodRoute, "/account/income-for-period/")

    api.add_resource(auth_routes.LoginRoute, "/auth/login/")
    api.add_resource(auth_routes.AdminRoute, "/auth/create-admin/")

    api.add_resource(common_special_routes.NameNumberRoute, "/account/<model_name>/")

    api.add_resource(counterparty_base_routes.DiscountRoute, "/discount/<instance_id>/")
    api.add_resource(counterparty_base_routes.DiscountsRoute, "/discount/")
    api.add_resource(
        counterparty_base_routes.CounterpartyRoute,
        "/counterpary/,<instance_id>/",
    )
    api.add_resource(counterparty_base_routes.CounterpartysRoute, "/counterparty/")
    api.add_resource(
        counterparty_base_routes.AgreementRoute,
        "/agreement/<instance_id>/",
    )
    api.add_resource(counterparty_base_routes.AgreementsRoute, "/agreement/")

    api.add_resource(
        counterparty_special_routes.CounterpartyAgreementsRoute,
        "/agreements/<company_id>/",
    )

    api.add_resource(invoice_base_routes.InvoiceRoute, "/invoice/<instance_id>/")
    api.add_resource(invoice_base_routes.InvoicesRoute, "/invoice/")
    api.add_resource(
        invoice_base_routes.InvoiceProductRoute,
        "/invoice-product/<instance_id>/",
    )
    api.add_resource(invoice_base_routes.InvoiceProductsRoute, "/invoice-product/")

    api.add_resource(invoice_special_routes.InvoiceRegistryRoute, "/invoice-registry/")
    api.add_resource(
        invoice_special_routes.InvoicesProductsRoute,
        "/invoice-products/<invoice_id>/",
    )
    api.add_resource(
        invoice_special_routes.AgreementInvoicesRoute,
        "/invoices/<agreement_id>/",
    )

    api.add_resource(order_base_routes.OrderRoute, "/order/<instance_id>/")
    api.add_resource(order_base_routes.OrdersRoute, "/order/")
    api.add_resource(
        order_base_routes.OrderProductRoute,
        "/order-product/<instance_id>/",
    )
    api.add_resource(order_base_routes.OrderProductsRoute, "/order-product/")

    api.add_resource(order_special_routes.OrderRegistryRoute, "/order-registry/")
    api.add_resource(
        order_special_routes.OrdersProductsRoute,
        "/orders-products/<order_id>/",
    )
    api.add_resource(order_special_routes.UserOrderRoute, "/user-order/")
    api.add_resource(
        order_special_routes.CounterpartyOrdersRoute,
        "/orders/<company_id>/",
    )

    api.add_resource(product_base_routes.ProductRoute, "/product/<instance_id>/")
    api.add_resource(product_base_routes.ProductsRoute, "/product/")
    api.add_resource(
        product_base_routes.ProductTypeRoute,
        "/product-type/<instance_id>/",
    )
    api.add_resource(product_base_routes.ProductTypesRoute, "/product-type/")

    api.add_resource(
        purchase_base_routes.PurchaseInvoiceRoute,
        "/purchase-invoice/<instance_id>/",
    )
    api.add_resource(purchase_base_routes.PurchaseInvoicesRoute, "/purchase-invoice/")
    api.add_resource(
        purchase_base_routes.PurchaseInvoiceProductRoute,
        "/purchase-invoice-product/<instance_id>/",
    )
    api.add_resource(
        purchase_base_routes.PurchaseInvoiceProductsRoute,
        "/purchase-invoice-product/",
    )

    api.add_resource(
        purchase_special_routes.PurchaseRegistryRoute,
        "/purchase-registry/",
    )
    api.add_resource(
        purchase_special_routes.PurchaseInvoicesProductsRoute,
        "/purchase-invoice-products/<purchase_invoice_id>/",
    )
    api.add_resource(
        purchase_special_routes.PurchaseInvoiceProductsLeftRoute,
        "/purchase-invoice-products/product/<product_id>/",
    )

    api.add_resource(sale_base_routes.SaleInvoiceRoute, "/sale-invoice/<instance_id>/")
    api.add_resource(sale_base_routes.SaleInvoicesRoute, "/sale-invoice/")
    api.add_resource(
        sale_base_routes.SaleInvoiceProductRoute,
        "/sale-invoice-product/<instance_id>/",
    )
    api.add_resource(
        sale_base_routes.SaleInvoiceProductsRoute,
        "/sale-invoice-product/",
    )

    api.add_resource(sale_special_routes.SaleRegistryRoute, "/sale-invoice-registry/")
    api.add_resource(
        sale_special_routes.SaleInvoicesProductsRoute,
        "/sale-invoice-products/<sale_invoice_id>/",
    )
    api.add_resource(
        sale_special_routes.TaxSaleInvoiceProductsLeftRoute,
        "/sale-invoice-products/<sale_invoice_id>/<tax_invoice_id>/",
    )
    api.add_resource(
        sale_special_routes.AgreementSaleInvoicesRoute,
        "/agreement-sale-invoices/<agreement_id>/",
    )

    api.add_resource(tax_base_routes.TaxInvoiceRoute, "/tax-invoice/<instance_id>/")
    api.add_resource(tax_base_routes.TaxInvoicesRoute, "/tax-invoice/")
    api.add_resource(
        tax_base_routes.TaxInvoiceProductRoute,
        "/tax-invoice-product/<instance_id>/",
    )
    api.add_resource(tax_base_routes.TaxInvoiceProductsRoute, "/tax-invoice-product/")

    api.add_resource(tax_special_routes.TaxRegistryRoute, "/tax-registry/")
    api.add_resource(
        tax_special_routes.TaxInvoicesProductsRoute,
        "/tax-invoice-products/<tax_invoice_id>/",
    )
    api.add_resource(
        tax_special_routes.TaxInvoiceProductCreateRoute,
        "/tax-invoice-product-create/",
    )
    api.add_resource(
        tax_special_routes.TaxInvoiceProductDeleteRoute,
        "/tax-invoice-product-delete/<tax_invoice_product_id>/",
    )
    api.add_resource(
        tax_special_routes.TaxInvoiceDeleteRoute,
        "/tax-invoice-delete/<tax_invoice_id>/",
    )

    api.add_resource(user_base_routes.UserRoute, "/user/<instance_id>/")
    api.add_resource(user_base_routes.UsersRoute, "/user/")

    api.add_resource(user_special_routes.AdminUserRoute, "/user/admin/<user_id>/")

    db.init_app(application)
    with application.app_context():
        db.create_all()
        yield application
        db.drop_all()


@pytest.fixture(scope="session")
def admin_user() -> User:
    """Create admin base."""
    return crud.create(
        User,
        {
            "username": "administrator",
            "email": "elegance@abc.com",
            "password": encrypt_password("11111"),
            "is_admin": True,
            "is_active": True,
        },
    )


@pytest.fixture(scope="session")
def auth_header(admin: User, application: Flask) -> dict:
    """Get admin base authorization token."""
    token = jwt.encode(
        {"user_id": admin.id},
        application.config["SECRET_KEY"],
        algorithm="HS256",
    )
    return {
        "Authorization": "Bearer {token}".format(token=token),
        "Content-Type": "application/json",
    }


@pytest.fixture(autouse=True, scope="session")
def set_session_for_factories() -> None:
    """Register model factories to set up a scoped session during the test run."""
    known_factories: list[typing.Type[BaseModelFactory]] = [
        AgreementFactory,
        CounterpartyFactory,
        DiscountFactory,
        InvoiceFactory,
        InvoiceProductFactory,
        OrderFactory,
        OrderProductFactory,
        ProductFactory,
        ProductTypeFactory,
        PurchaseInvoiceFactory,
        PurchaseInvoiceProductFactory,
        SaleInvoiceFactory,
        SaleInvoiceProductFactory,
        TaxInvoiceFactory,
        TaxInvoiceProductFactory,
        UserFactory,
    ]

    for factory_class in known_factories:
        # Set up session to factory
        factory_class._meta.sqlalchemy_session = db.session  # noqa WPS347


def check_instance_expected_data(
    response: typing.Any,
    expected_data: dict | ModelType,
) -> None:
    """
    Check response status whether it's 200.

    Compare instance data with expected.
    """
    result_response = response.get_json()
    assert response.status_code == 200
    if isinstance(expected_data, typing.Dict):
        for key, elem in expected_data.items():
            if key in result_response:
                assert result_response[key] == elem
    else:
        for ky, el in result_response.items():
            if ky == "created_at":
                assert getattr(expected_data, ky).strftime("%Y-%m-%dT%H:%M:%S") == el
            else:
                assert getattr(expected_data, ky) == el


def delete_random_dict_key(data_dict: dict) -> dict:
    """Delete random dict key."""
    if len(data_dict) > 1:
        key = random.choice(list(data_dict.keys()))
        data_dict.pop(key)
    return data_dict
