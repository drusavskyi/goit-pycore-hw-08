from .fields import Name, Phone, Birthday

class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.birthday: Birthday | None = None

    # --- телефони ---
    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def change_phone(self, old: str, new: str):
        for i, ph in enumerate(self.phones):
            if ph.value == old:
                self.phones[i] = Phone(new)
                return
        raise ValueError("Old phone not found")

    # --- дні народження ---
    def add_birthday(self, date_str: str):
        if self.birthday:
            raise ValueError("Birthday already set")
        self.birthday = Birthday(date_str)

    # --- зручний формат для сприйняття ---
    def __str__(self):
        phones = ", ".join(p.value for p in self.phones) or "no phones"
        bday = self.birthday.value.strftime("%d.%m.%Y") if self.birthday else "n/a"
        return f"{self.name.value}: {phones}; birthday: {bday}"