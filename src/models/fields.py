from datetime import datetime
from src.utils.validators import validate_phone, validate_email

class Field:
    def __init__(self, value: str) -> None:
        self.value = value

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.value!r})"


class Name(Field):
    def __init__(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("Name is required and cannot be blank.")
        super().__init__(value.strip())


class Phone(Field):
    def __init__(self, value: str) -> None:
        if not validate_phone(value):
            raise ValueError("Invalid phone format. Must be 10-12 digits.")
        super().__init__(value)


class Email(Field):
    def __init__(self, value: str) -> None:
        if not validate_email(value):
            raise ValueError("Invalid email format.")
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value: str) -> None:
        try:
            # Парсимо рядок і зберігаємо як об'єкт date
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Birthday must be in DD.MM.YYYY format.")

    def __str__(self) -> str:
        return self.value.strftime("%d.%m.%Y")


class Address(Field):
    def __init__(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("Address cannot be empty.")
        super().__init__(value.strip())