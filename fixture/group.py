"""
Создаём класс-помощник GroupHelper по работе с группами
"""
from model.group import Group

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/groups.php") and len(wd.find_elements_by_name("new")) > 0):
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
        self.group_cache = None

    def return_to_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/groups.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("group page").click()

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_group_by_id(self, id_group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id_group)
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def modify_group_by_index(self, index, group_obj):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("edit").click()
        # Вносим изменения в форму данных для выбранной группы
        self.data_form_completion(group_obj)
        # Подтверждаем изменение группы
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def modify_group_by_id(self, id_group, group_obj):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id_group)
        wd.find_element_by_name("edit").click()
        # Вносим изменения в форму данных для выбранной группы
        self.data_form_completion(group_obj)
        # Подтверждаем изменение группы
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def modify_first_group(self, group_obj):
        self.modify_group_by_index(0, group_obj)

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id_group):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='{}']".format(id_group)).click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None
    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id_group = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id_group=id_group))
        return list(self.group_cache)

    @staticmethod
    def clean(group):
        return Group(id_group=group.id_group, name=group.name.strip())

