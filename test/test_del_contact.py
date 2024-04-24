def test_delete_first_contact(app):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    """
    app.contact.delete_first_contact()

