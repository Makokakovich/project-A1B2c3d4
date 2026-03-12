# Персональний помічник

Командний проєкт з курсу Python Programming — Neoversity.
Команда: **Pythoneers**

CLI-застосунок для керування контактами та нотатками через термінал.

## Запуск

Python 3.10 або новіший.

```bash
git clone https://github.com/Makokakovich/project-A1B2c3d4.git
cd project-A1B2c3d4
python main.py
```

## Команди

### Контакти

| Команда | Що робить |
|---------|-----------|
| `add <ім'я> <телефон>` | Додати контакт або новий телефон |
| `change <ім'я> <старий> <новий>` | Змінити номер телефону |
| `phone <ім'я>` | Показати телефони контакту |
| `all` | Показати всі контакти |
| `find <запит>` | Пошук за іменем або телефоном |
| `delete <ім'я>` | Видалити контакт |
| `add-birthday <ім'я> <ДД.ММ.РРРР>` | Додати день народження |
| `birthdays <кількість днів>` | Найближчі дні народження |

### Нотатки

| Команда | Що робить |
|---------|-----------|
| `add-note <назва> <текст>` | Додати нотатку |
| `notes` | Показати всі нотатки |
| `find-note <запит>` | Пошук за текстом |
| `edit-note <назва> <новий текст>` | Редагувати нотатку |
| `delete-note <назва>` | Видалити нотатку |
| `tag <тег>` | Знайти нотатки за тегом |

### Інше

| Команда | Що робить |
|---------|-----------|
| `hello` | Привітання |
| `help` | Список команд |
| `exit` / `close` | Зберегти і вийти |

## Збереження даних

Дані зберігаються автоматично при виході в `~/.personal_assistant/` і залишаються після перезапуску.

## Структура проєкту

```
main.py                        # точка входу, головний цикл
src/
  models/
    fields.py                  # класи полів: Name, Phone, Email, Birthday, Address
    record.py                  # клас Record (один контакт)
    address_book.py            # клас AddressBook (колекція контактів)
    note.py                    # клас Note (одна нотатка)
    notes_book.py              # клас NotesBook (колекція нотаток)
  handlers/
    contact_handlers.py        # обробники команд для контактів
    note_handlers.py           # обробники команд для нотаток
  utils/
    validators.py              # валідація телефону та email
    storage.py                 # збереження та завантаження даних (pickle)
```

## Команда

| Учасник | Роль | Задачі |
|---------|------|--------|
| **Maksym Karmazynovskyi** | Team Lead | архітектура проєкту, main.py, address_book, інтеграція модулів, code review |
| **Vladyslav Krasnovskyi** | Scrum Master | note.py, notes_book.py, note_handlers.py, організація стендапів, Trello |
| **Maksym Kryvenko** | Developer | fields.py, record.py |
| **Olga Dobrynina** | Developer | validators.py, storage.py, contact_handlers.py |
