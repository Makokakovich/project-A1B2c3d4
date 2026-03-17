# src/handlers/contact_handlers.py
from src.models import AddressBook, Record
from src.utils.ui import (
    print_success, print_error, print_warning, print_info,
    print_contacts, print_contact_details,
    print_contact_added, print_contact_updated, print_contact_deleted,
    print_phone_added, print_phone_removed, print_birthday_added,
    console
)
import re


def add_contact(args, book):
    """Додає новий контакт або телефон до існуючого"""
    if len(args) < 2:
        print_warning("Введіть ім'я та телефон: add <ім'я> <телефон>")
        return

    name = args[0]
    phone = args[1]

    # Валідація телефону
    if not re.fullmatch(r"\d{10,12}", phone):
        print_error(
            f"Невірний формат телефону '{phone}'. Має бути 10-12 цифр.")
        return

    # Шукаємо контакт
    if name in book.data:
        # Контакт існує - додаємо телефон
        record = book.data[name]
        try:
            record.add_phone(phone)
            print_phone_added(name, phone)
        except ValueError as e:
            print_error(str(e))
    else:
        # Створюємо новий контакт
        try:
            record = Record(name)
            record.add_phone(phone)
            book.add_record(record)
            print_contact_added(name)
        except ValueError as e:
            print_error(str(e))


def show_all_contacts(args, book):
    """Показує всі контакти у вигляді таблиці"""
    if not book.data:
        print_info("📭 Немає контактів для відображення")
        return

    # ВИПРАВЛЕНО: виводимо через ui, а не повертаємо рядок
    print_contacts(book.data)


def find_contact(args, book):
    """Пошук контакту за ім'ям або частиною імені"""
    if not args:
        print_warning("Введіть ім'я для пошуку: find <ім'я> або phone <ім'я>")
        return

    query = args[0].lower()
    found = False

    for name, record in book.data.items():
        if query in name.lower():
            print_contact_details(record)
            found = True

    if not found:
        print_warning(f"Контактів за запитом '{args[0]}' не знайдено.")


def edit_contact(args, book):
    """Редагує телефон контакту"""
    if len(args) < 3:
        print_warning(
            "Введіть ім'я, старий та новий телефон: change <ім'я> <старий> <новий>")
        return

    name = args[0]
    old_phone = args[1]
    new_phone = args[2]

    # Валідація нового телефону
    if not re.fullmatch(r"\d{10,12}", new_phone):
        print_error(
            f"Невірний формат телефону '{new_phone}'. Має бути 10-12 цифр.")
        return

    if name not in book.data:
        print_error(f"Контакт '{name}' не знайдено.")
        return

    record = book.data[name]
    try:
        record.edit_phone(old_phone, new_phone)
        print_contact_updated(name)
    except ValueError as e:
        print_error(str(e))


def delete_contact(args, book):
    """Видаляє контакт"""
    if not args:
        print_warning("Введіть ім'я для видалення: delete <ім'я>")
        return

    name = args[0]

    if name not in book.data:
        print_error(f"Контакт '{name}' не знайдено.")
        return

    book.delete(name)
    print_contact_deleted(name)


def birthdays(args, book):
    """Показує найближчі дні народження"""
    if not args:
        days = 7
    else:
        try:
            days = int(args[0])
        except ValueError:
            print_error("Введіть кількість днів числом: birthdays <днів>")
            return

    try:
        results = book.get_birthdays_in_days(days)
    except AttributeError:
        results = book.get_upcoming_birthdays(days)

    if not results:
        print_info(f"📅 На найближчі {days} днів немає днів народження.")
        return

    # Виводимо у вигляді таблиці
    from rich.table import Table

    table = Table(title=f"🎂 Дні народження на найближчі {days} днів")
    table.add_column("Ім'я", style="green")
    table.add_column("Дата", style="yellow")
    table.add_column("Днів до", style="cyan", justify="right")

    for result in results:
        if hasattr(result, 'name') and hasattr(result, 'birthday'):
            name = result.name.value
            date = result.birthday.value
            days_left = result.days_to_birthday()
            table.add_row(name, date, str(days_left))
        elif isinstance(result, tuple) and len(result) >= 3:
            table.add_row(str(result[0]), str(result[1]), str(result[2]))
        else:
            table.add_row(str(result), "", "")

    console.print(table)
