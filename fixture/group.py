"""
Создаём класс-помощник GroupHelper по работе с группами
"""

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def data_form_completion(self, group_obj):
        # Заполняем/модифицируем форму данных для создаваемой группы
        wd = self.app.wd
        self.change_field_value("group_name", group_obj.name)
        self.change_field_value("group_header", group_obj.header)
        self.change_field_value("group_footer", group_obj.footer)

    def change_field_value(self, field_name, text):
        """
        :param field_name: название заполняемого поля
        :param text: текстовое значение, которое будет добавлено в поле
        """
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create(self, group_obj):
        wd = self.app.wd
        self.open_groups_page()
        # Начинаем создание группы
        wd.find_element_by_name("new").click()
        self.data_form_completion(group_obj)
        # Подтверждаем создание группы
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def modify_first_group(self, group_obj):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        # Вносим изменения в форму данных для выбранной группы
        self.data_form_completion(group_obj)
        # Подтверждаем изменение группы
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

