"""Module for testing auth apps routes."""
import json
from typing import Dict
from unittest.mock import MagicMock, patch

import pytest
from faker import Faker
from flask import url_for

from tests.apps.user.conftest import create_user_data
from tests.conftest import check_instance_expected_data


@pytest.mark.usefixtures("client_class")
class TestAdminRoute:
    """Class for testing AdminRoute."""

    @patch("flask_restful.reqparse.RequestParser.parse_args")
    def test_post_route(self, get_mock: MagicMock, faker: Faker) -> None:
        """Test AdminRoute post method."""
        expected_data: Dict = create_user_data(faker)
        expected_data["admin_password"] = "111"
        get_mock.return_value = expected_data
        response = self.client.post(
            url_for("adminroute"),
            headers={"Content-Type": "application/json"},
            data=json.dumps(expected_data),
        )
        check_instance_expected_data(response, expected_data)

    def test_post_route_invalid_admin_password(self, faker: Faker) -> None:
        """Test AdminRoute post method."""
        expected_data: Dict = create_user_data(faker)
        expected_data["admin_password"] = "111"
        response = self.client.post(
            url_for("adminroute"),
            headers={"Content-Type": "application/json"},
            data=json.dumps(expected_data),
        )
        assert response.status_code == 400
        assert response.get_json().get("message") == {
            "admin_password": "Access denied. Value is invalid."
        }
