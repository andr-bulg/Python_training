# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string
import datetime
import calendar

def random_first_last_name(maxlen):
    capital_letter = string.ascii_uppercase
    symbols = string.ascii_lowercase + string.digits + " "
    return random.choice(capital_letter) + "".join([random.choice(symbols)
                                                    for i in range(random.randrange(maxlen))])

def random_address(maxlen):
    symbols = string.ascii_letters + string.digits + " " * 5
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_phone_number(maxlen):
    digits = string.digits
    return "+" + "".join([random.choice(digits) for i in range(maxlen)])

def random_email(maxlen):
    name_user = string.ascii_lowercase + string.digits + "_" + "-"
    name_user = "".join([random.choice(name_user) for i in range(random.randrange(1, maxlen))])
    domain_part_1 = string.ascii_lowercase
    domain_part_1 = "".join([random.choice(domain_part_1) for i in range(random.randrange(4, 7))])
    domain_part_2 = string.ascii_lowercase
    domain_part_2 = "".join([random.choice(domain_part_2) for i in range(random.randrange(2, 4))])
    return name_user + "@" + domain_part_1 + "." + domain_part_2

def random_date():
    year = random.randint(1900, 2023)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    date = datetime.date(year, month, day)
    date = list(map(lambda x: int(x), date.strftime("%d.%m.%Y").split(".")))
    date[1] = calendar.month_name[date[1]]
    return date

some_contact = [Contact(first_name="Ivan", last_name="Ivanov", address="Moscow",
                        home_phone="+74991234567",mobile_phone="+79031234567",
                        work_phone="+79981234567", fax="+74951234567", email_1="ivanov_1@test.ru",
                        email_2="ivanov_2@test.ru", email_3="ivanov_3@test.ru",
                        day="2", month="March", year="1991")]

empty_contact = [Contact(first_name="", last_name="", address="", home_phone="", mobile_phone="",
                       work_phone="", fax="", email_1="", email_2="", email_3="",
                       day="", month="-", year="")]

test_data = empty_contact + some_contact + \
            [Contact(first_name=random_first_last_name(10), last_name=random_first_last_name(10),
                        address=random_address(20), home_phone=random_phone_number(10),
                        mobile_phone=random_phone_number(10), work_phone=random_phone_number(10),
                        fax=random_phone_number(10), email_1=random_email(12),
                        email_2=random_email(12), email_3=random_email(12),
                        day=repr(random_date()[0]), month=random_date()[1], year=repr(random_date()[2]))
            for i in range(3)]

@pytest.mark.parametrize("contact", test_data, ids=[repr(el) for el in test_data])
def test_add_contact(app, contact):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    :param contact: тестовые данные
    """
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

