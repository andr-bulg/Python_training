from lesson_2.model.contact import Contact

def test_modify_first_contact(app):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    """
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(first_name="Petr", last_name="Petrov",
                               address="Omsk", mobile_phone="+79231234545", email="petrov@test.ru",
                               day="11", month="May", year="1997"))
    app.session.logout()

