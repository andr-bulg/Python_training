from model.group import Group

def test_modify_group_name(app):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    """
    app.group.modify_first_group(Group(name="test_group_7"))

def test_modify_group_header(app):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    """
    app.group.modify_first_group(Group(header="Group_5"))

def test_modify_group_footer(app):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    """
    app.group.modify_first_group(Group(footer="footer9"))


# def test_modify_first_group(app):
#     """
#     Тестовая функция
#     :param app: фикстура (объект, который возвращает функция app())
#     """
#     app.group.modify_first_group(Group(name="test_group_3", header="Group_3", footer="footer3"))

