from model.group import Group
import random

def test_modify_group_name(app):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    """
    if app.group.count() == 0:
        app.group.create(Group(name="test_group_0", header="Group_0", footer="footer0"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="test_group_7"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_modify_group_header(app):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    """
    if app.group.count() == 0:
        app.group.create(Group(name="test_group_0", header="Group_0", footer="footer0"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="Group_5"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_modify_group_footer(app):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    """
    if app.group.count() == 0:
        app.group.create(Group(name="test_group_0", header="Group_0", footer="footer0"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(footer="footer9"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_modify_some_group(app, db, check_ui):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    :param db: фикстура работы с бд
    :param check_ui: фикстура, отвечающая за проверку UI
    """
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test_group_0", header="Group_0", footer="footer0"))
    old_groups = db.get_group_list()
    modified_group = random.choice(old_groups)
    group = Group(name="test_group_3", header="Group_3", footer="footer3")
    group.id_group = modified_group.id_group
    app.group.modify_group_by_id(modified_group.id_group, group)
    new_groups = db.get_group_list()
    old_groups.remove(modified_group)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        new_groups = map(app.group.clean, new_groups)
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

