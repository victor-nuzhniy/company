"""Module for testing counterparty routes."""
import json
from typing import Dict

import pytest
from faker import Faker
from flask import url_for

from api import Discount
from tests.apps.counterparty.factories import DiscountFactory


@pytest.mark.usefixtures("client_class")
class TestGetDiscountRoute:
    """Class for testing discount get single instance by id route."""

    def test_get_route(self, auth_header: Dict) -> None:
        """Test get route."""
        discount: Discount = DiscountFactory()
        response = self.client.get(
            url_for("discountroute", instance_id=discount.id),
            headers=auth_header,
        )
        result = response.get_json()
        assert response.status_code == 200
        for key, value in result.items():
            assert getattr(discount, key) == value

    def test_get_route_not_exist(self, faker: Faker, auth_header: Dict) -> None:
        """Test get route with not existed instance."""
        discount_id: int = faker.random_int(min=9000)
        response = self.client.get(
            url_for("discountroute", instance_id=discount_id),
            headers=auth_header,
        )
        result = response.get_json()
        assert response.status_code == 404
        assert (
            result.get("message")
            == f"Discount with data ['id: {discount_id}'] doesn't exist"
        )


@pytest.mark.usefixtures("client_class")
class TestPutDiscountRoute:
    """Class for testing Discount put single instance route."""

    def test_put_route(self, faker: Faker, auth_header: Dict) -> None:
        """Test put route."""
        discount: Discount = DiscountFactory()
        expected_data: Dict = {
            "name": faker.pystr(min_chars=4, max_chars=10),
            "rate": faker.random_int(min=0, max=100),
        }
        response = self.client.put(
            url_for("discountroute", instance_id=discount.id),
            headers=auth_header,
            data=json.dumps(expected_data),
        )
        result = response.get_json()
        assert response.status_code == 200
        for key, value in expected_data.items():
            assert result[key] == value

    def test_put_route_invalid_rate(self, faker: Faker, auth_header: Dict) -> None:
        """Test put route. Involid rate."""
        discount: Discount = DiscountFactory()
        expected_data: Dict = {
            "name": faker.pystr(min_chars=4, max_chars=10),
            "rate": faker.random_int(min=101),
        }
        response = self.client.put(
            url_for("discountroute", instance_id=discount.id),
            headers=auth_header,
            data=json.dumps(expected_data),
        )
        result = response.get_json()
        assert response.status_code == 400
        assert result.get("message") == {
            "rate": f"Invalid argument: {expected_data.get('rate')}. "
            f"argument must be within the range 0 - 100"
        }

    def test_put_route_without_rate(self, faker: Faker, auth_header: Dict) -> None:
        """Test put route. Same name."""
        discount: Discount = DiscountFactory()
        expected_data: Dict = {
            "name": faker.pystr(min_chars=4, max_chars=10),
        }
        response = self.client.put(
            url_for("discountroute", instance_id=discount.id),
            headers=auth_header,
            data=json.dumps(expected_data),
        )
        result = response.get_json()
        assert response.status_code == 400
        assert result.get("message") == {
            "rate": "Missing required parameter in the JSON "
            "body or the post body or the query string"
        }

    def test_put_route_same_name(self, faker: Faker, auth_header: Dict) -> None:
        """Test put route. Without rate."""
        discount: Discount = DiscountFactory()
        another_discount: Discount = DiscountFactory()
        expected_data: Dict = {
            "name": another_discount.name,
            "rate": faker.random_int(min=0, max=100),
        }
        response = self.client.put(
            url_for("discountroute", instance_id=discount.id),
            headers=auth_header,
            data=json.dumps(expected_data),
        )
        result = response.get_json()
        assert response.status_code == 409
        assert (
            result.get("message")
            == f"Field name already has {another_discount.name} value in discount table"
        )

    def test_put_route_long_name(self, faker: Faker, auth_header: Dict) -> None:
        """Test put route."""
        discount: Discount = DiscountFactory()
        expected_data: Dict = {
            "name": faker.pystr(min_chars=31, max_chars=40),
            "rate": faker.random_int(min=0, max=100),
        }
        response = self.client.put(
            url_for("discountroute", instance_id=discount.id),
            headers=auth_header,
            data=json.dumps(expected_data),
        )
        result = response.get_json()
        assert response.status_code == 400
        assert result.get("message") == {
            "name": f"{expected_data.get('name')} length should be lower"
            f" than 30 character."
        }
