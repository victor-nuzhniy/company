"""Validators for user base apps."""
import os
import re

from werkzeug.security import generate_password_hash


def username(username_str: str) -> str:
    """Validate username."""
    if len(username_str) > 50:
        raise ValueError(
            "{username} length shoud be lower.".format(username=username_str),
        )
    if not re.search(r"^[\w.@+-]+\Z", username_str):
        raise ValueError(
            "".join(
                (
                    "Enter a valid username. This value may contain",
                    " only English letters, ",
                    "numbers, and @/./+/-/_ characters.",
                ),
            ),
        )
    return username_str


def email(email_str: str) -> str:
    """Validate email."""
    if len(email_str) > 120:
        raise ValueError(
            "{email} length should be lower.".format(email=email_str),
        )
    specials = "!#$%&'*+-/=?^_`{|?."
    specials = re.escape(specials)
    regex = (
        "^(?!["
        + specials
        + "])(?!.*["
        + specials
        + "]{2})(?!.*["
        + specials
        + "]$)[A-Za-z0-9"
        + specials
        + "]+(?<!["
        + specials
        + "])@[A-Za-z0-9.-]+[.][A-Za-z]{2,4}$"
    )
    if not re.fullmatch(regex, email_str):
        raise ValueError(
            "Invalid email address format: {email}".format(email=email_str),
        )
    return email_str


def password(password_str: str) -> str:
    """Validate and encrypt password."""
    if len(password_str) < 2:  # TODO bigger int
        raise ValueError("Password length is too short.")
    return generate_password_hash(password_str)


def admin_password(admin_password_str: str) -> str:
    """Validate admin_header."""
    key = os.getenv("ADMIN_PASSWORD")
    if not key:
        raise ValueError("Forbidden.")
    if not admin_password_str:
        raise ValueError("Access field is empty.")
    if key == admin_password_str:
        return admin_password_str
    raise ValueError("Access denied. Value is invalid.")
