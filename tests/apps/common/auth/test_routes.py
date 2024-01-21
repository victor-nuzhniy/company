"""Module for testing auth apps routes."""
import json
from typing import Dict
from unittest.mock import MagicMock, patch

import jwt
import pytest
from faker import Faker
from flask import Flask, url_for

from api import User
from tests.apps.user.base.testing_utilities import (
    create_user_data,
    create_user_put_data,
)
from tests.testing_utilities import checkers


@pytest.mark.usefixtures("client_class")
class TestAdminRoute:
    """Class for testing AdminRoute."""

    @patch("flask_restful.reqparse.RequestParser.parse_args")
    def test_post_route(self, get_mock: MagicMock, faker: Faker) -> None:
        """Test AdminRoute post method."""
        expected_data: Dict = create_user_data(faker)
        expected_data["admin_password"] = "Emilia231"   # noqa: S105
        get_mock.return_value = expected_data
        response = self.client.post(
            url_for("adminroute"),
            headers={"Content-Type": "application/json"},
            data=json.dumps(expected_data),
        )
        checkers.check_instance_expected_data(response, expected_data)

    def test_post_route_invalid_admin_password(self, faker: Faker) -> None:
        """Test AdminRoute post method."""
        expected_data: Dict = create_user_data(faker)
        expected_data["admin_password"] = "Emilia231"   # noqa: S105
        response = self.client.post(
            url_for("adminroute"),
            headers={"Content-Type": "application/json"},
            data=json.dumps(expected_data),
        )
        assert response.status_code == 400
        assert response.get_json().get("message") == {
            "admin_password": "Access denied. Value is invalid.",
        }


@pytest.mark.usefixtures("client_class")
class TestLoginRoute:
    """Class for testing LoginRoute."""

    def test_post_route(self, auth_header: Dict, faker: Faker, app: Flask) -> None:
        """Test post route."""
        expected_data: Dict = create_user_put_data(faker)
        user: User = self.client.post(
            url_for("usersroute"),
            headers=auth_header,
            data=json.dumps(expected_data),
        ).get_json()
        response = self.client.post(
            url_for("loginroute"),
            headers={"Content-Type": "application/json"},
            data=json.dumps(
                {
                    "email": expected_data.get("email"),
                    "password": expected_data.get("password"),
                },
            ),
        )
        response_result = response.get_json()
        assert response.status_code == 200
        assert response_result.get("message") == "Successfully fetched auth token"
        assert response_result.get("data") == jwt.encode(
            {"user_id": user.get("id")}, app.config["SECRET_KEY"], algorithm="HS256",
        )
