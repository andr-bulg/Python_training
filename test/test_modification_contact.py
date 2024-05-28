from model.contact import Contact
import random

def test_modify_contact_first_name(app, db):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    :param db: фикстура работы с бд
    """
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="Irina", last_name="Ivanova", address="Kazan",
                                   home_phone="+74961234565", mobile_phone="+79161234565",
                                   work_phone="+79981237361", fax="+74981234567",
                                   email_1="ivanova_1@test.ru", email_2="ivanova_2@test.ru",
                                   email_3="ivanova_3@test.ru", day="22", month="July", year="2005"))
    old_contacts = db.get_contact_list()
    modified_contact = Contact(first_name="Василий", last_name=old_contacts[0].last_name,
                      address=old_contacts[0].address, home_phone=old_contacts[0].home_phone,
                      mobile_phone=old_contacts[0].mobile_phone, work_phone=old_contacts[0].work_phone,
                      fax=old_contacts[0].fax, email_1=old_contacts[0].email_1,
                      email_2=old_contacts[0].email_2, email_3=old_contacts[0].email_3,
                      day=old_contacts[0].day, month=old_contacts[0].month,
                      year=old_contacts[0].year)
    modified_contact.id_contact = old_contacts[0].id_contact
    contact = Contact(first_name="Василий")
    contact.id_contact = old_contacts[0].id_contact
    app.contact.modify_contact_by_id(modified_contact.id_contact, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = modified_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_modify_contact_last_name(app, db):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    :param db: фикстура работы с бд
    """
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="Irina", last_name="Ivanova", address="Kazan",
                                   home_phone="+74961234565", mobile_phone="+79161234565",
                                   work_phone="+79981237361", fax="+74981234567",
                                   email_1="ivanova_1@test.ru", email_2="ivanova_2@test.ru",
                                   email_3="ivanova_3@test.ru", day="22", month="July", year="2005"))
    old_contacts = db.get_contact_list()
    modified_contact = Contact(first_name=old_contacts[0].first_name, last_name="Николаев",
                               address=old_contacts[0].address, home_phone=old_contacts[0].home_phone,
                               mobile_phone=old_contacts[0].mobile_phone, work_phone=old_contacts[0].work_phone,
                               fax=old_contacts[0].fax, email_1=old_contacts[0].email_1,
                               email_2=old_contacts[0].email_2, email_3=old_contacts[0].email_3,
                               day=old_contacts[0].day, month=old_contacts[0].month,
                               year=old_contacts[0].year)
    modified_contact.id_contact = old_contacts[0].id_contact
    contact = Contact(last_name="Николаев")
    contact.id_contact = old_contacts[0].id_contact
    app.contact.modify_contact_by_id(modified_contact.id_contact, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = modified_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_modify_contact_address(app, db):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    :param db: фикстура работы с бд
    """
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="Irina", last_name="Ivanova", address="Kazan",
                                   home_phone="+74961234565", mobile_phone="+79161234565",
                                   work_phone="+79981237361", fax="+74981234567",
                                   email_1="ivanova_1@test.ru", email_2="ivanova_2@test.ru",
                                   email_3="ivanova_3@test.ru", day="22", month="July", year="2005"))
    old_contacts = db.get_contact_list()
    modified_contact = Contact(first_name=old_contacts[0].first_name, last_name=old_contacts[0].last_name,
                      address="Магнитогорск", home_phone=old_contacts[0].home_phone,
                      mobile_phone=old_contacts[0].mobile_phone, work_phone=old_contacts[0].work_phone,
                      fax=old_contacts[0].fax, email_1=old_contacts[0].email_1,
                      email_2=old_contacts[0].email_2, email_3=old_contacts[0].email_3,
                      day=old_contacts[0].day, month=old_contacts[0].month,
                      year=old_contacts[0].year)
    modified_contact.id_contact = old_contacts[0].id_contact
    contact = Contact(address="Магнитогорск")
    contact.id_contact = old_contacts[0].id_contact
    app.contact.modify_contact_by_id(modified_contact.id_contact, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = modified_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_modify_contact_mobile_phone(app, db):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    :param db: фикстура работы с бд
    """
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="Irina", last_name="Ivanova", address="Kazan",
                                   home_phone="+74961234565", mobile_phone="+79161234565",
                                   work_phone="+79981237361", fax="+74981234567",
                                   email_1="ivanova_1@test.ru", email_2="ivanova_2@test.ru",
                                   email_3="ivanova_3@test.ru", day="22", month="July", year="2005"))
    old_contacts = db.get_contact_list()
    modified_contact = Contact(first_name=old_contacts[0].first_name, last_name=old_contacts[0].last_name,
                               address=old_contacts[0].address, home_phone=old_contacts[0].home_phone,
                               mobile_phone="+79112223344", work_phone=old_contacts[0].work_phone,
                               fax=old_contacts[0].fax, email_1=old_contacts[0].email_1,
                               email_2=old_contacts[0].email_2, email_3=old_contacts[0].email_3,
                               day=old_contacts[0].day, month=old_contacts[0].month,
                               year=old_contacts[0].year)
    modified_contact.id_contact = old_contacts[0].id_contact
    contact = Contact(mobile_phone="+79112223344")
    contact.id_contact = old_contacts[0].id_contact
    app.contact.modify_contact_by_id(modified_contact.id_contact, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = modified_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_modify_contact_email(app, db):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    :param db: фикстура работы с бд
    """
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="Irina", last_name="Ivanova", address="Kazan",
                                   home_phone="+74961234565", mobile_phone="+79161234565",
                                   work_phone="+79981237361", fax="+74981234567",
                                   email_1="ivanova_1@test.ru", email_2="ivanova_2@test.ru",
                                   email_3="ivanova_3@test.ru", day="22", month="July", year="2005"))
    old_contacts = db.get_contact_list()
    modified_contact = Contact(first_name=old_contacts[0].first_name, last_name=old_contacts[0].last_name,
                      address=old_contacts[0].address, home_phone=old_contacts[0].home_phone,
                      mobile_phone=old_contacts[0].mobile_phone, work_phone=old_contacts[0].work_phone,
                      fax=old_contacts[0].fax, email_1="nikolaev@mail.ru",
                      email_2=old_contacts[0].email_2, email_3=old_contacts[0].email_3,
                      day=old_contacts[0].day, month=old_contacts[0].month,
                      year=old_contacts[0].year)
    modified_contact.id_contact = old_contacts[0].id_contact
    contact = Contact(email_1="nikolaev@mail.ru")
    contact.id_contact = old_contacts[0].id_contact
    app.contact.modify_contact_by_id(modified_contact.id_contact, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = modified_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_modify_contact_date_of_birth(app, db):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    :param db: фикстура работы с бд
    """
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="Irina", last_name="Ivanova", address="Kazan",
                                   home_phone="+74961234565", mobile_phone="+79161234565",
                                   work_phone="+79981237361", fax="+74981234567",
                                   email_1="ivanova_1@test.ru", email_2="ivanova_2@test.ru",
                                   email_3="ivanova_3@test.ru", day="22", month="July", year="2005"))
    old_contacts = db.get_contact_list()
    modified_contact = Contact(first_name=old_contacts[0].first_name, last_name=old_contacts[0].last_name,
                               address=old_contacts[0].address, home_phone=old_contacts[0].home_phone,
                               mobile_phone=old_contacts[0].mobile_phone, work_phone=old_contacts[0].work_phone,
                               fax=old_contacts[0].fax, email_1=old_contacts[0].email_1,
                               email_2=old_contacts[0].email_2, email_3=old_contacts[0].email_3,
                               day=old_contacts[0].day, month=old_contacts[0].month,
                               year=old_contacts[0].year)
    modified_contact.id_contact = old_contacts[0].id_contact
    contact = Contact(day='17', month="December", year="2000")
    contact.id_contact = old_contacts[0].id_contact
    app.contact.modify_contact_by_id(modified_contact.id_contact, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = modified_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_modify_some_contact(app, db, check_ui):
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
    modified_contact = random.choice(old_contacts)
    contact = Contact(first_name="Petr", last_name="Petrov",
                      address="Omsk", home_phone="+74560982354", mobile_phone="+79231234545",
                      work_phone="+9114569309", email_1="petrov_1@test.ru",
                      email_2="petrov_2@test.ru", email_3="petrov_3@test.ru",
                      day="11", month="May", year="1997")
    contact.id_contact = modified_contact.id_contact
    index = old_contacts.index(modified_contact)
    app.contact.modify_contact_by_id(modified_contact.id_contact, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

