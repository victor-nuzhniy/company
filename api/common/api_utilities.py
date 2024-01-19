"""Utilities for api."""
from typing import Dict, List, Optional

from flask import abort

from api.common.services import db_utils
from api.common.api_types import ModelType


def get_model_unique_fields_name(model: ModelType) -> List:
    """Get model unique fields names list."""
    names: List = []
    for column in model.__table__.columns:  # type: ignore
        if column.unique:
            names.append(column.name)
    return names


def check_unique(
    model: ModelType,
    data_values: Dict,
    instance_id: Optional[int] = None,
) -> None:
    """Check data_values for uniqueness."""
    unique_names: List = get_model_unique_fields_name(model)
    for name in unique_names:
        condition: bool = db_utils.check_unique_constraits(
            model,
            name,
            data_values.get(name),
            instance_id,
        )
        if name in data_values and condition:
            abort(
                409,
                "".join(
                    (
                        "Field {name} already has {data_value} value in ".format(
                            name=name,
                            data_value=data_values.get(name),
                        ),
                        "{table_name} table".format(
                            table_name=model.__table__,  # type: ignore
                        ),
                    ),
                ),
            )
