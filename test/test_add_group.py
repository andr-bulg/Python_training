# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    """
    app.group.create(Group(name="test_group_2", header="Group_2", footer="footer2"))

