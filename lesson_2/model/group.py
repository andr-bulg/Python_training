"""
Создаём класс Group, в котором через инициализатор будут задаваться свойства
создаваемых объектов, чтобы затем в качестве параметров в другие методы
достаточно было передать ссылку на объект класса (параметр self).
"""

class Group:

    def __init__(self, name, header, footer):
        self.name = name
        self.header = header
        self.footer = footer

