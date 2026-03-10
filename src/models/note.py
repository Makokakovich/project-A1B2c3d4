"""
Note — a single text note, optionally with tags.
"""

# TODO (Colleague 2): Implement the Note class below.


class Note:
    """
    Represents a single note.

    Attributes:
        title (str): Short title / identifier.
        content (str): Main text body.
        tags (list[str]): List of tag strings (e.g. ["work", "urgent"]).
    """

    def __init__(self, title: str, content: str) -> None:
        # TODO: validate that title and content are not empty (raise ValueError)
        self.title = title
        self.content = content
        self.tags: list[str] = []

    def add_tag(self, tag: str) -> None:
        """Add a tag. Ignore duplicates (case-insensitive)."""
        # TODO: normalise to lowercase, check duplicate, then append
        raise NotImplementedError

    def remove_tag(self, tag: str) -> None:
        """Remove a tag. Raises ValueError if not found."""
        # TODO: remove tag (case-insensitive match)
        raise NotImplementedError

    def edit_content(self, new_content: str) -> None:
        """Replace note content."""
        # TODO: validate not empty, then self.content = new_content
        raise NotImplementedError

    def edit_title(self, new_title: str) -> None:
        """Replace note title."""
        # TODO: validate not empty, then self.title = new_title
        raise NotImplementedError

    def matches_tag(self, tag: str) -> bool:
        """Return True if tag is in self.tags (case-insensitive)."""
        # TODO: return tag.lower() in self.tags
        raise NotImplementedError

    def __str__(self) -> str:
        tags = ", ".join(self.tags) if self.tags else "—"
        return f"[{self.title}] {self.content}  | Tags: {tags}"
