from model.contact import Contact

def test_delete_first_contact(app):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    """
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Irina", last_name="Ivanova", address="Kazan",
                                    mobile_phone="+79161234565", email="ivanova@test.ru",
                                    day="22", month="July", year="2005"))
    app.contact.delete_first_contact()

