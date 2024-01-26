"""Classes for testing."""
import json
from abc import abstractmethod
from typing import Any, Optional, Type

import pytest
from faker import Faker
from flask import Flask, url_for
from flask.testing import FlaskClient

from api import User
from api.common.api_types import ModelType
from tests.bases import BaseModelFactory
from tests.conftest import FixtureFunc
from tests.testing_utilities import checkers, delete_random_dict_key


@pytest.mark.usefixtures("client_class")
class SampleTestRoute:  # noqa WPS214
    """Class for testing model get single instance by id route."""

    model: Optional[ModelType] = None
    factory: Optional[Type[BaseModelFactory]] = None

    @property
    def client(self) -> FlaskClient:
        """Get flask client."""
        return FlaskClient()

    @abstractmethod
    def get_fake_data(self, faker: Faker) -> dict:
        """Implement getting instance fake data."""

    @abstractmethod
    def get_fake_put_data(self, faker: Faker) -> dict:
        """Implement getting instance fake data for patch method."""

    def test_get_route(self, auth_header: dict) -> None:
        """Test get route."""
        if self.factory and self.model:
            instance: ModelType = self.factory()
            response = self.client.get(
                url_for(
                    "{name}route".format(name=self.model.__name__.lower()),
                    instance_id=instance.id,  # type: ignore
                ),
                headers=auth_header,
            )
            checkers.check_instance_expected_data(response, instance)
        else:
            raise AssertionError("Improperly configured.")

    def test_get_route_not_exist(self, faker: Faker, auth_header: dict) -> None:
        """Test get route with not existed instance."""
        instance_id: int = faker.random_int(min=9000)
        response = self.client.get(
            url_for(
                "{name}route".format(name=self.model.__name__.lower()),  # type: ignore
                instance_id=instance_id,
            ),
            headers=auth_header,
        )
        response_result = response.get_json()
        assert response.status_code == 404
        assert response_result.get(
            "message",
        ) == "{name} with dataid: {id} doesn't exist".format(
            name=self.model.__name__,  # type: ignore
            id=instance_id,
        )

    def test_put_route(self, faker: Faker, auth_header: dict) -> None:
        """Test put route."""
        if self.factory and self.model:
            instance: ModelType = self.factory()
            expected_data: dict = self.get_fake_put_data(faker)
            response = self.client.put(
                url_for(
                    "{name}route".format(
                        name=self.model.__name__.lower(),
                    ),
                    instance_id=instance.id,  # type: ignore
                ),
                headers=auth_header,
                data=json.dumps(expected_data),
            )
            checkers.check_instance_expected_data(response, expected_data)
        else:
            raise AssertionError("Improperly configured.")

    def test_patch_route(self, faker: Faker, auth_header: dict) -> None:
        """Test patch_route."""
        if self.factory and self.model:
            instance: ModelType = self.factory()
            expected_data: dict = self.get_fake_put_data(faker)
            expected_data = delete_random_dict_key(expected_data)
            response = self.client.patch(
                url_for(
                    "{name}route".format(name=self.model.__name__.lower()),
                    instance_id=instance.id,  # type: ignore
                ),
                headers=auth_header,
                data=json.dumps(expected_data),
            )
            checkers.check_instance_expected_data(response, expected_data)
        else:
            raise AssertionError("Improperly configured.")

    def test_delete_route(self, auth_header: dict, app: FixtureFunc[Flask]) -> None:
        """Test delete route."""
        if self.factory and self.model:
            instance: ModelType = self.factory()
            instance_id: int = instance.id  # type: ignore
            response = self.client.delete(
                url_for(
                    "{name}route".format(name=self.model.__name__.lower()),
                    instance_id=instance.id,  # type: ignore
                ),
                headers=auth_header,
            )
            assert response.status_code == 200
            assert not self.model.query.filter_by(id=instance_id).first()
        else:
            raise AssertionError("Improperly configured.")

    def test_post_route(self, faker: Faker, auth_header: dict) -> None:
        """Test post route."""
        expected_data: dict = self.get_fake_data(faker)
        expected_data.pop("created_at", None)
        response = self.client.post(
            url_for(
                "{name}sroute".format(name=self.model.__name__.lower()),  # type: ignore
            ),
            headers=auth_header,
            data=json.dumps(expected_data),
        )
        checkers.check_instance_expected_data(response, expected_data)

    def test_get_many_route(self, auth_header: dict, admin: User) -> None:
        """Test get route. Model list expected."""
        if self.factory and self.model:
            instances: list[ModelType | Any] = self.factory.create_batch(size=5)
            if self.model == User:
                instances = [admin] + instances
            response = self.client.get(
                url_for("{name}sroute".format(name=self.model.__name__.lower())),
                headers=auth_header,
            )
            response_result = response.get_json()
            assert response.status_code == 200
            checkers.compare_lists(instances, response_result)
        else:
            raise AssertionError("Improperly configured.")
