"""
Persistent storage — save and load app data using pickle.

Files are stored in the user's home directory (~/.personal_assistant/).
"""

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
        notes_book: NotesBook instance
    """
    _ensure_dir()

    with open(CONTACTS_FILE, "wb") as f:
        pickle.dump(address_book, f)

    with open(NOTES_FILE, "wb") as f:
        pickle.dump(notes_book, f)


def load_data():
    """
    Load address_book and notes_book from disk.

    Returns:
        tuple(AddressBook, NotesBook)
        If files don't exist, return fresh empty instances.
    """
    from src.models.address_book import AddressBook
    from src.models.notes_book import NotesBook

    try:
        with open(CONTACTS_FILE, "rb") as f:
            address_book = pickle.load(f)
    except FileNotFoundError:
        address_book = AddressBook()

    try:
        with open(NOTES_FILE, "rb") as f:
            notes_book = pickle.load(f)
    except FileNotFoundError:
        notes_book = NotesBook()

    return address_book, notes_book

