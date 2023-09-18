"""Init module for api app."""
import os

from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
api = Api(app)
db = SQLAlchemy(app)

from api.apps.counterparty.models import Agreement, Counterparty, Discount
from api.apps.invoice.models import Invoice, InvoiceProducts, SaleInvoice
from api.apps.order.models import Order, OrderProducts
from api.apps.product.models import Product
from api.apps.purchase.models import PurchaseInvoice, PurchaseInvoiceProducts
from api.apps.tax.models import TaxInvoice, TaxInvoiceProducts
from api.apps.user.models import User

migrate = Migrate(app, db)

from api.apps.user import routes
