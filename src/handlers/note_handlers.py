"""
CLI handler functions for notes commands.

Convention: handler(args: list[str], notes: NotesBook) -> str
"""

from src.models import NotesBook, Note


def add_note(args: list[str], notes: NotesBook) -> str:
    """
    Usage: add-note <title> <content...>
    args[0] = title, args[1:] joined = content
    """
    if len(args) < 2:
        return "Enter note title and content."

    title = args[0]
    content = " ".join(args[1:])

    try:
        note = Note(title, content)
        notes.add_note(note)
        return f"Note '{title}' added."
    except ValueError as e:
        return str(e)


def show_all_notes(args: list[str], notes: NotesBook) -> str:
    """Usage: notes — show all notes."""
    return str(notes)


def find_note(args: list[str], notes: NotesBook) -> str:
    """Usage: find-note <query>"""
    if not args:
        return "Enter query for note search."

    query = " ".join(args)
    results = notes.search(query)

    if not results:
        return "No notes found."

    return "\n".join(str(note) for note in results)


def edit_note(args: list[str], notes: NotesBook) -> str:
    """
    Usage: edit-note <title> <new_content...>
    Replace content of the note with given title.
    """
    if len(args) < 2:
        return "Enter note title and new content."

    title = args[0]
    new_content = " ".join(args[1:])

    try:
        note = notes.find(title)
        note.edit_content(new_content)
        return f"Note '{title}' updated."
    except (KeyError, ValueError) as e:
        return str(e)


def delete_note(args: list[str], notes: NotesBook) -> str:
    """Usage: delete-note <title>"""
    if not args:
        return "Enter note title."

    title = args[0]

    try:
        notes.delete(title)
        return f"Note '{title}' deleted."
    except KeyError as e:
        return str(e)


def find_by_tag(args: list[str], notes: NotesBook) -> str:
    """Usage: tag <tag> — find notes by tag."""
    if not args:
        return "Enter tag."

    tag = args[0]

    results = notes.find_by_tag(tag)

    if not results:
        return f"No notes found with tag '{tag}'."

    return "\n".join(str(note) for note in results)