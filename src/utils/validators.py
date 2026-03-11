import re


def validate_phone(phone: str) -> bool:
    # прибираємо всі не-цифри і перевіряємо довжину
    digits = re.sub(r"\D", "", phone)
    return 10 <= len(digits) <= 12


def validate_email(email: str) -> bool:
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    return bool(re.match(pattern, email))
