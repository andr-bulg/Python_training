"""
Создаём класс Contact, в котором через инициализатор будут задаваться свойства
создаваемых объектов, чтобы затем в качестве параметров в другие методы
достаточно было передать ссылку на объект класса (параметр self).
"""

class Contact:

    def __init__(self, first_name=None, last_name=None, address=None, mobile_phone=None,
                 email=None, day=None, month=None, year=None, id_contact=None):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.mobile_phone = mobile_phone
        self.email = email
        self.day = day
        self.month = month
        self.year = year
        self.id_contact = id_contact

