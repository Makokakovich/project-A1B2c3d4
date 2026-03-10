"""
Validation helpers for phone and email fields.

Used by Field subclasses in src/models/fields.py.
"""

# TODO (Colleague 3): Implement both functions below using the `re` module.

import re


def validate_phone(phone: str) -> bool:
    """
    Return True if phone is valid, False otherwise.

    Rules:
    - 10 digits exactly (digits only, no spaces/dashes required but allowed)
    - Examples of VALID:   "0671234567", "067-123-45-67", "+380671234567"
    - Strip non-digit characters before checking length
    - Minimum 10 digits, maximum 12 digits (to support +380 prefix)
    """
    # TODO: strip non-digits, check length
    raise NotImplementedError


def validate_email(email: str) -> bool:
    """
    Return True if email looks valid, False otherwise.

    Use a simple regex: something@something.something
    Example pattern: r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    """
    # TODO: return bool(re.match(pattern, email))
    raise NotImplementedError
