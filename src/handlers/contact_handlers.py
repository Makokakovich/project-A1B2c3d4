"""
CLI handler functions for address book commands.

Each function receives the parsed args list and the AddressBook instance.
Each function returns a string to print to the user.

Convention: handler(args: list[str], book: AddressBook) -> str
"""

from src.models import AddressBook, Record


def add_contact(args: list[str], book: AddressBook) -> str:
    try:
        if len(args) < 2:
            return "Usage: add <name> <phone>"

        name, phone = args[0], args[1]
        record = book.find(name)

        if record:
            record.add_phone(phone)
            return f"Phone added to existing contact {name}."

        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
        return f"Contact {name} added."

    except KeyError:
        try:
            name, phone = args[0], args[1]
            record = Record(name)
            record.add_phone(phone)
            book.add_record(record)
            return f"Contact {name} added."
        except Exception as e:
            return f"Error adding contact: {e}"
    except Exception as e:
        return f"Error adding contact: {e}"


def show_all_contacts(args: list[str], book: AddressBook) -> str:
    try:
        return str(book)
    except Exception as e:
        return f"Error showing contacts: {e}"


def find_contact(args: list[str], book: AddressBook) -> str:
    try:
        if not args:
            return "Usage: find <query>"

        query = " ".join(args)
        results = book.search(query)

        if not results:
            return "No contacts found."

        return "\n".join(str(record) for record in results)

    except Exception as e:
        return f"Error finding contact: {e}"


def edit_contact(args: list[str], book: AddressBook) -> str:
    try:
        if len(args) < 3:
            return "Usage: edit <name> <old_phone> <new_phone>"

        name, old_phone, new_phone = args[0], args[1], args[2]
        record = book.find(name)
        record.edit_phone(old_phone, new_phone)

        return f"Phone for {name} updated."

    except Exception as e:
        return f"Error editing contact: {e}"


def delete_contact(args: list[str], book: AddressBook) -> str:
    try:
        if len(args) < 1:
            return "Usage: delete <name>"

        name = args[0]
        book.delete(name)

        return f"Contact {name} deleted."

    except Exception as e:
        return f"Error deleting contact: {e}"


def birthdays(args: list[str], book: AddressBook) -> str:
    try:
        if len(args) < 1:
            return "Usage: birthdays <days>"

        days = int(args[0])
        results = book.get_birthdays_in_days(days)

        if not results:
            return f"No birthdays in the next {days} days."

        return "\n".join(str(record) for record in results)

    except ValueError:
        return "Days must be a number."
    except Exception as e:
        return f"Error getting birthdays: {e}"
    