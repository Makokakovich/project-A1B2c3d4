from src.utils.ui import (
    print_success, print_error, print_warning, print_info,
    print_contacts, print_notes, print_help,
    print_contact_details, print_note_details, print_birthdays,
    print_birthday_added, confirm_action, get_input, console
)
from src.utils.cli_analyzer import enable_cli_analyzer, prompt_with_completion
from src.utils.storage import save_data, load_data
from src.handlers.note_handlers import (
    add_note, show_all_notes, find_note,
    edit_note, delete_note, find_by_tag, add_tag, sort_notes,
)
from src.handlers.contact_handlers import (
    add_contact, show_all_contacts, find_contact,
    edit_contact, delete_contact, birthdays,
)
from src.models import NotesBook, Note
from src.models import AddressBook, Record
import difflib
import sys

from src.utils.ui import console


if sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")


def parse_input(user_input: str) -> tuple[str, list[str]]:
    """розбиває введений рядок на команду і список аргументів. при порожньому рядку — ('', [])."""
    parts = user_input.strip().split()
    if not parts:
        return "", []
    return parts[0].lower(), parts[1:]


def show_help():
    """текстова довідка на випадок якщо rich не працює. зазвичай викликається print_help() з ui."""
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
    add-tag <назва> <тег>            — додати тег до нотатки
    tag <тег>                        — нотатки за тегом
    sort-notes <тег>                 — сортування нотаток за тегом

  Інше:
    hello                            — привітання
    help                             — ця довідка
    exit / close                     — вийти і зберегти
""")


def main():
    """точка входу. завантажує дані, запускає командний цикл, зберігає при виході."""
    book, notes = load_data()
    # Вирівняний прямокутник
    console.print(
        "[bold cyan]╔════════════════════════════════════════╗[/bold cyan]")
    console.print(
        "[bold cyan]║  🌟 ВІТАЮ! ПЕРСОНАЛЬНИЙ ПОМІЧНИК       ║[/bold cyan]")
    console.print(
        "[bold cyan]║  ✅ Запущено успішно!                  ║[/bold cyan]")
    console.print(
        "[bold cyan]║  📋 Введіть [bold underline green]help[/bold underline green] для списку команд     ║[/bold cyan]")
    console.print(
        "[bold cyan]╚════════════════════════════════════════╝[/bold cyan]")

    enable_cli_analyzer()

    console.print(
        "\n[bold cyan]✨ Для автодоповнення натискай [bold yellow]TAB[/bold yellow] ✨[/bold cyan]")

    while True:
        user_input = prompt_with_completion(">> ").strip()
        if not user_input:
            continue

        command, args = parse_input(user_input)

        if command in ("exit", "close"):
            save_data(book, notes)
            # ВИПРАВЛЕНО: кольоровий вихід
            print_success("Дані збережено. До побачення!")
            break

        elif command == "hello":
            # ВИПРАВЛЕНО: кольорове привітання
            print_info("Чим можу допомогти?")

        elif command == "help":
            # ВИПРАВЛЕНО: використовуємо гарну довідку з ui
            print_help()  # замість show_help()

        # контакти
        elif command == "add":
            # ЗМІНА: викликаємо функцію, вона сама виведе результат
            add_contact(args, book)

        elif command == "change":
            edit_contact(args, book)

        elif command == "phone":
            find_contact(args, book)

        elif command == "all":
            show_all_contacts(args, book)

        elif command == "find":
            find_contact(args, book)

        elif command == "delete":
            delete_contact(args, book)

        elif command == "add-birthday":
            if len(args) < 2:
                print_warning("Введіть ім'я і дату (дд.мм.рррр)")
            else:
                try:
                    record = book.find(args[0])
                    record.add_birthday(args[1])
                    # ВИПРАВЛЕНО: кольорове повідомлення
                    print_birthday_added(args[0])
                except (KeyError, ValueError) as e:
                    print_error(str(e))

        elif command == "birthdays":
            birthdays(args, book)  # birthdays вже виводить сама

        # нотатки - аналогічно
        elif command == "add-note":
            add_note(args, notes)

        elif command == "notes":
            show_all_notes(args, notes)

        elif command == "find-note":
            find_note(args, notes)

        elif command == "edit-note":
            edit_note(args, notes)

        elif command == "delete-note":
            delete_note(args, notes)

        elif command == "tag":
            find_by_tag(args, notes)

        elif command == "add-tag":
            add_tag(args, notes)

        elif command == "sort-notes":
            sort_notes(args, notes)

        else:
            all_commands = [
                "add", "change", "phone", "all", "find", "delete",
                "add-birthday", "birthdays", "add-note", "notes",
                "find-note", "edit-note", "delete-note", "add-tag",
                "tag", "sort-notes", "hello", "help", "exit", "close",
            ]
            closest = difflib.get_close_matches(
                command, all_commands, n=1, cutoff=0.5)
            if closest:
                # ВИПРАВЛЕНО: жовте попередження
                print_warning(
                    f"Невідома команда '{command}'. Можливо, ви мали на увазі: {closest[0]}?")
            else:
                # ВИПРАВЛЕНО: червона помилка
                print_error(f"Невідома команда '{command}'. Введіть help.")


if __name__ == "__main__":
    main()
