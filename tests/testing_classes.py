"""Classes for testing."""
import json
from abc import abstractmethod
from typing import Dict, List, Optional

import pytest
from faker import Faker
from flask import url_for

from api import User, db
from tests.bases import BaseModelFactory
from tests.conftest import check_instance_expected_data, delete_random_dict_key


@pytest.mark.usefixtures("client_class")
class SampleTestRoute:
    """Class for testing model get single instance by id route."""

    model: Optional[db.Model] = None
    factory: Optional[BaseModelFactory] = None

    @abstractmethod
    def get_fake_data(self, faker: Faker):
        """Implement getting instance fake data."""
        pass

    @abstractmethod
    def get_fake_put_data(self, faker: Faker):
        """Implement getting instance fake data for patch method."""
        pass

    def test_get_route(self, auth_header: Dict) -> None:
        """Test get route."""
        instance: db.Model = self.factory()
        response = self.client.get(
            url_for(f"{self.model.__name__.lower()}route", instance_id=instance.id),
            headers=auth_header,
        )
        check_instance_expected_data(response, instance)

    def test_get_route_not_exist(self, faker: Faker, auth_header: Dict) -> None:
        """Test get route with not existed instance."""
        instance_id: int = faker.random_int(min=9000)
        response = self.client.get(
            url_for(f"{self.model.__name__.lower()}route", instance_id=instance_id),
            headers=auth_header,
        )
        result = response.get_json()
        assert response.status_code == 404
        assert (
            result.get("message")
            == f"{self.model.__name__} with data ['id: {instance_id}'] doesn't exist"
        )

    def test_put_route(self, faker: Faker, auth_header: Dict) -> None:
        """Test put route."""
        instance: db.Model = self.factory()
        expected_data: Dict = self.get_fake_put_data(faker)
        response = self.client.put(
            url_for(f"{self.model.__name__.lower()}route", instance_id=instance.id),
            headers=auth_header,
            data=json.dumps(expected_data),
        )
        check_instance_expected_data(response, expected_data)

    def test_patch_route(self, faker: Faker, auth_header: Dict) -> None:
        """Test patch_route."""
        instance: db.Model = self.factory()
        expected_data: Dict = self.get_fake_put_data(faker)
        expected_data = delete_random_dict_key(expected_data)
        response = self.client.patch(
            url_for(f"{self.model.__name__.lower()}route", instance_id=instance.id),
            headers=auth_header,
            data=json.dumps(expected_data),
        )
        check_instance_expected_data(response, expected_data)

    def test_delete_route(self, auth_header: Dict, app) -> None:
        """Test delete route."""
        instance: db.Model = self.factory()
        instance_id: int = instance.id
        response = self.client.delete(
            url_for(f"{self.model.__name__.lower()}route", instance_id=instance.id),
            headers=auth_header,
        )
        assert response.status_code == 200
        assert not self.model.query.filter_by(id=instance_id).first()

    def test_post_route(self, faker: Faker, auth_header: Dict) -> None:
        """Test post route."""
        expected_data: Dict = self.get_fake_data(faker)
        expected_data.pop("created_at", None)
        response = self.client.post(
            url_for(f"{self.model.__name__.lower()}sroute"),
            headers=auth_header,
            data=json.dumps(expected_data),
        )
        check_instance_expected_data(response, expected_data)

    def test_get_many_route(self, auth_header: Dict, admin_user: User) -> None:
        """Test get route. Model list expected."""
        instances: List[db.Model] = self.factory.create_batch(size=5)
        if self.model == User:
            instances = [admin_user] + instances
        response = self.client.get(
            url_for(f"{self.model.__name__.lower()}sroute"),
            headers=auth_header,
        )
        result = response.get_json()
        assert response.status_code == 200
        for i, instance in enumerate(instances):
            for key, value in result[i].items():
                if key == "created_at":
                    assert getattr(instance, key).strftime("%Y-%m-%dT%H:%M:%S") == value
                else:
                    assert getattr(instance, key) == value
