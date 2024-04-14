# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
from lesson_2.contact import Contact


class TestAddContact(unittest.TestCase):

    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        self.login(username="admin", password="secret")
        self.create_contact(Contact(first_name="Ivan", last_name="Ivanov",
                                        address="Moscow", mobile_phone="+79031234567", email="ivanov@test.ru",
                                        day="2", month="March", year="1991"))
        self.logout()

    def test_add_empty_contact(self):
        self.login(username="admin", password="secret")
        self.create_contact(Contact(first_name="", last_name="",
                                        address="", mobile_phone="", email="",
                                        day="", month="-", year=""))
        self.logout()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def return_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def create_contact(self, contact_obj):
        wd = self.wd
        self.open_page_to_add_contact()
        # Заполняем форму данных для создаваемого контакта
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact_obj.first_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact_obj.last_name)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact_obj.address)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact_obj.mobile_phone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact_obj.email)
        # Указываем дату рождения при заполнении формы
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact_obj.day)
        wd.find_element_by_xpath("//option[@value={!r}]".format(contact_obj.day)).click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact_obj.month)
        wd.find_element_by_xpath("//option[@value={!r}]".format(contact_obj.month)).click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact_obj.year)
        # Подтверждаем создание контакта
        wd.find_element_by_xpath("//input[20]").click()
        self.return_to_home_page()

    def open_page_to_add_contact(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
