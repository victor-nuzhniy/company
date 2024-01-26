"""Utilities for testing."""
import random
import typing

from flask.testing import FlaskClient

from api.common.api_types import ModelType


class Checkers(object):
    """Checkers helper function."""

    def check_instance_expected_data(
        self,
        response: typing.Any,
        expected_data: dict | ModelType,
    ) -> None:
        """
        Check response status whether it's 200.

        Compare instance data with expected.
        """
        result_response = response.get_json()
        assert response.status_code == 200
        if isinstance(expected_data, typing.Dict):
            for key, elem in expected_data.items():
                if key in result_response:
                    assert result_response[key] == elem
        else:
            for ky, el in result_response.items():
                if ky == "created_at":
                    assert (
                        getattr(expected_data, ky).strftime("%Y-%m-%d %H:%M:%S") == el
                    )
                else:
                    assert getattr(expected_data, ky) == el

    def compare_lists(
        self,
        first_list: list[ModelType],
        second_list: list[dict],
    ) -> None:
        """Check two dicts for equality."""
        for index, instance in enumerate(reversed(first_list)):
            for key, elem in second_list[index].items():
                if key == "created_at":
                    assert getattr(instance, key).strftime("%Y-%m-%d %H:%M:%S") == elem
                else:
                    assert getattr(instance, key) == elem


checkers = Checkers()


def delete_random_dict_key(data_dict: dict) -> dict:
    """Delete random dict key."""
    if len(data_dict) > 1:
        key = random.choice(list(data_dict.keys()))
        data_dict.pop(key)
    return data_dict


class InstanceWithClient(typing.Protocol):
    """Class with given attributes."""

    @property
    def client(self) -> FlaskClient:
        """Get Flask client."""
