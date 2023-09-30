"""Pytest fixtures."""
import os
import random
import typing

import jwt
import pytest
from faker import Faker
from flask import Flask
from flask_restful import Api

from api import User, db
from api.apps.account.routes import (
    IncomeForPeriodRoute,
    PeriodReportRoute,
    ProcessSaleInvoiceRoute,
    ProductsLeftoversRoute,
)
from api.apps.auth.routes import AdminRoute, LoginRoute
from api.apps.auth.utils import encrypt_password
from api.apps.counterparty.routes import (
    AgreementRoute,
    AgreementsRoute,
    CounterpartiesRoute,
    CounterpartyRoute,
    DiscountRoute,
    DiscountsRoute,
)
from api.apps.invoice.routes import (
    InvoiceProductRoute,
    InvoiceProductsRoute,
    InvoiceRoute,
    InvoicesRoute,
)
from api.apps.order.routes import (
    OrderProductRoute,
    OrderProductsRoute,
    OrderRoute,
    OrdersRoute,
)
from api.apps.product.routes import (
    ProductRoute,
    ProductsRoute,
    ProductTypeRoute,
    ProductTypesRoute,
)
from api.apps.purchase.routes import (
    PurchaseInvoiceProductRoute,
    PurchaseInvoiceProductsRoute,
    PurchaseInvoiceRoute,
    PurchaseInvoicesRoute,
)
from api.apps.sale.routes import (
    SaleInvoiceProductRoute,
    SaleInvoiceProductsRoute,
    SaleInvoiceRoute,
    SaleInvoicesRoute,
)
from api.apps.tax.routes import (
    TaxInvoiceProductRoute,
    TaxInvoiceProductsRoute,
    TaxInvoiceRoute,
    TaxInvoicesRoute,
)
from api.apps.user.routes import AdminUserRoute, UserRoute, UsersRoute
from api.services import crud
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


@pytest.fixture(scope="function", autouse=True)
def faker_seed() -> None:
    """Generate random seed for Faker instance."""
    return random.seed(version=3)


@pytest.fixture(autouse=True)
def app():
    """Override dependencies for Flask and return flask instance."""
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
    app.config["TESTING"] = True
    app.config["DEBUG"] = False
    app.testing = True
    api = Api(app)
    api.add_resource(ProcessSaleInvoiceRoute, "/account/process-sale-invoice/")
    api.add_resource(PeriodReportRoute, "/account/sale-report/")
    api.add_resource(ProductsLeftoversRoute, "/account/product-leftovers/")
    api.add_resource(IncomeForPeriodRoute, "/account/income-for-period/")
    api.add_resource(LoginRoute, "/auth/login/")
    api.add_resource(AdminRoute, "/auth/create-admin/")

    api.add_resource(DiscountsRoute, "/discount/")
    api.add_resource(DiscountRoute, "/discount/<instance_id>")
    api.add_resource(CounterpartyRoute, "/counterpary/,<instance_id>")
    api.add_resource(CounterpartiesRoute, "/counterparty/")
    api.add_resource(AgreementRoute, "/agreement/<instance_id>")
    api.add_resource(AgreementsRoute, "/agreement/")
    api.add_resource(InvoiceRoute, "/invoice/<instance_id>")
    api.add_resource(InvoicesRoute, "/invoice/")
    api.add_resource(InvoiceProductRoute, "/invoice-product/<instance_id>")
    api.add_resource(InvoiceProductsRoute, "/invoice-product/")
    api.add_resource(OrderRoute, "/order/<instance_id>")
    api.add_resource(OrdersRoute, "/order/")
    api.add_resource(OrderProductRoute, "/order-product/<instance_id>")
    api.add_resource(OrderProductsRoute, "/order-product/")
    api.add_resource(ProductRoute, "/product/<instance_id>")
    api.add_resource(ProductsRoute, "/product/")
    api.add_resource(ProductTypeRoute, "/product-type/<instance_id>")
    api.add_resource(ProductTypesRoute, "/product-type/")
    api.add_resource(PurchaseInvoiceRoute, "/purchase-invoice/<instance_id>")
    api.add_resource(PurchaseInvoicesRoute, "/purchase-invoice/")
    api.add_resource(
        PurchaseInvoiceProductRoute, "/purchase-invoice-product/<instance_id>"
    )
    api.add_resource(PurchaseInvoiceProductsRoute, "/purchase-invoice-product/")
    api.add_resource(SaleInvoiceRoute, "/sale-invoice/<instance_id>")
    api.add_resource(SaleInvoicesRoute, "/sale-invoice/")
    api.add_resource(SaleInvoiceProductRoute, "/sale-invoice-product/<instance_id>")
    api.add_resource(SaleInvoiceProductsRoute, "/sale-invoice-product/")
    api.add_resource(TaxInvoiceRoute, "/tax-invoice/<instance_id>")
    api.add_resource(TaxInvoicesRoute, "/tax-invoice/")
    api.add_resource(TaxInvoiceProductRoute, "/tax-invoice-product/<instance_id>")
    api.add_resource(TaxInvoiceProductsRoute, "/tax-invoice-product/")
    api.add_resource(UserRoute, "/user/<instance_id>")
    api.add_resource(UsersRoute, "/user/")
    api.add_resource(AdminUserRoute, "/user/admin/<user_id>")

    db.init_app(app)
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture
def admin_user(faker: Faker) -> User:
    """Create admin user."""
    admin = crud.create(
        User,
        {
            "username": faker.user_name(),
            "email": faker.email(),
            "password": encrypt_password("11111"),
            "is_admin": True,
            "is_active": True,
        },
    )
    return admin


@pytest.fixture
def auth_header(admin_user: User, app: Flask) -> typing.Dict:
    """Get admin user authorization token."""
    token = jwt.encode(
        {"user_id": admin_user.id}, app.config["SECRET_KEY"], algorithm="HS256"
    )
    return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}


@pytest.fixture(autouse=True, scope="session")
def set_session_for_factories() -> None:
    """Register model factories to set up a scoped session during the test run."""
    known_factories: typing.List[typing.Type[BaseModelFactory]] = [
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
        factory_class._meta.sqlalchemy_session = db.session


def check_instance_expected_data(
    response: typing.Any, expected_data: typing.Dict | db.Model
) -> None:
    """
    Check response status whether it's 200.

    Compare instance data with expected.
    """
    result = response.get_json()
    assert response.status_code == 200
    if isinstance(expected_data, typing.Dict):
        for key, value in expected_data.items():
            assert result[key] == value
    else:
        for key, value in result.items():
            assert getattr(expected_data, key) == value
