"""Init module for api app."""
import os

from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_restful_swagger import swagger
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["DEFAULT_RENDERERS"] = [
    "flask_api.renderers.JSONRenderer",
    "flask_api.renderers.BrowsableAPIRenderer",
]
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
api = swagger.docs(Api(app), apiVersion="0.1")
db = SQLAlchemy(app)

from api.apps.counterparty.models import Agreement, Counterparty, Discount
from api.apps.invoice.models import Invoice, InvoiceProduct
from api.apps.order.models import Order, OrderProduct
from api.apps.product.models import Product
from api.apps.purchase.models import PurchaseInvoice, PurchaseInvoiceProduct
from api.apps.sale.models import SaleInvoice, SaleInvoiceProduct
from api.apps.tax.models import TaxInvoice, TaxInvoiceProduct
from api.apps.user.models import User

migrate = Migrate(app, db)

from api.apps.account import routes
from api.apps.auth import routes
from api.apps.counterparty import routes
from api.apps.invoice import routes
from api.apps.order import routes
from api.apps.product import routes
from api.apps.purchase import routes
from api.apps.sale import routes
from api.apps.tax import routes
from api.apps.user import routes
