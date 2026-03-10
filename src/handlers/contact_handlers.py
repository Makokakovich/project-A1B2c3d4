"""
CLI handler functions for address book commands.

Each function receives the parsed args list and the AddressBook instance.
Each function returns a string to print to the user.

Convention:  handler(args: list[str], book: AddressBook) -> str
"""

# TODO (Colleague 3): Implement all handler functions below.
# Wrap logic in try/except and return user-friendly error strings — never raise.

from src.models import AddressBook, Record


def add_contact(args: list[str], book: AddressBook) -> str:
    """
    Usage: add <name> <phone>
    Add new contact or add phone to existing contact.
    """
    # TODO:
    # 1. Validate len(args) >= 2
    # 2. name, phone = args[0], args[1]
    # 3. Try book.find(name); if found, record.add_phone(phone)
    #    else create Record(name), record.add_phone(phone), book.add_record(record)
    # 4. Return success message
    raise NotImplementedError


def show_all_contacts(args: list[str], book: AddressBook) -> str:
    """Usage: all  — show all contacts."""
    # TODO: return str(book)
    raise NotImplementedError


def find_contact(args: list[str], book: AddressBook) -> str:
    """
    Usage: find <query>
    Search contacts by name / phone / email.
    """
    # TODO: book.search(query), format results
    raise NotImplementedError


def edit_contact(args: list[str], book: AddressBook) -> str:
    """
    Usage: edit <name> <old_phone> <new_phone>
    Replace a phone number for an existing contact.
    """
    # TODO: find record, call record.edit_phone(old, new)
    raise NotImplementedError


def delete_contact(args: list[str], book: AddressBook) -> str:
    """Usage: delete <name>"""
    # TODO: book.delete(name)
    raise NotImplementedError


def birthdays(args: list[str], book: AddressBook) -> str:
    """
    Usage: birthdays <days>
    Show contacts with birthdays in the next <days> days.
    """
    # TODO: parse int(args[0]), call book.get_birthdays_in_days(days)
    raise NotImplementedError
