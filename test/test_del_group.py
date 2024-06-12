from model.group import Group
import random

def test_delete_some_group(app, db, check_ui):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    :param db: фикстура работы с бд
    :param check_ui: фикстура, отвечающая за проверку UI
    """
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test_group_0", header="header_0", footer="footer_0"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id_group)
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        new_groups = map(app.group.clean, new_groups)
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

