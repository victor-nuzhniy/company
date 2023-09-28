"""Module for testing counterparty routes."""
import pytest
from flask import url_for

from api import Discount
from tests.apps.counterparty.factories import DiscountFactory


@pytest.mark.usefixtures("client_class")
class TestGetDiscountRoute:
    """Class for testing discount routes."""

    def test_get_route(self) -> None:
        """Test get route."""
        discount: Discount = DiscountFactory()
        response = self.client.get(url_for("discountsroute", instance_id=discount.id))
        result = response.get_json()[0]
        assert response.status_code == 200
        for key, value in result.items():
            assert getattr(discount, key) == value
