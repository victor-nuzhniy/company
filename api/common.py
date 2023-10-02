"""Common functionality for api."""
from flask_restful import fields


class CustomDateTimeFormat(fields.Raw):
    """Class for creation custom datetime format."""

    def format(self, value):
        """Return custom datetime format."""
        return value.strftime("%Y-%m-%dT%H:%M:%S")
