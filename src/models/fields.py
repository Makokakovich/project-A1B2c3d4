"""
Field classes for the Personal Assistant.

Each field wraps a single value and provides validation.
Inherit from Field for any new field type.
"""

# TODO (Colleague 1): Implement all classes below.
# Each class must raise ValueError with a clear message on invalid input.
# Use validate_phone() and validate_email() from src/utils/validators.py


class Field:
    """Base class for record fields."""

    def __init__(self, value: str) -> None:
        self.value = value

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.value!r})"


class Name(Field):
    """Contact name. Required, cannot be empty."""

    def __init__(self, value: str) -> None:
        # TODO: raise ValueError if value is blank
        super().__init__(value)


class Phone(Field):
    """Phone number. Must pass validate_phone() check."""

    def __init__(self, value: str) -> None:
        # TODO: import validate_phone and raise ValueError if invalid
        super().__init__(value)


class Email(Field):
    """Email address. Must pass validate_email() check."""

    def __init__(self, value: str) -> None:
        # TODO: import validate_email and raise ValueError if invalid
        super().__init__(value)


class Birthday(Field):
    """Birthday stored as datetime.date. Input format: DD.MM.YYYY"""

    def __init__(self, value: str) -> None:
        # TODO: parse value with strptime("%d.%m.%Y")
        # Store as self.value = date object (not string)
        # Raise ValueError with helpful message on bad format
        super().__init__(value)


class Address(Field):
    """Free-text address field. Cannot be empty."""

    def __init__(self, value: str) -> None:
        # TODO: raise ValueError if value is blank
        super().__init__(value)
