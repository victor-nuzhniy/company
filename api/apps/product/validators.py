"""Validators for product apps."""
from flask import abort


def str_length_200(name_str):
    """Validate discount_name."""
    if len(name_str) > 200:
        abort(422, f"{name_str} length should be lower than 30 character.")
    return name_str
