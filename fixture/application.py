"""
Создаём класс Application, который будет представлять собой фикстуру,
и содержать все необходимые вспомогательные методы.
"""

from selenium import webdriver
# from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:

    def __init__(self, browser="firefox"):
        """
        Инициализация фикстуры
        """
        # if browser == "firefox":
        #     self.wd = webdriver.Firefox()
        # elif browser == "chrome":
        #     self.wd = webdriver.Chrome()
        # elif browser == "edge":
        #     self.wd = webdriver.Edge()
        # else:
        #     raise ValueError("Unrecognized browser {}".format(browser))

        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(5)
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

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

