import sys
if sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")

from src.models import AddressBook, Record
from src.models import NotesBook, Note
from src.handlers.contact_handlers import (
    add_contact, show_all_contacts, find_contact,
    edit_contact, delete_contact, birthdays,
)
from src.handlers.note_handlers import (
    add_note, show_all_notes, find_note,
    edit_note, delete_note, find_by_tag,
)
from src.utils.storage import save_data, load_data


def parse_input(user_input):
    parts = user_input.strip().split()
    if not parts:
        return "", []
    return parts[0].lower(), parts[1:]


def show_help():
    print("""
Доступні команди:

  Контакти:
    add <ім'я> <телефон>             — додати контакт
    change <ім'я> <старий> <новий>   — змінити телефон
    phone <ім'я>                     — показати телефони
    all                              — всі контакти
    find <запит>                     — пошук контакту
    delete <ім'я>                    — видалити контакт
    add-birthday <ім'я> <дд.мм.рррр> — додати дату народження
    birthdays <днів>                 — найближчі дні народження

  Нотатки:
    add-note <назва> <текст>         — додати нотатку
    notes                            — всі нотатки
    find-note <запит>                — пошук нотатки
    edit-note <назва> <новий текст>  — редагувати нотатку
    delete-note <назва>              — видалити нотатку
    tag <тег>                        — нотатки за тегом

  Інше:
    hello                            — привітання
    help                             — ця довідка
    exit / close                     — вийти і зберегти
""")


def main():
    book, notes = load_data()
    print("Вітаю! Персональний помічник запущено. Введіть help для списку команд.")

    while True:
        user_input = input(">> ").strip()
        if not user_input:
            continue

        command, args = parse_input(user_input)

        if command in ("exit", "close"):
            save_data(book, notes)
            print("Дані збережено. До побачення!")
            break

        elif command == "hello":
            print("Чим можу допомогти?")

        elif command == "help":
            show_help()

        # контакти
        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(edit_contact(args, book))

        elif command == "phone":
            print(find_contact(args, book))

        elif command == "all":
            print(show_all_contacts(args, book))

        elif command == "find":
            print(find_contact(args, book))

        elif command == "delete":
            print(delete_contact(args, book))

        elif command == "add-birthday":
            if len(args) < 2:
                print("Введіть ім'я і дату (дд.мм.рррр)")
            else:
                try:
                    record = book.find(args[0])
                    record.add_birthday(args[1])
                    print("День народження додано.")
                except (KeyError, ValueError) as e:
                    print(str(e))

        elif command == "birthdays":
            print(birthdays(args, book))

        # нотатки
        elif command == "add-note":
            print(add_note(args, notes))

        elif command == "notes":
            print(show_all_notes(args, notes))

        elif command == "find-note":
            print(find_note(args, notes))

        elif command == "edit-note":
            print(edit_note(args, notes))

        elif command == "delete-note":
            print(delete_note(args, notes))

        elif command == "tag":
            print(find_by_tag(args, notes))

        else:
            print(f"Невідома команда '{command}'. Введіть help.")


if __name__ == "__main__":
    main()
