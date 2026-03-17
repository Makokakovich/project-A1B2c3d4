# src/utils/cli_analyzer.py
"""
Модуль для TAB-автодоповнення команд у консолі.
Використовує prompt_toolkit для надійної роботи на всіх платформах.
"""

from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.styles import Style

# Список усіх команд
COMMANDS = [
    "add", "change", "phone", "all", "find", "delete",
    "add-birthday", "birthdays", "add-note", "notes",
    "find-note", "edit-note", "delete-note", "add-tag",
    "tag", "sort-notes", "hello", "help", "exit", "close",
]

# Стиль для підказок
style = Style.from_dict({
    'completion-menu.completion': 'bg:#008888 #ffffff',
    'completion-menu.completion.current': 'bg:#00aaaa #000000',
    'scrollbar.background': 'bg:#88aaaa',
    'scrollbar.button': 'bg:#222222',
})

# Глобальна змінна для сесії
_session = None


def get_session():
    """Створює або повертає існуючу сесію prompt_toolkit"""
    global _session
    if _session is None:
        # Створюємо доповнювач слів
        completer = WordCompleter(COMMANDS, ignore_case=True)

        # Створюємо сесію з історією та автодоповненням
        _session = PromptSession(
            completer=completer,
            history=InMemoryHistory(),
            auto_suggest=AutoSuggestFromHistory(),
            style=style,
            complete_while_typing=True,
            enable_history_search=True
        )
    return _session


def enable_cli_analyzer():
    """Активує автодоповнення команд по TAB"""
    print("✓ Автодоповнення активовано (prompt_toolkit)")
    get_session()
    return True


def prompt_with_completion(message=">> "):
    """
    Функція для використання замість input()
    Повертає введений рядок з автодоповненням
    """
    session = get_session()
    try:
        return session.prompt(message)
    except (KeyboardInterrupt, EOFError):
        return "exit"
