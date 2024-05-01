"""
Создаём класс Group, в котором через инициализатор будут задаваться свойства
создаваемых объектов, чтобы затем в качестве параметров в другие методы
достаточно было передать ссылку на объект класса (параметр self).
"""

class Group:

    def __init__(self, name=None, header=None, footer=None, id_group=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id_group = id_group

