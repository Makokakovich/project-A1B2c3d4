from typing import Optional
from datetime import date
from .fields import Name, Phone, Email, Birthday, Address


class Record:
    def __init__(self, name: str) -> None:
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.email: Optional[Email] = None
        self.birthday: Optional[Birthday] = None
        self.address: Optional[Address] = None

    def add_phone(self, phone: str) -> None:
        if self.find_phone(phone):
            raise ValueError(f"Телефон {phone} вже існує.")
        self.phones.append(Phone(phone))

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return
        raise ValueError(f"Телефон {old_phone} не знайдено.")

    def remove_phone(self, phone: str) -> None:
        phone_obj = self.find_phone(phone)
        if not phone_obj:
            raise ValueError(f"Телефон {phone} не знайдено.")
        self.phones.remove(phone_obj)

    def find_phone(self, phone: str) -> Optional[Phone]:
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def add_email(self, email: str) -> None:
        self.email = Email(email)

    def add_birthday(self, birthday: str) -> None:
        self.birthday = Birthday(birthday)

    def add_address(self, address: str) -> None:
        self.address = Address(address)

    def days_to_birthday(self) -> Optional[int]:
        if not self.birthday:
            return None
        today = date.today()
        # self.birthday.value вже є обʼєктом date
        bday = self.birthday.value.replace(year=today.year)
        if bday < today:
            bday = self.birthday.value.replace(year=today.year + 1)
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
