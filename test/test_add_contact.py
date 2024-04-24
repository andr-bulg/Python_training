# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    """
    app.contact.create(Contact(first_name="Ivan", last_name="Ivanov",
                               address="Moscow", mobile_phone="+79031234567", email="ivanov@test.ru",
                               day="2", month="March", year="1991"))

def test_add_empty_contact(app):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    """
    app.contact.create(Contact(first_name="", last_name="",
                               address="", mobile_phone="", email="",
                               day="", month="-", year=""))

