"""
CLI handler functions for notes commands.

Convention:  handler(args: list[str], notes: NotesBook) -> str
"""

# TODO (Colleague 2): Implement all handler functions below.
# Return user-friendly strings. Never raise — catch exceptions and return error text.

from src.models import NotesBook, Note


def add_note(args: list[str], notes: NotesBook) -> str:
    """
    Usage: add-note <title> <content...>
    args[0] = title, args[1:] joined = content
    """
    # TODO: validate, create Note(title, content), notes.add_note(note)
    raise NotImplementedError


def show_all_notes(args: list[str], notes: NotesBook) -> str:
    """Usage: notes  — show all notes."""
    # TODO: return str(notes)
    raise NotImplementedError


def find_note(args: list[str], notes: NotesBook) -> str:
    """Usage: find-note <query>"""
    # TODO: notes.search(query)
    raise NotImplementedError


def edit_note(args: list[str], notes: NotesBook) -> str:
    """
    Usage: edit-note <title> <new_content...>
    Replace content of the note with given title.
    """
    # TODO: find note, call note.edit_content(new_content)
    raise NotImplementedError


def delete_note(args: list[str], notes: NotesBook) -> str:
    """Usage: delete-note <title>"""
    # TODO: notes.delete(title)
    raise NotImplementedError


def find_by_tag(args: list[str], notes: NotesBook) -> str:
    """Usage: tag <tag>  — find notes by tag."""
    # TODO: notes.find_by_tag(tag), format results
    raise NotImplementedError
