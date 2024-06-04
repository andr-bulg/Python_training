# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group


def test_add_contact_to_group(app, db, orm):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    :param db: фикстура работы с бд
    :param json_contacts: фикстура orm
    """

    if not db.get_group_list():
        app.group.create(Group(name="test_group_0", header="Group_0", footer="footer0"))

    if not db.get_contact_list():
        app.contact.create(Contact(first_name="Irina", last_name="Ivanova", address="Kazan",
                                   home_phone="+74961234565", mobile_phone="+79161234565",
                                   work_phone="+79981237361", fax="+74981234567",
                                   email_1="ivanova_1@test.ru", email_2="ivanova_2@test.ru",
                                   email_3="ivanova_3@test.ru", day="22", month="July", year="2005"))
    groups = db.get_group_list()

    for group in groups:
        if not orm.get_contacts_in_group(group):
            app.contact.add_first_contact_to_group(group)
            result = group
            assert len(orm.get_contacts_in_group(result)) == 1
            break
    else:
        app.contact.delete_all_contacts_from_group(groups[0])
        app.contact.add_first_contact_to_group(groups[0])
        result = groups[0]
        assert len(orm.get_contacts_in_group(result)) == 1
