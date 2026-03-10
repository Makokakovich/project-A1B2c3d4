"""
AddressBook — collection of Record objects.

Inherits from UserDict so it behaves like a dict: {name_str: Record}.
"""

# TODO (Colleague 1): Implement all methods marked with TODO.

from collections import UserDict
from datetime import date
from .record import Record


class AddressBook(UserDict):
    """Stores and manages contacts."""

    def add_record(self, record: Record) -> None:
        """Add a Record. Key is record.name.value."""
        # TODO: self.data[record.name.value] = record
        raise NotImplementedError

    def find(self, name: str) -> Record:
        """Return Record by name. Raises KeyError if not found."""
        # TODO: return self.data[name]  (raise KeyError with message if missing)
        raise NotImplementedError

    def delete(self, name: str) -> None:
        """Delete Record by name. Raises KeyError if not found."""
        # TODO: del self.data[name]
        raise NotImplementedError

    def search(self, query: str) -> list[Record]:
        """Return all records where name, phone, or email contain query (case-insensitive)."""
        # TODO: iterate self.data.values(), check each field
        raise NotImplementedError

    def get_birthdays_in_days(self, days: int) -> list[Record]:
        """Return contacts whose birthday falls within the next `days` days."""
        # TODO: use record.days_to_birthday() and filter by 0 <= days_left <= days
        raise NotImplementedError

    def __str__(self) -> str:
        if not self.data:
            return "Address book is empty."
        return "\n".join(str(record) for record in self.data.values())
