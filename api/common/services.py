"""Db service functionality for api."""
from typing import Any, Optional, Sequence

from flask import abort
from sqlalchemy import (
    CursorResult,
    Result,
    Select,
    and_,
    delete,
    insert,
    select,
    update,
)
from sqlalchemy.sql.dml import ReturningInsert

from api import db
from api.common.api_types import ModelType


class AbortMethods(object):
    """Class with methods that performing abort operation."""

    def raise_forbidden_error(self, ex: str) -> None:
        """Raise forbidden error."""
        abort(
            403,
            "Authentication token is invalid. Error - {ex}".format(
                ex=ex,
            ),
        )

    def raise_not_found_error(self, data_values: dict, name: str) -> None:
        """Raise not found error."""
        abort(
            404,
            "".join(
                (
                    "{name} with data".format(name=name),
                    *[
                        "{key}: {elem}".format(
                            key=key,
                            elem=elem,
                        )
                        for key, elem in data_values.items()
                    ],
                    " doesn't exist",
                ),
            ),
        )


abort_methods = AbortMethods()


class CRUDOperations(object):
    """CRUD operations for api app."""

    def create(
        self,
        model: ModelType,
        data_values: dict,
    ) -> Any:
        """Create model instance with given data_values."""
        insert_statement: ReturningInsert = (
            insert(model).values(**data_values).returning(model)
        )
        statement = (
            select(model)
            .from_statement(insert_statement)
            .execution_options(populate_existing=True)
        )
        result_value: Result = db.session.execute(statement=statement)
        result_data: Any = result_value.scalar_one()
        db.session.commit()
        return result_data

    def create_many(
        self,
        model: ModelType,
        data_values: list[dict],
    ) -> Sequence[Any]:
        """Create many model instances with given data_values."""
        insert_statement = insert(model).values(data_values).returning(model)
        statement = (
            select(model)
            .from_statement(insert_statement)
            .execution_options(populate_existing=True)
        )
        result_value: Result = db.session.execute(statement=statement)
        result_data: Sequence[Any] = result_value.scalars().all()
        db.session.commit()
        return result_data

    def read(
        self,
        model: ModelType,
        data_values: dict,
    ) -> Any | None:
        """Get model instance by given data_values."""
        statement = select(model)
        for key, elem in data_values.items():
            statement = statement.where(getattr(model, key) == elem)
        result_value: Result = db.session.execute(statement=statement)
        result_data: Any | None = result_value.scalar_one_or_none()
        if not result_data:
            abort_methods.raise_not_found_error(data_values, model.__name__)
        return result_data

    def update(
        self,
        model: ModelType,
        data_values: dict,
        filters: dict,
    ) -> Any:
        """Update model instance with given data."""
        where_expr = self._get_where_expressions(model, filters)
        update_statement = (
            update(model)
            .where(and_(*where_expr))
            .values(**data_values)
            .returning(model)
            .execution_options(synchronize_session="fetch")
        )
        statement = (
            select(model)
            .from_statement(statement=update_statement)
            .execution_options(populate_existing=True)
        )
        result_value: Result = db.session.execute(statement=statement)
        result_data: Any | None = result_value.scalar_one_or_none()
        if not result_data:
            abort_methods.raise_not_found_error(filters, model.__name__)
        db.session.commit()
        return result_data

    def delete(
        self,
        model: ModelType,
        data_values: dict,
    ) -> CursorResult:
        """Delete model instance."""
        statement = delete(model)
        for key, elem in data_values.items():
            statement = statement.where(getattr(model, key) == elem)
        result_value: CursorResult = db.session.execute(statement=statement)
        db.session.commit()
        return result_value

    def read_many(
        self,
        model: ModelType,
        filters: Optional[dict] = None,
        rev: bool = False,
    ) -> Sequence[Any]:
        """Get model instances list."""
        filters = filters if filters else {}
        select_statement: Select[Any] = select(model)
        if filters:
            select_statement = select_statement.filter_by(**filters)
        if rev:
            select_statement = select_statement.order_by(
                model.id.desc(),  # type: ignore
            )
        select_statement = select_statement.execution_options(populate_existing=True)
        result_value: Result = db.session.execute(statement=select_statement)
        return result_value.scalars().all()

    def _get_where_expressions(self, model: ModelType, filters: dict) -> list:
        """Create 'where' expressions for sql statement."""
        where_expr = []
        for key, elem in filters.items():
            where_expr.append(getattr(model, key) == elem)
        return where_expr


crud = CRUDOperations()


class DbUtils(object):
    """Db utilities."""

    def is_exists(
        self,
        model: ModelType,
        data_values: dict,
    ) -> bool:
        """Check instance existence."""
        statement = select(model.id)  # type: ignore
        for key, elem in data_values.items():
            statement = statement.where(getattr(model, key) == elem)
        result_value: Result = db.session.execute(statement=statement)
        return result_value.first() is not None

    def check_unique_constraits(
        self,
        model: ModelType,
        name: str,
        model_value: Any,
        instance_id: Optional[int],
    ) -> bool:
        """Check unique constraits for model field with given model_value."""
        statement = select(model.id).where(  # type: ignore
            getattr(model, name) == model_value,
        )
        if instance_id:
            statement = statement.where(model.id != instance_id)  # type: ignore
        result_value: Result = db.session.execute(statement=statement)
        return result_value.first() is not None


db_utils = DbUtils()
