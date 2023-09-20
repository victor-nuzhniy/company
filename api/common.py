"""Common utilities for api."""
from datetime import datetime

from pytz import utc
from sqlalchemy import TypeDecorator
from sqlalchemy.dialects.sqlite import DATETIME


class AwareDateTime(TypeDecorator):
    """Results returned as aware datetimes, not naive ones."""

    impl = DATETIME

    @property
    def python_type(
        self,
    ) -> type(datetime):
        """Get python type property."""
        return type(datetime)

    def process_bind_param(self, value: datetime, dialect) -> datetime:
        """Process bind param, in case tzinfo is absent - raise error."""
        if value is not None:
            if not value.tzinfo:
                raise TypeError("tzinfo is required")
            value = value.astimezone(utc).replace(tzinfo=None)
        return value

    def process_literal_param(self, value: datetime, dialect) -> datetime:
        """Implement process literal param."""
        pass

    def process_result_value(self, value: datetime, dialect) -> datetime:
        """Return value with tzinfo utc replacement."""
        return value.replace(tzinfo=utc)
