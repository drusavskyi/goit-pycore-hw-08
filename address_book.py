from collections import UserDict
from datetime import date, timedelta
from pathlib import Path
import pickle

from .record import Record   # relative import усередині пакета

# Файл даних лежить у тій же папці, що й цей модуль
DATA_PATH = Path(__file__).resolve().parent / "assistant_book.pkl"


class AddressBook(UserDict):
    """Контейнер для об'єктів Record"""

    # ---------- базові операції ---------------------------------
    def add_record(self, record: Record) -> None:
        """Додає або замінює запис за іменем"""
        self.data[record.name.value] = record

    def find(self, name: str) -> Record | None:
        return self.data.get(name)

    def __iter__(self):
        return iter(self.data.values())

    def delete_record(self, name: str) -> bool:
        if name in self.data:
            del self.data[name]
            return True
        return False

    # ---------- дні народження ----------------------------------
    def get_upcoming_birthdays(self, days: int = 7) -> list[tuple[str, str]]:
        """Повертає [(name, DD.MM.YYYY), ...] для найближчих N днів"""
        today = date.today()
        last_day = today + timedelta(days=days)
        upcoming: list[tuple[str, str]] = []

        for rec in self:
            if rec.birthday:
                bday = rec.birthday.value.replace(year=today.year)
                if bday < today:                     # вже пройшов цього року
                    bday = bday.replace(year=today.year + 1)
                if today <= bday <= last_day:
                    upcoming.append((rec.name.value, bday.strftime("%d.%m.%Y")))
        return upcoming

    # ---------- серіалізація ------------------------------------
    def save(self, path: Path = DATA_PATH) -> None:
        """Записує поточну книгу у двійковий pickle-файл"""
        with open(path, "wb") as fh:
            pickle.dump(self.data, fh)

    @classmethod
    def load(cls, path: Path = DATA_PATH) -> "AddressBook":
        """Читає книгу з диска або повертає порожню, якщо файлу немає"""
        book = cls()
        if path.exists():
            with open(path, "rb") as fh:
                book.data = pickle.load(fh)
        return book
