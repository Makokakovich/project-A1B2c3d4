"""
валідація телефону і email перед збереженням.
"""

import re


def validate_phone(phone: str) -> bool:
    """
    перевіряє чи нормальний номер телефону.

    допускає + на початку, пробіли, дефіси, дужки — все це обрізається.
    головне щоб цифр було від 10 до 12.
    """
    if not re.match(r'^\+?[\d\s\-\(\)]+$', phone):
        return False
    digits = re.sub(r"\D", "", phone)
    return 10 <= len(digits) <= 12


def validate_email(email: str) -> bool:
    """перевіряє email за простим патерном user@domain.tld."""
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    return bool(re.match(pattern, email))
