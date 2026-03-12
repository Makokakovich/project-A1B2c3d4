"""
NotesBook — collection of Note objects.

Inherits from UserDict: {title_str: Note}.
"""

from collections import UserDict
from .note import Note


class NotesBook(UserDict):
    """Stores and manages notes."""

    def add_note(self, note: Note) -> None:
        """Add a Note. Key is note.title. Raises ValueError if title already exists."""
        if note.title in self.data:
            raise ValueError(f"Note with title '{note.title}' already exists.")

        self.data[note.title] = note

    def find(self, title: str) -> Note:
        """Return Note by title. Raises KeyError if not found."""
        if title not in self.data:
            raise KeyError(f"Note '{title}' not found.")

        return self.data[title]

    def delete(self, title: str) -> None:
        """Delete note by title. Raises KeyError if not found."""
        if title not in self.data:
            raise KeyError(f"Note '{title}' not found.")

        del self.data[title]

    def search(self, query: str) -> list[Note]:
        """Return notes whose title or content contain query (case-insensitive)."""
        normalized_query = query.strip().lower()
        results = []

        for note in self.data.values():
            if (
                normalized_query in note.title.lower()
                or normalized_query in note.content.lower()
            ):
                results.append(note)

        return results

    def find_by_tag(self, tag: str) -> list[Note]:
        """Return all notes that have the given tag."""
        return [note for note in self.data.values() if note.matches_tag(tag)]

    def sort_by_tag(self, tag: str) -> list[Note]:
        """Return notes sorted: tagged notes first, then the rest."""
        tagged = []
        untagged = []

        for note in self.data.values():
            if note.matches_tag(tag):
                tagged.append(note)
            else:
                untagged.append(note)

        return tagged + untagged

    def __str__(self) -> str:
        if not self.data:
            return "Notes book is empty."
        return "\n".join(str(note) for note in self.data.values())