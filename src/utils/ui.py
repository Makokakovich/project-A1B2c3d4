# src/utils/ui.py
"""
Модуль для гарного виводу інформації в консоль.
Використовує бібліотеку rich для кольорів та форматування.
"""

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.columns import Columns
from rich import print as rprint
from rich.text import Text
from rich.prompt import Prompt, Confirm
from datetime import datetime

# Створюємо глобальний консольний об'єкт
console = Console()


def print_success(message):
    """Зелене повідомлення про успіх"""
    console.print(f"✅ {message}", style="bold green")


def print_error(message):
    """Червоне повідомлення про помилку"""
    console.print(f"❌ {message}", style="bold red")


def print_warning(message):
    """Жовте попередження"""
    console.print(f"⚠️ {message}", style="bold yellow")


def print_info(message):
    """Синє інформаційне повідомлення"""
    console.print(f"ℹ️ {message}", style="bold blue")


def print_contacts(contacts, title="Контакти"):
    """Вивід контактів у вигляді таблиці"""
    if not contacts:
        print_warning("Немає контактів для відображення")
        return

    table = Table(title=title, title_style="bold cyan", border_style="blue")
    table.add_column("№", style="dim", width=4)
    table.add_column("Ім'я", style="green")
    table.add_column("Телефони", style="yellow")
    table.add_column("День народження", style="magenta")

    for i, (name, record) in enumerate(contacts.items(), 1):
        phones = ", ".join(
            p.value for p in record.phones) if record.phones else "—"

        # ВАЖЛИВО: безпечне отримання значення дня народження
        try:
            if record.birthday:
                # Якщо це об'єкт з атрибутом value
                if hasattr(record.birthday, 'value'):
                    birthday = str(record.birthday.value)
                else:
                    birthday = str(record.birthday)
            else:
                birthday = "—"
        except:
            birthday = "—"

        # Додаємо рядок тільки з рядковими значеннями
        table.add_row(str(i), str(name), str(phones), str(birthday))

    console.print(table)


def print_notes(notes, title="Нотатки"):
    """Вивід нотаток у вигляді карток"""
    if not notes:
        print_warning("Немає нотаток для відображення")
        return

    console.print(Panel(f"[bold cyan]{title}[/bold cyan]", expand=False))

    for i, (title_note, note) in enumerate(notes.items(), 1):
        # Форматуємо теги
        tags_text = f"[yellow]{', '.join(note.tags)}[/yellow]" if note.tags else "[dim]немає тегів[/dim]"

        # Створюємо панель для кожної нотатки
        note_panel = Panel(
            f"[bold green]{note.content}[/bold green]\n\n"
            f"[blue]Теги:[/blue] {tags_text}",
            title=f"[bold]{i}. {title_note}[/bold]",
            border_style="cyan",
            padding=(1, 2)
        )
        console.print(note_panel)


def print_contact_details(contact):
    """Детальний вивід одного контакту"""
    if not contact:
        print_error("Контакт не знайдено")
        return

    # Збираємо інформацію
    phones = "\n".join(
        f"  📞 {p.value}" for p in contact.phones) if contact.phones else "  📭 Немає телефонів"
    birthday = f"  🎂 {contact.birthday.value}" if contact.birthday else "  🎂 Не вказано"

    # Виводимо в гарній рамці
    content = f"[bold green]{phones}[/bold green]\n\n{birthday}"
    console.print(Panel(
        content,
        title=f"[bold cyan]👤 {contact.name.value}[/bold cyan]",
        border_style="green",
        padding=(1, 2)
    ))


def print_note_details(note):
    """Детальний вивід однієї нотатки"""
    if not note:
        print_error("Нотатку не знайдено")
        return

    tags = f"[yellow]{', '.join(note.tags)}[/yellow]" if note.tags else "[dim]немає тегів[/dim]"

    console.print(Panel(
        f"[white]{note.text}[/white]\n\n"
        f"[blue]Теги:[/blue] {tags}",
        title=f"[bold cyan]📝 {note.title}[/bold cyan]",
        border_style="yellow",
        padding=(1, 2)
    ))


def print_birthdays(birthdays_list):
    """Вивід списку днів народження"""
    if not birthdays_list:
        print_info("Найближчих днів народження немає")
        return

    table = Table(title="🎂 Найближчі дні народження",
                  title_style="bold magenta")
    table.add_column("Ім'я", style="green")
    table.add_column("Дата", style="yellow")
    table.add_column("Днів до", style="cyan", justify="right")

    for name, date, days in birthdays_list:
        table.add_row(name, date, str(days))

    console.print(table)


def print_help():
    """Гарний вивід допомоги"""
    console.print(Panel.fit(
        "[bold cyan]📚 ДОВІДКА З КОМАНД[/bold cyan]",
        border_style="cyan"
    ))

    # Контакти
    contacts_table = Table(title="📇 Контакти", border_style="green", box=None)
    contacts_table.add_column("Команда", style="yellow", width=25)
    contacts_table.add_column("Опис", style="white")
    contacts_table.add_row("add <ім'я> <телефон>", "Додати новий контакт")
    contacts_table.add_row("change <ім'я> <старий> <новий>", "Змінити телефон")
    contacts_table.add_row("phone <ім'я>", "Показати телефони контакту")
    contacts_table.add_row("all", "Показати всі контакти")
    contacts_table.add_row("find <запит>", "Пошук контактів")
    contacts_table.add_row("delete <ім'я>", "Видалити контакт")
    contacts_table.add_row(
        "add-birthday <ім'я> <дд.мм.рррр>", "Додати день народження")
    contacts_table.add_row(
        "birthdays <днів>", "Показати найближчі дні народження")
    console.print(contacts_table)

    # Нотатки
    notes_table = Table(title="📝 Нотатки", border_style="yellow", box=None)
    notes_table.add_column("Команда", style="cyan", width=25)
    notes_table.add_column("Опис", style="white")
    notes_table.add_row("add-note <назва> <текст>", "Додати нотатку")
    notes_table.add_row("notes", "Показати всі нотатки")
    notes_table.add_row("find-note <запит>", "Пошук нотаток")
    notes_table.add_row("edit-note <назва> <новий текст>",
                        "Редагувати нотатку")
    notes_table.add_row("delete-note <назва>", "Видалити нотатку")
    notes_table.add_row("add-tag <назва> <тег>", "Додати тег до нотатки")
    notes_table.add_row("tag <тег>", "Показати нотатки з тегом")
    notes_table.add_row("sort-notes <тег>", "Сортувати нотатки за тегом")
    console.print(notes_table)

    # Інше
    other_table = Table(title="⚙️ Інше", border_style="blue", box=None)
    other_table.add_column("Команда", style="magenta", width=25)
    other_table.add_column("Опис", style="white")
    other_table.add_row("hello", "Привітання")
    other_table.add_row("help", "Показати цю довідку")
    other_table.add_row("exit / close", "Вийти з програми")
    console.print(other_table)


def confirm_action(message):
    """Запит підтвердження з гарним виглядом"""
    return Confirm.ask(f"[yellow]❓ {message}[/yellow]")


def get_input(message):
    """Гарне введення даних"""
    return Prompt.ask(f"[cyan]➡️ {message}[/cyan]")

# src/utils/ui.py (додайте ці функції до існуючих)


def print_contact_added(name):
    """Успішне додавання контакту"""
    console.print(f"✅ [green]Контакт [bold]{name}[/bold] додано.[/green]")


def print_contact_updated(name):
    """Оновлення контакту"""
    console.print(f"🔄 [green]Контакт [bold]{name}[/bold] оновлено.[/green]")


def print_contact_deleted(name):
    """Видалення контакту"""
    console.print(f"🗑️ [green]Контакт [bold]{name}[/bold] видалено.[/green]")


def print_phone_added(name, phone):
    """Додавання телефону"""
    console.print(
        f"📞 [green]Телефон [bold]{phone}[/bold] додано до контакту [bold]{name}[/bold].[/green]")


def print_phone_removed(name, phone):
    """Видалення телефону"""
    console.print(
        f"📞 [green]Телефон [bold]{phone}[/bold] видалено з контакту [bold]{name}[/bold].[/green]")


def print_birthday_added(name):
    """Додавання дня народження"""
    console.print(
        f"🎂 [green]День народження додано до контакту [bold]{name}[/bold].[/green]")


def print_note_added(title):
    """Додавання нотатки"""
    console.print(f"📝 [green]Нотатку [bold]'{title}'[/bold] додано.[/green]")


def print_note_updated(title):
    """Оновлення нотатки"""
    console.print(f"📝 [green]Нотатку [bold]'{title}'[/bold] оновлено.[/green]")


def print_note_deleted(title):
    """Видалення нотатки"""
    console.print(
        f"🗑️ [green]Нотатку [bold]'{title}'[/bold] видалено.[/green]")


def print_tag_added(title, tag):
    """Додавання тегу"""
    console.print(
        f"🏷️ [green]Тег [bold]{tag}[/bold] додано до нотатки [bold]'{title}'[/bold].[/green]")
