from model.contact import Contact
from random import randrange

def test_delete_some_contact(app):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    """
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Irina", last_name="Ivanova", address="Kazan",
                                    mobile_phone="+79161234565", email="ivanova@test.ru",
                                    day="22", month="July", year="2005"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts

