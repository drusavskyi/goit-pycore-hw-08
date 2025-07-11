from .address_book import AddressBook
from .cli_handlers import (
    add_contact,
    change_phone,
    show_phones,
    add_birthday,
    show_birthday,
    birthdays,
    list_all,
    delete_contact,
)

# --- команди, що змінюють книгу ---
MUTATING = {"add", "change", "add-birthday", "delete"}

COMMANDS = {
    "add": add_contact,
    "change": change_phone,
    "phone": show_phones,
    "all": list_all,
    "add-birthday": add_birthday,
    "show-birthday": show_birthday,
    "birthdays": birthdays,
    "delete": delete_contact,
}

def parse_input(text: str):
    """Розбиває введення на команду та аргументи.
    Якщо рядок порожній ‒ повертає ('', []).
    """
    parts = text.strip().split()
    if not parts:           # користувач натиснув просто Enter
        return "", []
    return parts[0].lower(), parts[1:]

def main():
    book = AddressBook.load()          # відновлюємо дані з диска
    print("Welcome to the assistant bot!")

    while True:
        cmd, args = parse_input(input("Enter a command: "))

        if not cmd:                    # порожній ввід ‒ нічого не робимо
            continue

        if cmd in ("close", "exit"):
            print("Good bye!")
            break

        elif cmd == "hello":
            print("How can I help you?")

        elif cmd in COMMANDS:
            result = COMMANDS[cmd](args, book)
            print(result)

            if cmd in MUTATING:        # зберігаємо лише після змін
                book.save()

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
