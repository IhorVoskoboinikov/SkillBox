# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


class Water:

    def __init__(self):
        self.name = 'Вода'

    def __str__(self):
        return self.name

    def __add__(self, other):
        if self.name in GLOBAL_ELEMENTS:
            elements = GLOBAL_ELEMENTS[self.name]
            return elements.get(other.name, UnknownElement())
        else:
            elements = GLOBAL_ELEMENTS[other.name]
            return elements.get(self.name, UnknownElement())


class Air:

    def __init__(self):
        self.name = 'Воздух'

    def __str__(self):
        return self.name

    def __add__(self, other):
        if self.name in GLOBAL_ELEMENTS:
            elements = GLOBAL_ELEMENTS[self.name]
            return elements.get(other.name, UnknownElement())
        else:
            elements = GLOBAL_ELEMENTS[other.name]
            return elements.get(self.name, UnknownElement())


class Fire:

    def __init__(self):
        self.name = 'Огонь'

    def __str__(self):
        return self.name

    def __add__(self, other):
        if self.name in GLOBAL_ELEMENTS:
            elements = GLOBAL_ELEMENTS[self.name]
            return elements.get(other.name, UnknownElement())
        else:
            elements = GLOBAL_ELEMENTS[other.name]
            return elements.get(self.name, UnknownElement())


class Earth:

    def __init__(self):
        self.name = 'Земля'

    def __str__(self):
        return self.name

    def __add__(self, other):
        if self.name in GLOBAL_ELEMENTS:
            elements = GLOBAL_ELEMENTS[self.name]
            return elements.get(other.name, UnknownElement())
        else:
            elements = GLOBAL_ELEMENTS[other.name]
            return elements.get(self.name, UnknownElement())


class Storm:

    def __init__(self):
        self.name = 'Шторм'

    def __str__(self):
        return self.name

    def __add__(self, other):
        if self.name in GLOBAL_ELEMENTS:
            elements = GLOBAL_ELEMENTS[self.name]
            return elements.get(other.name, UnknownElement())
        else:
            elements = GLOBAL_ELEMENTS[other.name]
            return elements.get(self.name, UnknownElement())


class Steam:

    def __init__(self):
        self.name = 'Пар'

    def __str__(self):
        return self.name

    def __add__(self, other):
        if self.name in GLOBAL_ELEMENTS:
            elements = GLOBAL_ELEMENTS[self.name]
            return elements.get(other.name, UnknownElement())
        else:
            elements = GLOBAL_ELEMENTS[other.name]
            return elements.get(self.name, UnknownElement())


class Dirt:

    def __init__(self):
        self.name = 'Грязь'

    def __str__(self):
        return self.name

    def __add__(self, other):
        if self.name in GLOBAL_ELEMENTS:
            elements = GLOBAL_ELEMENTS[self.name]
            return elements.get(other.name, UnknownElement())
        else:
            elements = GLOBAL_ELEMENTS[other.name]
            return elements.get(self.name, UnknownElement())


class Lightning:

    def __init__(self):
        self.name = 'Молния'

    def __str__(self):
        return self.name

    def __add__(self, other):
        if self.name in GLOBAL_ELEMENTS:
            elements = GLOBAL_ELEMENTS[self.name]
            return elements.get(other.name, UnknownElement())
        else:
            elements = GLOBAL_ELEMENTS[other.name]
            return elements.get(self.name, UnknownElement())


class Dust:

    def __init__(self):
        self.name = 'Пыль'

    def __str__(self):
        return self.name

    def __add__(self, other):
        if self.name in GLOBAL_ELEMENTS:
            elements = GLOBAL_ELEMENTS[self.name]
            return elements.get(other.name, UnknownElement())
        else:
            elements = GLOBAL_ELEMENTS[other.name]
            return elements.get(self.name, UnknownElement())


class Lava:

    def __init__(self):
        self.name = 'Лава'

    def __str__(self):
        return self.name

    def __add__(self, other):
        if self.name in GLOBAL_ELEMENTS:
            elements = GLOBAL_ELEMENTS[self.name]
            return elements.get(other.name, UnknownElement())
        else:
            elements = GLOBAL_ELEMENTS[other.name]
            return elements.get(self.name, UnknownElement())


class UnknownElement:
    def __init__(self):
        self.name = 'Не известный элемент!'

    def __str__(self):
        return self.name

    def __add__(self, other):
        if self.name in GLOBAL_ELEMENTS:
            elements = GLOBAL_ELEMENTS[self.name]
            return elements.get(other.name, UnknownElement())
        else:
            elements = GLOBAL_ELEMENTS[other.name]
            return elements.get(self.name, UnknownElement())


GLOBAL_ELEMENTS = {
    "Вода": {
        "Воздух": Storm(),
        "Огонь": Steam(),
        "Земля": Dirt(),
    },
    "Воздух": {
        "Огонь": Lightning(),
        "Земля": Dust(),
    },
    "Огонь": {
        "Земля": Lava(),
        "Воздух": Lightning(),
        "Вода": Steam(),

    },
}

print(Water(), '+', Air(), '=', Water() + Air())
print(Water(), '+', Fire(), '=', Fire() + Water())
print(Water(), '+', Earth(), '=', Water() + Earth())
print(Air(), '+', Fire(), '=', Air() + Fire())
print(Air(), '+', Earth(), '=', Earth() + Air())
print(Fire(), '+', Earth(), '=', Earth() + Fire())

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новы
