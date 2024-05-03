from model.group import Group
from random import randrange

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

def test_modify_some_group(app):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    """
    if app.group.count() == 0:
        app.group.create(Group(name="test_group_0", header="Group_0", footer="footer0"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="test_group_3", header="Group_3", footer="footer3")
    group.id_group = old_groups[index].id_group
    app.group.modify_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

