def test_delete_first_group(app):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    """
    app.group.delete_first_group()

