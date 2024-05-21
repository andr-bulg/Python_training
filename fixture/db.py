"""
Создаём класс DbFixture, который инциализирует фикстуру
для взаимодействия с базой данных приложения
"""

import pymysql
class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, db=name, user=user, password=password)

    def destroy(self):
        self.connection.close()


