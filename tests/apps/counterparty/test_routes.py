"""Module for testing counterparty routes."""
import json
from typing import Dict, List

import pytest
from faker import Faker
from flask import url_for

from api import Discount
from tests.apps.counterparty.factories import DiscountFactory
from tests.conftest import check_instance_expected_data


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
        check_instance_expected_data(response, discount)

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
        check_instance_expected_data(response, expected_data)

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
        """Test put route. Without rate."""
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
        """Test put route. Same name."""
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
        """Test put route. Long name field."""
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


@pytest.mark.usefixtures("client_class")
class TestPatchDiscountRoute:
    """Class for testing Discount patch single instance route."""

    def test_patch_route(self, faker: Faker, auth_header: Dict) -> None:
        """Test patch route."""
        discount: Discount = DiscountFactory()
        expected_data: Dict = {
            "name": faker.pystr(min_chars=1, max_chars=30),
            "rate": faker.random_int(min=0, max=100),
        }
        response = self.client.patch(
            url_for("discountroute", instance_id=discount.id),
            headers=auth_header,
            data=json.dumps(expected_data),
        )
        check_instance_expected_data(response, expected_data)

    def test_patch_route_only_name(self, faker: Faker, auth_header: Dict) -> None:
        """Test patch route. Only name."""
        discount: Discount = DiscountFactory()
        expected_data: Dict = {
            "name": faker.pystr(min_chars=1, max_chars=30),
        }
        response = self.client.patch(
            url_for("discountroute", instance_id=discount.id),
            headers=auth_header,
            data=json.dumps(expected_data),
        )
        check_instance_expected_data(response, expected_data)


@pytest.mark.usefixtures("client_class")
class TestDeleteDiscountRoute:
    """Class for testing Discount delete single instance route."""

    def test_delete_route(self, auth_header: Dict) -> None:
        """Test delete route."""
        discount: Discount = DiscountFactory()
        response = self.client.delete(
            url_for("discountroute", instance_id=discount.id), headers=auth_header
        )
        assert response.status_code == 200
        assert not Discount.query.all()


@pytest.mark.usefixtures("client_class")
class TestPostDiscountsRoute:
    """Class for testing Discount post instance route."""

    def test_post_route(self, faker: Faker, auth_header: Dict) -> None:
        """Test post route."""
        expected_data: Dict = {
            "name": faker.pystr(min_chars=1, max_chars=30),
            "rate": faker.random_int(min=0, max=100),
        }
        response = self.client.post(
            url_for("discountsroute"),
            headers=auth_header,
            data=json.dumps(expected_data),
        )
        check_instance_expected_data(response, expected_data)


@pytest.mark.usefixtures("client_class")
class TestGetDiscountsRoute:
    """Class for testing Discount post instance route."""

    def test_get_route(self, auth_header: Dict) -> None:
        """Test get route. Discount list expected."""
        discounts: List[Discount] = DiscountFactory.create_batch(size=5)
        response = self.client.get(
            url_for("discountsroute"),
            headers=auth_header,
        )
        result = response.get_json()
        assert response.status_code == 200
        for i, discount in enumerate(discounts):
            for key, value in result[i].items():
                assert getattr(discount, key) == value
