"""
Создаём класс Account, в котором через инициализатор будут задаваться свойства
создаваемых объектов, чтобы затем в качестве параметров в другие методы
достаточно было передать ссылку на объект класса (параметр self).
"""

class Contact:

    def __init__(self, first_name, last_name, address, mobile_phone, email, day, month, year):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.mobile_phone = mobile_phone
        self.email = email
        self.day = day
        self.month = month
        self.year = year



