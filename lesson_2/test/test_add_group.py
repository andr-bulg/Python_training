# -*- coding: utf-8 -*-
import pytest
from lesson_2.model.group import Group
from lesson_2.fixture.application_group import Application_group


@pytest.fixture
def app(request):
    """
    Функция, которая создаёт и разрушает фикстуру
    :param request: специальный параметр
    :return: фикстура (объект класса Application_group)
    """
    fixture = Application_group()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    """
    app.login(username="admin", password="secret")
    app.create_group(Group(name="test_group_2", header="Group_2", footer="footer2"))
    app.logout()

