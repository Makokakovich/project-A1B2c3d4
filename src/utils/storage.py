"""
Persistent storage — save and load app data using pickle.

Files are stored in the user's home directory (~/.personal_assistant/).
"""

# TODO (Colleague 3): Implement save_data and load_data.

import pickle
from pathlib import Path

# Directory where data files will be stored
DATA_DIR = Path.home() / ".personal_assistant"
CONTACTS_FILE = DATA_DIR / "address_book.pkl"
NOTES_FILE = DATA_DIR / "notes_book.pkl"


def _ensure_dir() -> None:
    """Create the data directory if it does not exist."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def save_data(address_book, notes_book) -> None:
    """
    Serialise address_book and notes_book to disk with pickle.

    Args:
        address_book: AddressBook instance
        notes_book:   NotesBook instance
    """
    # TODO:
    # 1. _ensure_dir()
    # 2. open CONTACTS_FILE in "wb" mode, pickle.dump(address_book, f)
    # 3. open NOTES_FILE   in "wb" mode, pickle.dump(notes_book,   f)
    raise NotImplementedError


def load_data():
    """
    Load address_book and notes_book from disk.

    Returns:
        tuple(AddressBook, NotesBook)
        If files don't exist, return fresh empty instances.
    """
    # TODO:
    # Import AddressBook and NotesBook here (avoid circular imports at module level)
    # Try to open each file with "rb" and pickle.load()
    # On FileNotFoundError return AddressBook(), NotesBook()
    raise NotImplementedError
