# -*- coding: utf-8 -*-
from model.group import Group
import pytest
from data.add_group import constant as test_data


@pytest.mark.parametrize("group", test_data, ids=[repr(el) for el in test_data])
def test_add_group(app, group):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    :param group: тестовые данные
    """
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

