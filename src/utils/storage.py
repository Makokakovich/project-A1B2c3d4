"""
збереження і завантаження даних через pickle.

файли лежать у ~/.personal_assistant/ — там де користувач точно має права.
при першому запуску директорія створюється автоматично.
"""

import pickle
from pathlib import Path

DATA_DIR = Path.home() / ".personal_assistant"
CONTACTS_FILE = DATA_DIR / "address_book.pkl"
NOTES_FILE = DATA_DIR / "notes_book.pkl"


def _ensure_dir() -> None:
    """створює директорію для даних якщо ще не існує."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def save_data(address_book, notes_book) -> None:
    """серіалізує адресну книгу і нотатки на диск."""
    _ensure_dir()
    with open(CONTACTS_FILE, "wb") as f:
        pickle.dump(address_book, f)
    with open(NOTES_FILE, "wb") as f:
        pickle.dump(notes_book, f)


def load_data():
    """
    завантажує і повертає (AddressBook, NotesBook) з диску.

    якщо файлів ще нема — повертає порожні екземпляри.
    імпорт всередині функції щоб не було циклічних залежностей.
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
