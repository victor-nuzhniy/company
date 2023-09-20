"""Validators for product apps."""
from flask import abort


def str_length_200(name_str):
    """Validate discount_name."""
    if len(name_str) > 200:
        abort(422, f"{name_str} length should be lower than 200 character.")
    return name_str


def str_length_15(name_str):
    """Validate discount_name."""
    if len(name_str) > 15:
        abort(422, f"{name_str} length should be lower than 15 character.")
    return name_str
