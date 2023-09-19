"""Validators for user apps."""
import re

from werkzeug.security import generate_password_hash


def username(username_str) -> str:
    """Validate username."""
    if len(username_str) > 50:
        raise ValueError(f"{username_str} length shoud be lower.")
    if not re.search(r"^[\w.@+-]+\Z", username_str):
        raise ValueError(
            "Enter a valid username. This value may contain"
            " only English letters, "
            "numbers, and @/./+/-/_ characters."
        )
    return username_str


def email(email_str) -> str:
    """Validate email."""
    if len(email_str) > 120:
        raise ValueError(f"{email_str} length should be lower.")
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
        raise ValueError(f"Invalid email address format: {email_str}")
    return email_str


def password(password_str: str) -> str:
    """Validate and encrypt password."""
    if len(password_str) < 1:  # TODO bigger int
        raise ValueError("Password length is too short.")
    token = generate_password_hash(password_str, salt_length=20)
    return token
