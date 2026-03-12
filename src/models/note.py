"""
Note — a single text note, optionally with tags.
"""


class Note:
    """
    Represents a single note.

    Attributes:
        title (str): Short title / identifier.
        content (str): Main text body.
        tags (list[str]): List of tag strings (e.g. ["work", "urgent"]).
    """

    def __init__(self, title: str, content: str) -> None:
        if not title.strip():
            raise ValueError("Title cannot be empty.")
        if not content.strip():
            raise ValueError("Content cannot be empty.")

        self.title = title.strip()
        self.content = content.strip()
        self.tags: list[str] = []

    def add_tag(self, tag: str) -> None:
        """Add a tag. Ignore duplicates (case-insensitive)."""
        normalized_tag = tag.strip().lower()

        if not normalized_tag:
            raise ValueError("Tag cannot be empty.")

        if normalized_tag not in self.tags:
            self.tags.append(normalized_tag)

    def remove_tag(self, tag: str) -> None:
        """Remove a tag. Raises ValueError if not found."""
        normalized_tag = tag.strip().lower()

        if normalized_tag in self.tags:
            self.tags.remove(normalized_tag)
            return

        raise ValueError(f"Tag '{tag}' not found.")

    def edit_content(self, new_content: str) -> None:
        """Replace note content."""
        if not new_content.strip():
            raise ValueError("Content cannot be empty.")

        self.content = new_content.strip()

    def edit_title(self, new_title: str) -> None:
        """Replace note title."""
        if not new_title.strip():
            raise ValueError("Title cannot be empty.")

        self.title = new_title.strip()

    def matches_tag(self, tag: str) -> bool:
        """Return True if tag is in self.tags (case-insensitive)."""
        return tag.strip().lower() in self.tags

    def __str__(self) -> str:
        tags = ", ".join(self.tags) if self.tags else "—"
        return f"[{self.title}] {self.content}  | Tags: {tags}"