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
            raise ValueError(f"Phone {phone} already exists.")
        self.phones.append(Phone(phone))

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        found = False
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                found = True
                break
        if not found:
            raise ValueError(f"Phone {old_phone} not found.")

    def remove_phone(self, phone: str) -> None:
        phone_obj = self.find_phone(phone)
        if not phone_obj:
            raise ValueError(f"Phone {phone} not found.")
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
        # self.birthday.value вже є об'єктом date завдяки реалізації у fields.py
        bday = self.birthday.value
        next_bday = bday.replace(year=today.year)
        
        if next_bday < today:
            next_bday = bday.replace(year=today.year + 1)
            
        return (next_bday - today).days

    def __str__(self) -> str:
        phones = ", ".join(str(p) for p in self.phones) or "—"
        email = str(self.email) if self.email else "—"
        birthday = str(self.birthday) if self.birthday else "—"
        address = str(self.address) if self.address else "—"
        return (
            f"Name: {self.name} | Phone(s): {phones} | "
            f"Email: {email} | Birthday: {birthday} | Address: {address}"
        )