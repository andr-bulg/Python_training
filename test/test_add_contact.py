# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    """
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(first_name="Ivan", last_name="Ivanov",
                               address="Moscow", mobile_phone="+79031234567", email="ivanov@test.ru",
                               day="2", month="March", year="1991"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)

def test_add_empty_contact(app):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    """
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(first_name="", last_name="",
                               address="", mobile_phone="", email="",
                               day="", month="-", year=""))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
