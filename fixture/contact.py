"""
Создаём класс-помощник ContactHelper по работе с контактами
"""

from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_page_to_add_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def data_form_completion(self, contact_obj):
        wd = self.app.wd
        # Заполняем/модифицируем форму данных для создаваемого контакта
        self.change_field_value("firstname", contact_obj.first_name)
        self.change_field_value("lastname", contact_obj.last_name)
        self.change_field_value("address", contact_obj.address)
        self.change_field_value("home", contact_obj.home_phone)
        self.change_field_value("mobile", contact_obj.mobile_phone)
        self.change_field_value("work", contact_obj.work_phone)
        self.change_field_value("fax", contact_obj.fax)
        self.change_field_value("email", contact_obj.email_1)
        self.change_field_value("email2", contact_obj.email_2)
        self.change_field_value("email3", contact_obj.email_3)
        # Указываем дату рождения при заполнении формы
        self.change_field_value_date("bday", contact_obj.day, "//option[@value={!r}]")
        self.change_field_value_date("bmonth", contact_obj.month, "//option[@value={!r}]")
        self.change_field_value("byear", contact_obj.year)

    def change_field_value_date(self, field_name, text, xpath):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
            wd.find_element_by_xpath(xpath.format(text)).click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create(self, contact_obj):
        contact_obj = contact_obj
        wd = self.app.wd
        self.open_home_page()
        self.open_page_to_add_contact()
        # Заполняем форму данных для создаваемого контакта
        self.data_form_completion(contact_obj)
        # Подтверждаем создание контакта
        wd.find_element_by_xpath("//input[20]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.find_elements_by_xpath("//input[@value='Send e-Mail']")):
            wd.find_element_by_link_text("home page").click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.contact_cache = None

    def delete_contact_by_id(self, id_contact):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_id(id_contact)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id_contact):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='{}']".format(id_contact)).click()

    def select_first_contact(self):
        wd = self.app.wd
        self.select_contact_by_index(0)

    def modify_contact_by_index(self, index, contact_obj):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        # Вносим изменения в форму данных для выбранного контакта
        self.data_form_completion(contact_obj)
        # Подтверждаем изменение контакта
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def modify_contact_by_id(self, id_contact, contact_obj):
        wd = self.app.wd
        self.open_contact_to_edit_by_id(id_contact)
        # Вносим изменения в форму данных для выбранного контакта
        self.data_form_completion(contact_obj)
        # Подтверждаем изменение контакта
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def modify_first_contact(self, contact_obj):
        self.modify_contact_by_index(0, contact_obj)

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.find_elements_by_xpath("//input[@value='Send e-Mail']")):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None
    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr[name]"):
                cells = element.find_elements_by_tag_name("td")
                id_contact = cells[0].find_element_by_tag_name("input").get_attribute("value")
                first_name = cells[2].text
                last_name = cells[1].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(first_name=first_name, last_name=last_name,
                                                  address=address, id_contact=id_contact,
                                                  all_emails_from_home_page=all_emails,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_edit_by_id(self, id_contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_css_selector("a[href='edit.php?id={}']".format(id_contact)).click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        id_contact = wd.find_element_by_name("id").get_attribute("value")
        email_1 = wd.find_element_by_name("email").get_attribute("value")
        email_2 = wd.find_element_by_name("email2").get_attribute("value")
        email_3 = wd.find_element_by_name("email3").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        return Contact(first_name=first_name, last_name=last_name, address=address,
                       id_contact=id_contact, email_1=email_1, email_2=email_2, email_3=email_3,
                       home_phone=home_phone, mobile_phone=mobile_phone,
                       work_phone=work_phone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        return Contact(home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone)

