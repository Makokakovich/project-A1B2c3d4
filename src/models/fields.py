"""
класи-поля для атрибутів контакту.

кожен клас обгортає рядкове значення і перевіряє його під час створення.
використовуються всередині Record як типізовані атрибути.
"""

import re
from datetime import datetime
from src.utils.validators import validate_phone, validate_email


class Field:
    """базовий клас для всіх полів. просто зберігає value і вміє в рядок."""

    def __init__(self, value: str) -> None:
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Name(Field):
    """імʼя контакту. якщо передати порожній рядок — впаде ValueError."""

    def __init__(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("Імʼя не може бути порожнім.")
        super().__init__(value.strip())


class Phone(Field):
    """номер телефону, 10-12 цифр. всі не-цифрові символи обрізаємо при збереженні."""

    def __init__(self, value: str) -> None:
        if not validate_phone(value):
            raise ValueError("Невірний формат телефону. Має бути 10-12 цифр.")
        super().__init__(re.sub(r"\D", "", value))


class Email(Field):
    """email адреса. якщо формат кривий — кидає ValueError."""

    def __init__(self, value: str) -> None:
        if not validate_email(value):
            raise ValueError("Невірний формат email.")
        super().__init__(value)


class Birthday(Field):
    """
    дата народження, зберігається як обʼєкт date (не рядок).

    приймає рядок у форматі ДД.ММ.РРРР.
    будь-який інший формат — ValueError.
    """

    def __init__(self, value: str) -> None:
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Формат дати має бути ДД.ММ.РРРР.")

    def __str__(self) -> str:
        return self.value.strftime("%d.%m.%Y")


class Address(Field):
    """фізична адреса контакту. порожній рядок не приймає."""

    def __init__(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("Адреса не може бути порожньою.")
        super().__init__(value.strip())
