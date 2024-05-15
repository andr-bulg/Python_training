# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, json_contacts):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    :param json_contacts: тестовые данные из файла формата json
    """
    contact = json_contacts
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

