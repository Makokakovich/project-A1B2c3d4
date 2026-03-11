from src.models import AddressBook, Record


def add_contact(args, book):
    if len(args) < 2:
        return "Введіть імʼя і телефон"
    name, phone = args[0], args[1]
    try:
        record = book.find(name)
        record.add_phone(phone)
        return f"Телефон додано до контакту {name}."
    except KeyError:
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
        return f"Контакт {name} додано."
    except ValueError as e:
        return str(e)


def show_all_contacts(args, book):
    return str(book)


def find_contact(args, book):
    if not args:
        return "Введіть запит для пошуку"
    results = book.search(" ".join(args))
    if not results:
        return "Контактів не знайдено."
    return "\n".join(str(r) for r in results)


def edit_contact(args, book):
    if len(args) < 3:
        return "Введіть імʼя, старий і новий телефон"
    try:
        record = book.find(args[0])
        record.edit_phone(args[1], args[2])
        return f"Телефон контакту {args[0]} оновлено."
    except (KeyError, ValueError) as e:
        return str(e)


def delete_contact(args, book):
    if not args:
        return "Введіть імʼя контакту"
    try:
        book.delete(args[0])
        return f"Контакт {args[0]} видалено."
    except KeyError as e:
        return str(e)


def birthdays(args, book):
    if not args:
        return "Введіть кількість днів"
    try:
        days = int(args[0])
    except ValueError:
        return "Кількість днів має бути числом"
    results = book.get_birthdays_in_days(days)
    if not results:
        return f"Найближчих днів народження немає (за {days} днів)."
    return "\n".join(str(r) for r in results)
