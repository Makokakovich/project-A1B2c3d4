from datetime import datetime
from src.utils.validators import validate_phone, validate_email


class Field:
    def __init__(self, value: str) -> None:
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Name(Field):
    def __init__(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("Імʼя не може бути порожнім.")
        super().__init__(value.strip())


class Phone(Field):
    def __init__(self, value: str) -> None:
        if not validate_phone(value):
            raise ValueError("Невірний формат телефону. Має бути 10-12 цифр.")
        super().__init__(value)


class Email(Field):
    def __init__(self, value: str) -> None:
        if not validate_email(value):
            raise ValueError("Невірний формат email.")
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value: str) -> None:
        try:
            # парсимо рядок і зберігаємо як обʼєкт date
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Формат дати має бути ДД.ММ.РРРР.")

    def __str__(self) -> str:
        return self.value.strftime("%d.%m.%Y")


class Address(Field):
    def __init__(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("Адреса не може бути порожньою.")
        super().__init__(value.strip())
