"""Module for testing base apps routes."""
import json
from typing import Dict

import pytest
from faker import Faker
from flask import url_for

from api import User
from tests.apps.user.base.factories import UserFactory
from tests.apps.user.base.testing_utilities import (
    create_user_data,
    create_user_put_data,
)
from tests.bases import TestType
from tests.testing_classes import SampleTestRoute
from tests.testing_utilities import checkers


class TestUserRoutes(SampleTestRoute):
    """Class with methods for testing User routes."""

    model = User
    factory = UserFactory

    def get_fake_data(self, faker: Faker) -> Dict:
        """Get User fake data dict."""
        return create_user_data(faker)

    def get_fake_put_data(self, faker: Faker) -> Dict:
        """Get User fake data dict for put and patch methods."""
        return create_user_put_data(faker)


@pytest.mark.usefixtures("client_class")
class TestAdminUserRoute:
    """Class for testing User patch by id route."""

    def test_patch_route(self: TestType, auth_header: Dict) -> None:
        """Test patch User instance - is_active and is_admin only by admin base."""
        instance: User = UserFactory(is_admin=False, is_active=False)
        expected_data: Dict = {"is_admin": True, "is_active": True}
        response = self.client.patch(
            url_for("adminuserroute", user_id=instance.id),
            headers=auth_header,
            data=json.dumps(expected_data),
        )
        checkers.check_instance_expected_data(response, expected_data)
