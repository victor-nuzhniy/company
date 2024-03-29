"""Module for testing base routes."""
import json

import pytest
from faker import Faker
from flask import url_for

from api import Agreement, Counterparty, Discount
from tests.apps.counterparty.base.factories import (
    AgreementFactory,
    CounterpartyFactory,
    DiscountFactory,
)
from tests.apps.counterparty.base.testing_utilities import (
    create_agreement_data,
    create_counterparty_data,
    create_discount_data,
)
from tests.bases import TestType
from tests.testing_classes import SampleTestRoute


class TestDiscountRoute(SampleTestRoute):
    """Class with methods for testing Discount routes."""

    model = Discount
    factory = DiscountFactory

    def get_fake_data(self, faker: Faker) -> dict:
        """Get Discount fake data dict."""
        return create_discount_data(faker)

    def get_fake_put_data(self, faker: Faker) -> dict:
        """Get Discount fake data dict for put and patch methods."""
        return create_discount_data(faker)


@pytest.mark.usefixtures("client_class")
class TestPutDiscountRoute:
    """Class for testing Discount put single instance route."""

    def test_put_route_invalid_rate(
        self: TestType,
        faker: Faker,
        auth_header: dict,
    ) -> None:
        """Test put route. Involid rate."""
        discount: Discount = DiscountFactory()
        expected_data: dict = {
            "name": faker.pystr(min_chars=4, max_chars=10),
            "rate": faker.random_int(min=101),
        }
        response = self.client.put(
            url_for("discountroute", instance_id=discount.id),
            headers=auth_header,
            data=json.dumps(expected_data),
        )
        response_result = response.get_json()
        assert response.status_code == 400
        assert response_result.get("message") == {
            "rate": "".join(
                (
                    "Invalid argument: {rate}. ".format(rate=expected_data.get("rate")),
                    "argument must be within the range 0 - 100",
                ),
            ),
        }

    def test_put_route_without_rate(
        self: TestType,
        faker: Faker,
        auth_header: dict,
    ) -> None:
        """Test put route. Without rate."""
        discount: Discount = DiscountFactory()
        expected_data: dict = {
            "name": faker.pystr(min_chars=4, max_chars=10),
        }
        response = self.client.put(
            url_for("discountroute", instance_id=discount.id),
            headers=auth_header,
            data=json.dumps(expected_data),
        )
        response_result = response.get_json()
        assert response.status_code == 400
        assert response_result.get("message") == {
            "rate": "".join(
                (
                    "Missing required parameter in the JSON ",
                    "body or the post body or the query string",
                ),
            ),
        }

    def test_put_route_same_name(
        self: TestType,
        faker: Faker,
        auth_header: dict,
    ) -> None:
        """Test put route. Same name."""
        discount: Discount = DiscountFactory()
        another_discount: Discount = DiscountFactory()
        expected_data: dict = {
            "name": another_discount.name,
            "rate": faker.random_int(min=0, max=100),
        }
        response = self.client.put(
            url_for("discountroute", instance_id=discount.id),
            headers=auth_header,
            data=json.dumps(expected_data),
        )
        response_result = response.get_json()
        assert response.status_code == 409
        assert response_result.get(
            "message",
        ) == "Field name already has {name} value in discount table".format(
            name=another_discount.name,
        )

    def test_put_route_long_name(
        self: TestType,
        faker: Faker,
        auth_header: dict,
    ) -> None:
        """Test put route. Long name field."""
        discount: Discount = DiscountFactory()
        expected_data: dict = {
            "name": faker.pystr(min_chars=31, max_chars=40),
            "rate": faker.random_int(min=0, max=100),
        }
        response = self.client.put(
            url_for("discountroute", instance_id=discount.id),
            headers=auth_header,
            data=json.dumps(expected_data),
        )
        response_result = response.get_json()
        assert response.status_code == 400
        assert response_result.get("message") == {
            "name": "".join(
                (
                    "{name} length should be lower".format(
                        name=expected_data.get("name"),
                    ),
                    " than 30 character.",
                ),
            ),
        }


class TestAgreementRoute(SampleTestRoute):
    """Test AgreementRoute routes."""

    model = Agreement
    factory = AgreementFactory

    def get_fake_data(self, faker: Faker) -> dict:
        """Get Agreement fake data dict."""
        return create_agreement_data(faker)

    def get_fake_put_data(self, faker: Faker) -> dict:
        """Get Agreement fake data dict for put and patch methods."""
        return create_agreement_data(faker)


class TestCounterpartyRoute(SampleTestRoute):
    """Test CounterpartyRoute routes."""

    model = Counterparty
    factory = CounterpartyFactory

    def get_fake_data(self, faker: Faker) -> dict:
        """Get Counterparty fake data dict."""
        return create_counterparty_data(faker)

    def get_fake_put_data(self, faker: Faker) -> dict:
        """Get CounterParty fake data dict for put and patch methods."""
        return create_counterparty_data(faker)
