import pickle
from pathlib import Path

# папка для збереження даних у домашній директорії користувача
DATA_DIR = Path.home() / ".personal_assistant"
CONTACTS_FILE = DATA_DIR / "address_book.pkl"
NOTES_FILE = DATA_DIR / "notes_book.pkl"


def _ensure_dir():
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def save_data(address_book, notes_book):
    _ensure_dir()
    with open(CONTACTS_FILE, "wb") as f:
        pickle.dump(address_book, f)
    with open(NOTES_FILE, "wb") as f:
        pickle.dump(notes_book, f)


def load_data():
    # імпорт тут щоб уникнути циклічних залежностей
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
