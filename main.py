import re
from collections import UserDict
from datetime import date, datetime


# --- базові класи для полів ---

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        if not value.strip():
            raise ValueError("Ім'я не може бути порожнім")
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        digits = re.sub(r'\D', '', value)
        if not (10 <= len(digits) <= 12):
            raise ValueError(f"Номер телефону не валідний: {value}")
        super().__init__(digits)


class Email(Field):
    def __init__(self, value):
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w{2,}$', value):
            raise ValueError(f"Email не валідний: {value}")
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Формат дати має бути ДД.ММ.РРРР")

    def __str__(self):
        return self.value.strftime("%d.%m.%Y")


# TODO: додати клас Address


# --- запис контакту ---

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.email = None
        self.birthday = None

    def add_phone(self, phone):
        p = Phone(phone)
        for existing in self.phones:
            if existing.value == p.value:
                raise ValueError("Такий номер вже існує")
        self.phones.append(p)

    def edit_phone(self, old_phone, new_phone):
        digits = re.sub(r'\D', '', old_phone)
        for i, ph in enumerate(self.phones):
            if ph.value == digits:
                self.phones[i] = Phone(new_phone)
                return
        raise ValueError(f"Номер {old_phone} не знайдено")

    def add_email(self, email):
        self.email = Email(email)

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def days_to_birthday(self):
        if not self.birthday:
            return None
        today = date.today()
        bday = self.birthday.value.replace(year=today.year)
        if bday < today:
            bday = bday.replace(year=today.year + 1)
        return (bday - today).days

    def __str__(self):
        phones_str = ', '.join(str(p) for p in self.phones)
        result = f"Ім'я: {self.name}"
        if phones_str:
            result += f", телефони: {phones_str}"
        if self.email:
            result += f", email: {self.email}"
        if self.birthday:
            result += f", день народження: {self.birthday}"
        return result


# --- адресна книга ---

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

    def get_upcoming_birthdays(self, days):
        result = []
        for record in self.data.values():
            n = record.days_to_birthday()
            if n is not None and 0 <= n <= days:
                result.append(record)
        return result


# TODO: класи Note і NotesBook (Vladyslav)
# TODO: збереження на диск (Olga)


# --- розбір введення ---

def parse_input(user_input):
    parts = user_input.strip().split()
    return parts[0].lower(), parts[1:]


# --- обробники контактів ---

def handle_add(args, book):
    if len(args) < 2:
        return "Введіть ім'я і телефон"
    name, phone = args[0], args[1]
    try:
        record = book.find(name)
    except KeyError:
        record = Record(name)
        book.add_record(record)
    try:
        record.add_phone(phone)
    except ValueError as e:
        return str(e)
    return "Контакт збережено."


def handle_change(args, book):
    if len(args) < 3:
        return "Введіть ім'я, старий і новий телефон"
    try:
        record = book.find(args[0])
        record.edit_phone(args[1], args[2])
        return "Контакт оновлено."
    except (KeyError, ValueError) as e:
        return str(e)


def handle_phone(args, book):
    if not args:
        return "Введіть ім'я контакту"
    try:
        record = book.find(args[0])
        if not record.phones:
            return "Телефонів немає"
        return ', '.join(str(p) for p in record.phones)
    except KeyError as e:
        return str(e)


def handle_all(book):
    if not book.data:
        return "Книга контактів порожня"
    return '\n'.join(str(r) for r in book.data.values())


def handle_add_birthday(args, book):
    if len(args) < 2:
        return "Введіть ім'я і дату (ДД.ММ.РРРР)"
    try:
        record = book.find(args[0])
        record.add_birthday(args[1])
        return "День народження додано."
    except (KeyError, ValueError) as e:
        return str(e)


def handle_birthdays(args, book):
    days = 7
    if args:
        try:
            days = int(args[0])
        except ValueError:
            return "Кількість днів має бути числом"
    upcoming = book.get_upcoming_birthdays(days)
    if not upcoming:
        return f"Найближчих днів народження немає (за {days} днів)"
    return '\n'.join(f"{r.name}: через {r.days_to_birthday()} дн." for r in upcoming)


def handle_find(args, book):
    if not args:
        return "Введіть запит для пошуку"
    results = book.search(args[0])
    if not results:
        return "Нічого не знайдено"
    return '\n'.join(str(r) for r in results)


def handle_delete(args, book):
    if not args:
        return "Введіть ім'я контакту"
    try:
        book.delete(args[0])
        return "Контакт видалено."
    except KeyError as e:
        return str(e)


# --- головний цикл ---

def main():
    book = AddressBook()
    # TODO: підключити load_data коли Olga зробить storage
    print("Вітаю! Персональний помічник запущено.")

    while True:
        user_input = input("Введіть команду: ").strip()
        if not user_input:
            continue

        command, args = parse_input(user_input)

        if command in ("exit", "close", "good bye"):
            # TODO: зберігати дані перед виходом
            print("До побачення!")
            break

        elif command == "hello":
            print("Чим можу допомогти?")

        elif command == "add":
            print(handle_add(args, book))

        elif command == "change":
            print(handle_change(args, book))

        elif command == "phone":
            print(handle_phone(args, book))

        elif command == "all":
            print(handle_all(book))

        elif command == "add-birthday":
            print(handle_add_birthday(args, book))

        elif command == "birthdays":
            print(handle_birthdays(args, book))

        elif command == "find":
            print(handle_find(args, book))

        elif command == "delete":
            print(handle_delete(args, book))

        else:
            print("Невідома команда.")


if __name__ == "__main__":
    main()
