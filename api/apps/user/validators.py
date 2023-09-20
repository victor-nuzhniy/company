"""Validators for user apps."""
import os
import re

from flask import abort

from api.apps.auth.utils import encrypt_password


def username(username_str) -> str:
    """Validate username."""
    if len(username_str) > 50:
        abort(422, f"{username_str} length shoud be lower.")
    if not re.search(r"^[\w.@+-]+\Z", username_str):
        abort(
            422,
            "Enter a valid username. This value may contain"
            " only English letters, "
            "numbers, and @/./+/-/_ characters.",
        )
    return username_str


def email(email_str) -> str:
    """Validate email."""
    if len(email_str) > 120:
        abort(422, f"{email_str} length should be lower.")
    specials = "!#$%&'*+-/=?^_`{|?."
    specials = re.escape(specials)
    regex = (
        r"^(?!["
        + specials
        + "])(?!.*["
        + specials
        + "]{2})(?!.*["
        + specials
        + "]$)[A-Za-z0-9"
        + specials
        + "]+(?<!["
        + specials
        + "])@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}$"
    )
    if not re.fullmatch(regex, email_str):
        abort(422, f"Invalid email address format: {email_str}")
    return email_str


def password(password_str: str) -> str:
    """Validate and encrypt password."""
    if len(password_str) < 1:  # TODO bigger int
        abort(422, "Password length is too short.")
    return encrypt_password(password_str)


def admin_password(admin_password_str: str) -> str:
    """Validate admin_header."""
    key = os.getenv("ADMIN_PASSWORD")
    if not key:
        abort(403)
    if not admin_password_str:
        abort(422, "Access field is empty.")
    if key == admin_password_str:
        return admin_password_str
    abort(403, "Access denied. Value is invalid.")
