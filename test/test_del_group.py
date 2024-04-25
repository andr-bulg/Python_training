from model.group import Group

def test_delete_first_group(app):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    """
    if app.group.count() == 0:
        app.group.create(Group(name="test_group_0", header="Group_0", footer="footer0"))
    app.group.delete_first_group()

