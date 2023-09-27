"""Pytest fixtures."""
import os
import random

import pytest
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from api.apps.counterparty.models import Agreement, Counterparty, Discount
from api.apps.invoice.models import Invoice, InvoiceProduct
from api.apps.order.models import Order, OrderProduct
from api.apps.product.models import Product
from api.apps.purchase.models import PurchaseInvoice, PurchaseInvoiceProduct
from api.apps.sale.models import SaleInvoice, SaleInvoiceProduct
from api.apps.tax.models import TaxInvoice, TaxInvoiceProduct
from api.apps.user.models import User


@pytest.fixture(scope="function", autouse=True)
def faker_seed() -> None:
    """Generate random seed for Faker instance."""
    return random.seed(version=3)


@pytest.fixture
def app():
    """Override dependencies for Flask and return flask instance."""
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
    Api(app)
    Migrate(app, db)
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()
