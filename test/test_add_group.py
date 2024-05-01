# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    """
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="test_group_2", header="Group_2", footer="footer2"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

