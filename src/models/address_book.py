from collections import UserDict
from .record import Record


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name not in self.data:
            raise KeyError(f"Контакт '{name}' не знайдено")
        return self.data[name]

    def delete(self, name):
        if name not in self.data:
            raise KeyError(f"Контакт '{name}' не знайдено")
        del self.data[name]

    def search(self, query):
        query = query.lower()
        found = []
        for record in self.data.values():
            if query in record.name.value.lower():
                found.append(record)
                continue
            for ph in record.phones:
                if query in ph.value:
                    found.append(record)
                    break
        return found

    # TODO: дописати get_birthdays_in_days

    def __str__(self):
        if not self.data:
            return "Книга контактів порожня"
        return "\n".join(str(r) for r in self.data.values())
