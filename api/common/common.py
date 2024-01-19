"""Common functionality for api."""
from datetime import datetime

from flask_restful import fields


class CustomDateTimeFormat(fields.Raw):
    """Class for creation custom datetime format."""

    def format(self, value_to_format: datetime) -> str:
        """Return custom datetime format."""
        return value_to_format.strftime("%Y-%m-%d %H:%M:%S")
