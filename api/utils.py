"""Utilities for api."""
from typing import Dict, List, Optional

from flask import abort

from api import db
from api.services import db_utils


def get_model_unique_fields_name(model: db.Model) -> List:
    """Get model unique fields names list."""
    names: List = []
    for column in model.__table__.columns:
        if column.unique:
            names.append(column.name)
    return names


def check_unique(
    model: db.Model, data: Dict, instance_id: Optional[int] = None
) -> None:
    """Check data for uniqueness."""
    unique_names: List = get_model_unique_fields_name(model)
    for name in unique_names:
        if name in data and db_utils.check_unique_constraits(
            model, name, data.get(name), instance_id
        ):
            abort(
                409,
                f"Field {name} already has {data.get(name)} value in "
                f"{model.__table__} table",
            )
