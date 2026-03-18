"""
один запис контакту в адресній книзі.

містить імʼя (обовʼязково) і купу опціональних полів:
телефони, email, день народження, адреса.
"""

from typing import Optional
from datetime import date
from .fields import Name, Phone, Email, Birthday, Address


class Record:
    """
    один контакт з усіма його даними.

    атрибути:
        name — обовʼязкове імʼя
        phones — список телефонів (може бути кілька)
        email — пошта, якщо є
        birthday — дата народження, якщо є
        address — адреса, якщо є
    """

    def __init__(self, name: str) -> None:
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.email: Optional[Email] = None
        self.birthday: Optional[Birthday] = None
        self.address: Optional[Address] = None

    def add_phone(self, phone: str) -> None:
        """додає телефон. якщо такий вже є — ValueError."""
        if self.find_phone(phone):
            raise ValueError(f"Телефон {phone} вже існує.")
        self.phones.append(Phone(phone))

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        """замінює старий телефон на новий. якщо старого нема — ValueError."""
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return
        raise ValueError(f"Телефон {old_phone} не знайдено.")

    def remove_phone(self, phone: str) -> None:
        """видаляє телефон. якщо не знайдено — ValueError."""
        phone_obj = self.find_phone(phone)
        if not phone_obj:
            raise ValueError(f"Телефон {phone} не знайдено.")
        self.phones.remove(phone_obj)

    def find_phone(self, phone: str) -> Optional[Phone]:
        """повертає обʼєкт Phone якщо знайшов, або None."""
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def add_email(self, email: str) -> None:
        """встановлює email контакту."""
        self.email = Email(email)

    def add_birthday(self, birthday: str) -> None:
        """встановлює день народження (формат ДД.ММ.РРРР)."""
        self.birthday = Birthday(birthday)

    def add_address(self, address: str) -> None:
        """встановлює адресу контакту."""
        self.address = Address(address)

    def days_to_birthday(self) -> Optional[int]:
        """
        скільки днів до наступного дня народження.

        повертає None якщо дата не задана.
        29 лютого у невисокосному році замінюємо на 1 березня — інакше впаде.
        """
        if not self.birthday:
            return None
        today = date.today()
        try:
            bday = self.birthday.value.replace(year=today.year)
        except ValueError:
            bday = date(today.year, 3, 1)
        if bday < today:
            try:
                bday = self.birthday.value.replace(year=today.year + 1)
            except ValueError:
                bday = date(today.year + 1, 3, 1)
        return (bday - today).days

    def __str__(self) -> str:
        phones = ", ".join(str(p) for p in self.phones) or "—"
        email = str(self.email) if self.email else "—"
        birthday = str(self.birthday) if self.birthday else "—"
        address = str(self.address) if self.address else "—"
        return (
            f"Імʼя: {self.name} | Телефони: {phones} | "
            f"Email: {email} | День народження: {birthday} | Адреса: {address}"
        )
