"""Pytest fixtures."""
import os
import random
import typing

import pytest
from flask import Flask
from flask_restful import Api

from api import db
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
    Api(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture(autouse=True, scope="session")
def set_session_for_factories() -> None:
    """Register model factories to set up a scoped session during the test run."""
    known_factories: typing.List[typing.Type[BaseModelFactory]] = [
        UserFactory
        # === Add new factory classes here!!! ===
    ]

    for factory_class in known_factories:
        # Set up session to factory
        factory_class._meta.sqlalchemy_session = db.session
