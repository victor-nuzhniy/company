"""Init module for api app."""
import os

from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
db = SQLAlchemy(app)

from .models import (
    Agreement,
    Counterparty,
    Discount,
    Invoice,
    InvoiceProducts,
    Order,
    OrderProducts,
    Product,
    PurchaseInvoice,
    PurchaseInvoiceProducts,
    SaleInvoice,
    TaxInvoice,
    TaxInvoiceProducts,
    User,
)

migrate = Migrate(app, db)

from api import routes
