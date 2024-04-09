# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
from lesson_1.account import Account


class TestAddContact(unittest.TestCase):

    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    
    def test_add_contact(self):
        wd = self.wd

        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_page_to_add_account(wd)
        self.create_account(wd, Account(first_name="Ivan", last_name="Ivanov",
                                        address="Moscow", mobile_phone="+79031234567", email="ivanov@test.ru",
                                        day="2", month="March", year="1991"))
        self.return_to_home_page(wd)
        self.logout(wd)


    def test_add_empty_contact(self):
        wd = self.wd

        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_page_to_add_account(wd)
        self.create_account(wd, Account(first_name="", last_name="",
                                        address="", mobile_phone="", email="",
                                        day="", month="-", year=""))
        self.return_to_home_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def create_account(self, wd, account_obj):
        # Заполняем форму данных для создаваемого аккаунта
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(account_obj.first_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(account_obj.last_name)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(account_obj.address)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(account_obj.mobile_phone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(account_obj.email)
        # Указываем дату рождения при заполнении формы
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(account_obj.day)
        wd.find_element_by_xpath("//option[@value={!r}]".format(account_obj.day)).click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(account_obj.month)
        wd.find_element_by_xpath("//option[@value={!r}]".format(account_obj.month)).click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(account_obj.year)
        # Подтверждаем создание аккаунта
        wd.find_element_by_xpath("//input[20]").click()

    def open_page_to_add_account(self, wd):
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
