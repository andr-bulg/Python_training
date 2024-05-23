"""
Создаём класс Group, в котором через инициализатор будут задаваться свойства
создаваемых объектов, чтобы затем в качестве параметров в другие методы
достаточно было передать ссылку на объект класса (параметр self).
"""

from sys import maxsize

class Group:

    def __init__(self, name=None, header=None, footer=None, id_group=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id_group = id_group

    def __repr__(self):
        return f"{self.id_group}:{self.name}:{self.header}:{self.footer}"

    def __eq__(self, other):
        return (self.id_group is None or other.id_group is None or self.id_group == other.id_group) \
            and self.name == other.name

    def id_or_max(self):
        if self.id_group:
            return int(self.id_group)
        else:
            return maxsize

