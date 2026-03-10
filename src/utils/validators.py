"""
Validation helpers for phone and email fields.

Used by Field subclasses in src/models/fields.py.
"""

import re


def validate_phone(phone: str) -> bool:
    """
    Return True if phone is valid, False otherwise.

    Rules:
    - Accept digits exactly (digits only, no spaces/dashes required but allowed)
    - Examples of VALID: "0671234567", "067-123-45-67", "+380671234567"
    - Strip non-digit characters before checking length
    - Minimum 10 digits, maximum 12 digits (to support +380 prefix)
    """
    digits = re.sub(r"\D", "", phone)
    return 10 <= len(digits) <= 12


def validate_email(email: str) -> bool:
    """
    Return True if email looks valid, False otherwise.

    Use a simple regex: something@something.something
    Example pattern: r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    """
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    return bool(re.match(pattern, email))

