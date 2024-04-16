"""
Создаём класс Application_group, который будет представлять собой фикстуру,
и содержать все необходимые вспомогательные методы.
"""

from selenium import webdriver
from lesson_2.fixture.session import SessionHelper
from lesson_2.fixture.group import GroupHelper
from lesson_2.fixture.contact import ContactHelper

class Application:

    def __init__(self):
        """
        Инициализация фикстуры
        """
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        """
        Разрушение фикстуры
        """
        self.wd.quit()

