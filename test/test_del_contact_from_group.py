# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group


def test_delete_contact_from_group(app, db, orm):
    """
    Тестовая функция
    :param app: фикстура (объект, который возвращает функция app())
    :param db: фикстура работы с бд
    :param json_contacts: фикстура orm
    """
    groups = db.get_group_list()
    contacts = db.get_contact_list()
    if not groups:
        app.group.create(Group(name="test_group_0", header="Group_0", footer="footer0"))
    if not contacts:
        app.contact.create(Contact(first_name="Irina", last_name="Ivanova", address="Kazan",
                                   home_phone="+74961234565", mobile_phone="+79161234565",
                                   work_phone="+79981237361", fax="+74981234567",
                                   email_1="ivanova_1@test.ru", email_2="ivanova_2@test.ru",
                                   email_3="ivanova_3@test.ru", day="22", month="July", year="2005"))
    some_group = None
    for group in groups:
        if orm.get_contacts_in_group(group):
            some_group = group
            break

    if some_group is None:
        groups = db.get_group_list()
        app.contact.add_first_contact_to_group(groups[0])
        some_group = groups[0]

    count_contacts_before = len(orm.get_contacts_in_group(some_group))
    app.contact.delete_first_contact_from_group(some_group)
    count_contacts_after = len(orm.get_contacts_in_group(some_group))
    assert count_contacts_before - 1 == count_contacts_after

