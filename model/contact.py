"""
Создаём класс Contact, в котором через инициализатор будут задаваться свойства
создаваемых объектов, чтобы затем в качестве параметров в другие методы
достаточно было передать ссылку на объект класса (параметр self).
"""

from sys import maxsize

class Contact:

    def __init__(self, first_name=None, last_name=None, address=None, home_phone=None,
                 mobile_phone=None, work_phone=None, all_phones_from_home_page=None, fax=None,
                 email_1=None, email_2=None, email_3=None, all_emails_from_home_page=None,
                 day=None, month=None, year=None, id_contact=None):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.fax = fax
        self.email_1 = email_1
        self.email_2 = email_2
        self.email_3 = email_3
        self.all_emails_from_home_page = all_emails_from_home_page
        self.day = day
        self.month = month
        self.year = year
        self.id_contact = id_contact

    def __repr__(self):
        return f"{self.id_contact}: {self.first_name} {self.last_name}"

    def __eq__(self, other):
        return (self.id_contact is None or other.id_contact is None or self.id_contact == other.id_contact) \
            and self.first_name == other.first_name and self.last_name == other.last_name

    def id_or_max(self):
        if self.id_contact:
            return int(self.id_contact)
        else:
            return maxsize

