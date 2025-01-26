"""
Создаём класс Application, который будет представлять собой фикстуру,
и содержать все необходимые вспомогательные методы.
"""

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:

    def __init__(self, browser, base_url):
        """
        Инициализация фикстуры
        """
        if browser == "firefox":
            self.options = Options()
            self.options.binary_location = r'C:/Program Files/Mozilla Firefox/firefox.exe'
            self.wd = webdriver.Firefox(executable_path=r'C:/Windows/System32/geckodriver.exe', options=self.options)
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser {}".format(browser))

        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

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

