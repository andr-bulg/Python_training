# -*- coding: utf-8 -*-
from model.group import Group
import allure

def test_add_group(app, db, json_groups, check_ui):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    :param db: фикстура работы с бд
    :param json_groups: тестовые данные из файла формата json
    :param check_ui: фикстура, отвечающая за проверку UI
    """
    group = json_groups
    with allure.step("Given a group list"):
        old_groups = db.get_group_list()
    with allure.step(f"When I add a group {group} to the list"):
        app.group.create(group)
    with allure.step(f"Then the new group list is equal to the old list with the added group"):
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            new_groups = map(app.group.clean, new_groups)
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

