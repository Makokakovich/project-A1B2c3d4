"""
CLI handler functions for notes commands.
"""

from src.models import NotesBook, Note
from src.utils.ui import (
    print_success, print_error, print_warning, print_info,
    print_notes, print_note_details,
    print_note_added, print_note_updated, print_note_deleted,
    print_tag_added, console
)


def add_note(args: list[str], notes: NotesBook) -> None:
    """
    Usage: add-note <title> <content...>
    """
    if len(args) < 2:
        print_warning(
            "Введіть назву і текст нотатки: add-note <назва> <текст>")
        return

    title = args[0]
    content = " ".join(args[1:])

    try:
        note = Note(title, content)
        notes.add_note(note)
        print_note_added(title)
    except ValueError as e:
        print_error(str(e))


def show_all_notes(args: list[str], notes: NotesBook) -> None:
    """Usage: notes — show all notes."""
    if not notes.data:
        print_info("📭 Немає нотаток для відображення")
        return

    print_notes(notes.data)


def find_note(args: list[str], notes: NotesBook) -> None:
    """Usage: find-note <query>"""
    if not args:
        print_warning("Введіть запит для пошуку: find-note <текст>")
        return

    query = " ".join(args).lower()
    results = {}

    for title, note in notes.data.items():
        if query in note.content.lower() or query in title.lower():
            results[title] = note

    if not results:
        print_warning(f"Нотаток за запитом '{' '.join(args)}' не знайдено.")
        return

    print_notes(results, title=f"Результати пошуку: '{' '.join(args)}'")


def edit_note(args: list[str], notes: NotesBook) -> None:
    """
    Usage: edit-note <title> <new_content...>
    """
    if len(args) < 2:
        print_warning(
            "Введіть назву нотатки і новий текст: edit-note <назва> <новий текст>")
        return

    title = args[0]
    new_content = " ".join(args[1:])

    try:
        note = notes.find(title)
        note.edit_content(new_content)
        print_note_updated(title)
    except (KeyError, ValueError) as e:
        print_error(str(e))


def delete_note(args: list[str], notes: NotesBook) -> None:
    """Usage: delete-note <title>"""
    if not args:
        print_warning("Введіть назву нотатки: delete-note <назва>")
        return

    title = args[0]

    try:
        notes.delete(title)
        print_note_deleted(title)
    except KeyError as e:
        print_error(f"Нотатку '{title}' не знайдено.")


def find_by_tag(args: list[str], notes: NotesBook) -> None:
    """Usage: tag <tag> — find notes by tag."""
    if not args:
        print_warning("Введіть тег: tag <тег>")
        return

    tag = args[0].lower()
    results = {}

    for title, note in notes.data.items():
        if note.matches_tag(tag):
            results[title] = note

    if not results:
        print_warning(f"Нотаток з тегом '{args[0]}' не знайдено.")
        return

    print_notes(results, title=f"Нотатки з тегом '{args[0]}'")


def add_tag(args: list[str], notes: NotesBook) -> None:
    """Usage: add-tag <title> <tag>"""
    if len(args) < 2:
        print_warning("Введіть назву нотатки і тег: add-tag <назва> <тег>")
        return

    title = args[0]
    tag = args[1]

    try:
        note = notes.find(title)
        note.add_tag(tag)
        print_tag_added(title, tag)
    except (KeyError, ValueError) as e:
        print_error(str(e))


def sort_notes(args: list[str], notes: NotesBook) -> None:
    """Usage: sort-notes <tag>"""
    if not args:
        print_warning("Введіть тег для сортування: sort-notes <тег>")
        return

    tag = args[0].lower()

    # Використовуємо вбудований метод sort_by_tag
    sorted_notes_list = notes.sort_by_tag(tag)

    if not sorted_notes_list:
        print_warning("Немає нотаток для відображення.")
        return

    # Перетворюємо список назад у словник для print_notes
    sorted_dict = {}
    for note in sorted_notes_list:
        sorted_dict[note.title] = note

    print_notes(sorted_dict, title=f"Нотатки (спочатку з тегом '{args[0]}')")
