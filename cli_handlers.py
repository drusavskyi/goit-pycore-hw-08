from .address_book import AddressBook
from .record import Record
from .errors import input_error

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    msg = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        msg = "Contact added."
    record.add_phone(phone)
    return msg

@input_error
def change_phone(args, book):
    name, old, new, *_ = args
    record = book.find(name)
    if not record:
        raise KeyError("Contact not found")
    record.change_phone(old, new)
    return "Phone updated."

@input_error
def show_phones(args, book):
    name, *_ = args
    record = book.find(name)
    if not record:
        raise KeyError("Contact not found")
    return ", ".join(p.value for p in record.phones)

@input_error
def add_birthday(args, book):
    name, date_str, *_ = args
    record = book.find(name)
    if not record:
        raise KeyError("Contact not found")
    record.add_birthday(date_str)
    return "Birthday added."

@input_error
def show_birthday(args, book):
    name, *_ = args
    record = book.find(name)
    if not record or not record.birthday:
        raise KeyError("Birthday not found")
    return record.birthday.value.strftime("%d.%m.%Y")

@input_error
def birthdays(_, book):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No upcoming birthdays."
    lines = [f"{n}: {d}" for n, d in upcoming]
    return "\n".join(lines)

@input_error
def list_all(_, book):
    if not book.data:
        return "Address book is empty."
    return "\n".join(str(rec) for rec in book)

@input_error
def delete_contact(args, book: AddressBook):
    if not args:
        return "Enter the name to delete."
    name = args[0]
    if book.delete_record(name):
        return f"Contact '{name}' deleted."
    else:
        return f"Contact '{name}' not found."
