"""
Создаём класс DbFixture, который инциализирует фикстуру
для взаимодействия с базой данных приложения
"""

import pymysql
from model.group import Group
from model.contact import Contact

class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, db=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list_of_groups = []
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT group_id, group_name, group_header, group_footer FROM group_list")
            for row in cursor:
                (id_group, name, header, footer) = row
                list_of_groups.append(Group(id_group=str(id_group), name=name, header=header, footer=footer))
        return list_of_groups

    def get_contact_list(self):
        list_of_contacts = []
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT id, firstname, lastname, address, home, mobile, work, email, email2, "
                           "email3 FROM addressbook WHERE deprecated IS NULL")
            for row in cursor:
                (id_contact, first_name, last_name, address, home_phone, mobile_phone, work_phone,
                 email_1, email_2, email_3) = row
                list_of_contacts.append(Contact(id_contact=str(id_contact), first_name=first_name,
                                                last_name=last_name, address=address,
                                                home_phone=home_phone, mobile_phone=mobile_phone,
                                                work_phone=work_phone, email_1=email_1,
                                                email_2=email_2, email_3=email_3))
        return list_of_contacts

    def destroy(self):
        self.connection.close()

