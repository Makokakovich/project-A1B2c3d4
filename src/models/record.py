"""
Record — one contact entry in the address book.

Stores: name (required), phones (list), email, birthday, address.
"""

# TODO (Colleague 1): Implement all methods marked with TODO.

from typing import Optional
from .fields import Name, Phone, Email, Birthday, Address


class Record:
    """Represents a single contact."""

    def __init__(self, name: str) -> None:
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.email: Optional[Email] = None
        self.birthday: Optional[Birthday] = None
        self.address: Optional[Address] = None

    # --- phones ---

    def add_phone(self, phone: str) -> None:
        """Add a phone number. Raises ValueError if already exists or invalid."""
        # TODO: check for duplicates, then append Phone(phone)
        raise NotImplementedError

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        """Replace old_phone with new_phone. Raises ValueError if not found."""
        # TODO: find Phone by value, replace it
        raise NotImplementedError

    def remove_phone(self, phone: str) -> None:
        """Remove phone by value. Raises ValueError if not found."""
        # TODO: remove matching Phone object
        raise NotImplementedError

    def find_phone(self, phone: str) -> Optional[Phone]:
        """Return Phone object or None."""
        # TODO: return matching Phone or None
        raise NotImplementedError

    # --- other fields ---

    def add_email(self, email: str) -> None:
        """Set email. Raises ValueError if invalid."""
        # TODO: self.email = Email(email)
        raise NotImplementedError

    def add_birthday(self, birthday: str) -> None:
        """Set birthday. Raises ValueError if format is wrong (DD.MM.YYYY)."""
        # TODO: self.birthday = Birthday(birthday)
        raise NotImplementedError

    def add_address(self, address: str) -> None:
        """Set address."""
        # TODO: self.address = Address(address)
        raise NotImplementedError

    def days_to_birthday(self) -> Optional[int]:
        """Return number of days until next birthday, or None if not set."""
        # TODO: calculate using date.today()
        raise NotImplementedError

    def __str__(self) -> str:
        phones = ", ".join(str(p) for p in self.phones) or "—"
        email = str(self.email) if self.email else "—"
        birthday = str(self.birthday) if self.birthday else "—"
        address = str(self.address) if self.address else "—"
        return (
            f"Name: {self.name} | Phone(s): {phones} | "
            f"Email: {email} | Birthday: {birthday} | Address: {address}"
        )
