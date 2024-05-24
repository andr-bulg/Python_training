from model.contact import Contact
import random

def test_delete_some_contact(app, db, check_ui):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    :param db: фикстура работы с бд
    :param check_ui: фикстура, отвечающая за проверку UI
    """
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="Irina", last_name="Ivanova", address="Kazan",
                                   home_phone="+74961234565", mobile_phone="+79161234565",
                                   work_phone="+79981237361", fax="+74981234567",
                                   email_1="ivanova_1@test.ru", email_2="ivanova_2@test.ru",
                                   email_3="ivanova_3@test.ru", day="22", month="July", year="2005"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id_contact)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        # Проверка информации о контактах на главной странице с информацией, загруженной из базы данных
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

