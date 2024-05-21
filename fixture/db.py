"""
Создаём класс DbFixture, который инциализирует фикстуру
для взаимодействия с базой данных приложения
"""

import pymysql
from model.group import Group

class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, db=name, user=user, password=password)

    def get_group_list(self):
        list_of_groups = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT group_id, group_name, group_header, group_footer FROM group_list")
            for row in cursor:
                (id_group, name, header, footer) = row
                list_of_groups.append(Group(id_group=str(id_group), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list_of_groups


    def destroy(self):
        self.connection.close()


