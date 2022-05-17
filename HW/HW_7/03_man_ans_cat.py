# -*- coding: utf-8 -*-


# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

from random import randint
from termcolor import cprint, colored


class Men:
    def __init__(self, name):
        self.name = name
        self.satiety = 10
        self.power = 50
        self.love_cat = 20
        self.house = None

    def __str__(self):
        return colored(f"Я - {self.name}, "
                       f"сытость  = {self.satiety}, "
                       f"сила = {self.power}, "
                       f"любовь кота = {self.love_cat},"
                       f"деньги = {self.house.money}", color='blue')

    def workout_in_the_gym(self):
        if self.satiety >= 50:
            self.power += 50
            self.satiety -= 20
            cprint(f"{self.name} хорошо потренировался!!!!", color='blue')
        else:
            cprint(f"{self.name} не хватает сил на тренировку, пойду поем!", color='blue')
            self.eat()

    def eat(self):
        self.satiety += 20
        self.house.food -= 20
        cprint(f"{self.name} покушал вкусняху!", color='blue')

    def playing_with_a_cat(self):
        self.power -= 10
        self.love_cat += 20
        cprint(f"{self.name} поиграл с котом!", color='blue')

    def go_to_shop(self):
        if self.house.money <= 10:
            cprint(f"{self.name} нет денег! Нужно сходить на работу!", color='blue')
            self.work()
        else:
            cprint(f"{self.name} сходил в магазин купил продуктов и корм коту", color='blue')
            self.house.money -= 50
            self.power -= 5
            self.house.food += 20
            self.house.cat_food += 20


    def work(self):
        self.power -= 20
        self.satiety -= 20
        self.love_cat -= 50
        self.house.money += 150
        cprint(f"{self.name} сходил на работу!", color='blue')

    def move_into_the_house(self, house):
        self.house = house
        cprint(f"{self.name} купил дом!", color='blue')

    def bay_eat_from_cat(self):
        self.house.cat_food += 50
        self.house.money -= 50
        cprint(f"{self.name} купил коту Вискас!", color='blue')

    def clean_the_house(self):
        self.house.dirt_in_the_house -= 100
        self.power -= 10
        self.satiety -= 20
        cprint(f"{self.name} убрал весь дом!", color='blue')

    def live(self):
        if self.satiety <= 0:
            cprint(f"{self.name} умер!", color='red')
            return
        if self.house.cat_food <= 20:
            self.go_to_shop()
        step = randint(1, 6)
        if self.satiety <= 20:
            self.eat()
        elif self.house.money <= 10:
            self.work()
        elif self.love_cat <= 10:
            self.playing_with_a_cat()
        elif self.power <= 10:
            self.workout_in_the_gym()
        elif self.house.dirt_in_the_house >= 100:
            self.clean_the_house()
        elif step == 1:
            self.workout_in_the_gym()
        elif step == 2:
            self.eat()
        elif step == 3:
            self.playing_with_a_cat()
        elif step == 4:
            self.work()
        else:
            self.go_to_shop()


class Cat:
    def __init__(self, name):
        self.name = name
        self.cat_satiety = 0
        self.house = None

    def __str__(self):
        return colored(f"Кот - {self.name}, сытость (кота)  = {self.cat_satiety}", color='green')

    def cat_sleep(self):
        self.cat_satiety -= 10
        cprint(f"Кот - {self.name} поспал!", color='green')

    def cat_eat(self):
        self.cat_satiety += 20
        self.house.cat_food -= 20
        cprint(f"Кот - {self.name} поел корм!", color='green')

    def cat_fights_wallpaper(self):
        self.cat_satiety -= 20
        self.house.dirt_in_the_house += 5
        cprint(f"Кот - {self.name} подрал обои в доме!", color='green')

    def move_into_the_house(self, house):
        self.house = house
        cprint(f"Кот - {self.name} нашел дом!", color='blue')

    def live(self):
        if self.cat_satiety <= 20:
            self.cat_eat()
        if self.cat_satiety <= 0:
            cprint(f"{self.name} умер!", color='red')
            return
        step = randint(1, 4)
        if step == 1:
            self.cat_eat()
        elif step == 2:
            self.cat_sleep()
        elif step == 3:
            self.cat_fights_wallpaper()


class OurHouse:

    def __init__(self):
        self.dirt_in_the_house = 0  # грязь в доме
        self.money = 0
        self.food = 0
        self.cat_food = 0

    def __str__(self):
        return colored(f"В доме осталось: денег - {self.money}, еда человека  = {self.food},"
                       f"еда кота = {self.cat_food}, чистота в доме = {self.dirt_in_the_house}", color='yellow')


citizens = [
    Men(name='Игорь'),
    Cat(name='Борис'),
]

my_favorite_house = OurHouse()

for citizen in citizens:
    citizen.move_into_the_house(house=my_favorite_house)

for day in range(1, 366):
    print(f"-----------День № {day} - утро----------")
    for citisen in citizens:
        citisen.live()
    print('------------ в конце дня --------------')
    for citisen in citizens:
        print(citisen)
    print(my_favorite_house)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
