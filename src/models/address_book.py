"""
адресна книга — словник усіх контактів.

ключ — рядок з іменем, значення — обʼєкт Record.
успадковує UserDict, тому веде себе як звичайний dict.
"""

from collections import UserDict
from .record import Record


class AddressBook(UserDict):
    """
    зберігає і керує контактами.

    по суті це просто обгортка над dict з методами для зручної роботи:
    додати, знайти, видалити, пошук, дні народження.
    """

    def add_record(self, record: Record) -> None:
        """додає Record до книги. ключ — record.name.value."""
        self.data[record.name.value] = record

    def find(self, name: str) -> Record:
        """повертає контакт по імені. якщо нема — KeyError."""
        if name not in self.data:
            raise KeyError(f"Контакт '{name}' не знайдено.")
        return self.data[name]

    def delete(self, name: str) -> None:
        """видаляє контакт по імені. якщо нема — KeyError."""
        if name not in self.data:
            raise KeyError(f"Контакт '{name}' не знайдено.")
        del self.data[name]

    def search(self, query: str) -> list[Record]:
        """шукає контакти де query є в імені, телефоні або email (без урахування регістру)."""
        query = query.lower()
        result = []
        for record in self.data.values():
            if query in record.name.value.lower():
                result.append(record)
                continue
            for phone in record.phones:
                if query in phone.value:
                    result.append(record)
                    break
            else:
                if record.email and query in str(record.email).lower():
                    result.append(record)
        return result

    def get_birthdays_in_days(self, days: int) -> list[Record]:
        """повертає контакти у яких день народження протягом наступних days днів."""
        result = []
        for record in self.data.values():
            n = record.days_to_birthday()
            if n is not None and 0 <= n <= days:
                result.append(record)
        return result

    def __str__(self) -> str:
        if not self.data:
            return "Книга контактів порожня."
        return "\n".join(str(record) for record in self.data.values())
