"""Db service functionality for api."""
from typing import Any, Dict, List, Optional, Sequence

from flask_restful import abort
from sqlalchemy import (
    ChunkedIteratorResult,
    CursorResult,
    and_,
    delete,
    insert,
    select,
    update,
)

from api import db


class CRUDOperations:
    """CRUD operations for api app."""

    @staticmethod
    def create(
        model: db.Model,
        data: Dict,
    ) -> db.Model:
        """Create model instance with given data."""
        insert_statement = insert(model).values(**data).returning(model)
        statement = (
            select(model)
            .from_statement(insert_statement)
            .execution_options(populate_existing=True)
        )
        result: ChunkedIteratorResult = db.session.execute(statement=statement)
        data: db.Model = result.scalar_one()
        db.session.commit()
        return data

    @staticmethod
    def create_many(
        model: db.Model,
        data: List[Dict],
    ) -> Optional[List[db.Model]]:
        """Create many model instances with given data."""
        insert_statement = insert(model).values(data).returning(model)
        statement = (
            select(model)
            .from_statement(insert_statement)
            .execution_options(populate_existing=True)
        )
        result: CursorResult = db.session.execute(statement=statement)
        data: Optional[db.Model] = result.scalars().all()
        db.session.commit()
        return data

    @staticmethod
    def read(
        model: db.Model,
        data: Dict,
    ) -> db.Model:
        """Get model instance by given data."""
        statement = select(model)
        for k, v in data.items():
            statement = statement.where(getattr(model, k) == v)
        result: CursorResult = db.session.execute(statement=statement)
        response: db.Model = result.first()
        if not response:
            abort(
                404,
                message=f"{model.__name__} with data "
                f"{[str(key) + ': ' + str(value) for key, value in data.items()]} "
                f"doesn't exist",
            )
        return response[0]

    @staticmethod
    def update(
        model: db.Model,
        values: Dict,
        filters: Dict,
    ) -> db.Model:
        """Update model instance with given data."""
        where_expr = []
        for k, v in filters.items():
            where_expr.append(getattr(model, k) == v)
        update_statement = (
            update(model)
            .where(and_(*where_expr))
            .values(**values)
            .returning(model)
            .execution_options(synchronize_session="fetch")
        )
        statement = (
            select(model)
            .from_statement(statement=update_statement)
            .execution_options(populate_existing=True)
        )
        result: CursorResult = db.session.execute(statement=statement)
        data: db.Model = result.scalar_one_or_none()
        db.session.commit()
        return data

    @staticmethod
    def delete(
        model: db.Model,
        data: Dict,
    ) -> db.Model:
        """Delete model instance."""
        statement = delete(model)
        for k, v in data.items():
            statement = statement.where(getattr(model, k) == v)
        result: CursorResult = db.session.execute(statement=statement)
        db.session.commit()
        return result

    @staticmethod
    def read_many(
        model: db.Model,
        filters: Dict = None,
    ) -> db.Model:
        """Get model instances list."""
        filters = filters if filters else dict()
        select_statement = select(model)
        if filters:
            select_statement = select_statement.filter_by(**filters)
        select_statement = select_statement.execution_options(populate_existing=True)
        result: CursorResult = db.session.execute(statement=select_statement)
        objects: Sequence = result.scalars().all()
        return objects


crud = CRUDOperations()


class DbUtils:
    """Db utilities."""

    @staticmethod
    def is_exists(
        model: db.Model,
        data: Dict,
    ) -> bool:
        """Check instance existence."""
        """Get model instance by given data."""
        statement = select(model.id)
        for k, v in data.items():
            statement = statement.where(getattr(model, k) == v)
        result: CursorResult = db.session.execute(statement=statement)
        return result.first() is not None

    @staticmethod
    def check_unique_constraits(
        model: db.Model, name: str, value: Any, instance_id: Optional[int]
    ) -> bool:
        """Check unique constraits for model field with given value."""
        statement = select(model.id).where(getattr(model, name) == value)
        if instance_id:
            statement = statement.where(model.id != instance_id)
        result: CursorResult = db.session.execute(statement=statement)
        return result.first() is not None


db_utils = DbUtils()
