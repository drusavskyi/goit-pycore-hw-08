from datetime import datetime
import re

class Field:
    def __init__(self, value: str):
        self.value = value

class Name(Field):
    pass

PHONE_PATTERN = re.compile(r"^\d{10}$")

class Phone(Field):
    def __init__(self, value: str):
        if not PHONE_PATTERN.fullmatch(value):
            raise ValueError("Phone must be 10 digits.")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value: str):
        try:
            # зберігаємо одразу datetime.date
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")