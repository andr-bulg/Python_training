from model.contact import Contact

def test_modify_contact_first_name(app):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    """
    app.contact.modify_first_contact(Contact(first_name="Василий"))

def test_modify_contact_last_name(app):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    """
    app.contact.modify_first_contact(Contact(last_name="Николаев"))

def test_modify_contact_address(app):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    """
    app.contact.modify_first_contact(Contact(address="Магнитогорск"))

def test_modify_contact_mobile_phone(app):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    """
    app.contact.modify_first_contact(Contact(mobile_phone="+79112223344"))

def test_modify_contact_email(app):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    """
    app.contact.modify_first_contact(Contact(email="nkkolaev@mail.ru"))

def test_modify_contact_date_of_birth(app):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    """
    app.contact.modify_first_contact(Contact(day='17', month="December", year="2000"))

def test_modify_first_contact(app):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    """
    app.contact.modify_first_contact(Contact(first_name="Petr", last_name="Petrov",
                               address="Omsk", mobile_phone="+79231234545", email="petrov@test.ru",
                               day="11", month="May", year="1997"))

