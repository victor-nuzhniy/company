"""Validators for counterparty apps."""


def discount_name(name_str):
    """Validate discount_name."""
    if len(name_str) > 30:
        raise ValueError(f"{name_str} length should be lower than 30 character.")
    return name_str
