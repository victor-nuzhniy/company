"""Init module for api app."""
import os

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_restful_swagger import swagger
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

from api import typing
from api.typing import ModelType

load_dotenv()

app = Flask(__name__)
cors = CORS(
    app,
    resources={r"/*": {"origins": "*", "allow_headers": "*", "expose_headers": "*"}},
)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["DEFAULT_RENDERERS"] = [
    "flask_api.renderers.JSONRenderer",
    "flask_api.renderers.BrowsableAPIRenderer",
]
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
api = swagger.docs(Api(app), apiVersion="0.1")


class Base(DeclarativeBase):
    """Base class for models instantiaton."""


db: SQLAlchemy = SQLAlchemy(model_class=Base)
db.init_app(app)

Model: ModelType = db.Model

migrate = Migrate(app, db)

from api.apps.account import routes
from api.apps.auth import routes
from api.apps.common_services import routes
from api.apps.counterparty import routes
from api.apps.invoice import routes
from api.apps.order import routes
from api.apps.product import routes
from api.apps.purchase import routes
from api.apps.sale import routes
from api.apps.tax import routes
from api.apps.user import routes
