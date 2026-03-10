"""
NotesBook — collection of Note objects.

Inherits from UserDict: {title_str: Note}.
"""

# TODO (Colleague 2): Implement all methods marked with TODO.

from collections import UserDict
from .note import Note


class NotesBook(UserDict):
    """Stores and manages notes."""

    def add_note(self, note: Note) -> None:
        """Add a Note. Key is note.title. Raises ValueError if title already exists."""
        # TODO: check duplicate, then self.data[note.title] = note
        raise NotImplementedError

    def find(self, title: str) -> Note:
        """Return Note by title. Raises KeyError if not found."""
        # TODO: return self.data[title]
        raise NotImplementedError

    def delete(self, title: str) -> None:
        """Delete note by title. Raises KeyError if not found."""
        # TODO: del self.data[title]
        raise NotImplementedError

    def search(self, query: str) -> list[Note]:
        """Return notes whose title or content contain query (case-insensitive)."""
        # TODO: iterate values, check title and content
        raise NotImplementedError

    def find_by_tag(self, tag: str) -> list[Note]:
        """Return all notes that have the given tag."""
        # TODO: use note.matches_tag(tag)
        raise NotImplementedError

    def sort_by_tag(self, tag: str) -> list[Note]:
        """Return notes sorted: tagged notes first, then the rest."""
        # TODO: partition into tagged / untagged, return tagged + untagged
        raise NotImplementedError

    def __str__(self) -> str:
        if not self.data:
            return "Notes book is empty."
        return "\n".join(str(note) for note in self.data.values())
