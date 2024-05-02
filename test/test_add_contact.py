# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    """
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="Ivan", last_name="Ivanov",
                               address="Moscow", mobile_phone="+79031234567", email="ivanov@test.ru",
                               day="2", month="March", year="1991")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    """
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="", last_name="",
                               address="", mobile_phone="", email="",
                               day="", month="-", year="")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

