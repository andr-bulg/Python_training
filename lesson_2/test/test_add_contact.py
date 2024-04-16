# -*- coding: utf-8 -*-
import pytest
from lesson_2.model.contact import Contact
from lesson_2.fixture.application import Application


@pytest.fixture
def app(request):
    """
    Функция, которая создаёт и разрушает фикстуру
    :param request: специальный параметр
    :return: фикстура (объект класса Application_contact)
    """
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    """
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="Ivan", last_name="Ivanov",
                               address="Moscow", mobile_phone="+79031234567", email="ivanov@test.ru",
                               day="2", month="March", year="1991"))
    app.session.logout()

def test_add_empty_contact(app):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    """
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="", last_name="",
                               address="", mobile_phone="", email="",
                               day="", month="-", year=""))
    app.session.logout()

