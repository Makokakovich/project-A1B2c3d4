# src/utils/cli_analyzer.py
"""
Модуль для TAB-автодоповнення команд у консолі з підказками.
"""

from prompt_toolkit import PromptSession
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.styles import Style
from prompt_toolkit.formatted_text import HTML

# Словник команд з описом формату
COMMANDS_WITH_HINTS = {
    "add": "add <ім'я> <телефон>",
    "change": "change <ім'я> <старий телефон> <новий телефон>",
    "phone": "phone <ім'я>",
    "all": "показати всі контакти",
    "find": "find <запит>",
    "delete": "delete <ім'я>",
    "add-birthday": "add-birthday <ім'я> <дд.мм.рррр>",
    "birthdays": "birthdays <днів>",
    "add-note": "add-note <назва> <текст>",
    "notes": "показати всі нотатки",
    "find-note": "find-note <запит>",
    "edit-note": "edit-note <назва> <новий текст>",
    "delete-note": "delete-note <назва>",
    "add-tag": "add-tag <назва нотатки> <тег>",
    "tag": "tag <тег>",
    "sort-notes": "sort-notes <тег>",
    "hello": "hello",
    "help": "help",
    "exit": "exit",
    "close": "close",
}

# Список тільки команд (для автодоповнення)
COMMANDS = list(COMMANDS_WITH_HINTS.keys())

# Стиль для підказок
style = Style.from_dict({
    'completion-menu.completion': 'bg:#008888 #ffffff',
    'completion-menu.completion.current': 'bg:#00aaaa #000000',
    'completion-menu.meta': 'bg:#444444 #ffffff italic',  # Стиль для підказки
})


class SmartCommandCompleter(Completer):
    """
    Розумний доповнювач з підказками формату
    """

    def __init__(self, commands_with_hints):
        self.commands_with_hints = commands_with_hints
        self.commands = list(commands_with_hints.keys())

    def get_completions(self, document, complete_event):
        text = document.text_before_cursor

        # Якщо нічого не введено - показуємо всі команди
        if not text:
            for cmd in sorted(self.commands):
                yield Completion(
                    cmd,
                    start_position=0,
                    # Це показується як підказка
                    display_meta=self.commands_with_hints[cmd]
                )
            return

        # Фільтруємо команди, що починаються з введеного тексту
        text_lower = text.lower()
        for cmd in sorted(self.commands):
            if cmd.lower().startswith(text_lower):
                yield Completion(
                    cmd,
                    start_position=-len(text),
                    # Підказка праворуч
                    display_meta=self.commands_with_hints[cmd]
                )


# Глобальна змінна для сесії
_session = None


def get_session():
    """Створює або повертає існуючу сесію prompt_toolkit"""
    global _session
    if _session is None:
        # Використовуємо наш розумний доповнювач
        completer = SmartCommandCompleter(COMMANDS_WITH_HINTS)

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
    """Активує автодоповнення команд по TAB з підказками"""
    print("✓ Автодоповнення з підказками активовано")
    get_session()
    return True


def prompt_with_completion(message=">> "):
    """
    Функція для використання замість input()
    """
    session = get_session()
    try:
        return session.prompt(message)
    except (KeyboardInterrupt, EOFError):
        return "exit"
