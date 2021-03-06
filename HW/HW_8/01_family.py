# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.

class Human:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.satiety = 30  # сытость
        self.happiness = 100  # уровень счастья

    def __str__(self):
        return f'{self.name}: сытость = {self.satiety}, уровень счастья = {self.happiness}'

    def pet_the_cat(self):
        self.happiness += 5
        print(f'{self.name} - погладил кота!')


class House:
    total_food = 0

    def __init__(self):
        self.money_in_the_nightstand = 100  # деньги в тумбочке
        self.food_in_the_fridge = 50  # еда в холодильнике
        self.dirt_in_the_house = 0  # грязь в доме
        self.food_for_cat = 30

    def __str__(self):
        return f'В доме: деньги = {self.money_in_the_nightstand}, еда = {self.food_in_the_fridge},' \
               f' чистота (грязь) = {self.dirt_in_the_house}, еда кота = {self.food_for_cat}'


class Husband(Human):
    total_money = 0

    def act(self):
        if self.satiety <= 0:
            cprint(f'{self.name} - УМЕР!', color='red')
            return
        if self.happiness <= 10:
            cprint(f'{self.name} - УМЕР от депрессии!', color='red')
            return
        if self.house.dirt_in_the_house >= 80:
            self.happiness -= 10
        if self.satiety <= 10:
            self.eat()
        elif self.happiness <= 20:
            self.gaming()
        else:
            self.work()
            Husband.total_money += 150

    def eat(self):
        food = randint(20, 31)
        self.house.food_in_the_fridge -= food
        self.satiety += food
        House.total_food += food
        cprint(f'{self.name} вкусно поел! Всего съел = {food}')

    def work(self):
        self.satiety -= 10
        self.house.money_in_the_nightstand += 150
        cprint(f'{self.name} сходил на работу!')

    def gaming(self):
        self.satiety -= 10
        self.happiness += 20
        cprint(f'{self.name} поиграл в Мир Танков по сети!')


class Wife(Human):
    total_fur_coats = 0

    def eat(self):
        food = randint(20, 31)
        self.house.food_in_the_fridge -= food
        self.satiety += food
        House.total_food += food
        cprint(f'{self.name} вкусно поела! Всего съела = {food}')

    def shopping(self):
        amount_of_food = 70
        self.house.money_in_the_nightstand -= amount_of_food
        self.house.food_in_the_fridge += amount_of_food
        self.satiety -= 10
        cprint(f'{self.name} сходила в магазин за едой!Купила еды = {amount_of_food}')

    def buy_fur_coat(self):
        self.satiety -= 10
        self.house.money_in_the_nightstand -= 350
        self.happiness += 60
        Wife.total_fur_coats += 1
        cprint(f'{self.name} купила норковую шубу! за 350 грн')

    def clean_house(self):
        cleaning = randint(75, 101)
        self.house.dirt_in_the_house -= cleaning
        self.satiety -= 10
        cprint(f'{self.name} поубирала в доме! на {cleaning} ед.')

    def by_eat_for_cat(self):
        self.house.food_for_cat += 10
        self.house.money_in_the_nightstand -= 10
        cprint(f'{self.name} купила еду коту!')

    def act(self):
        if self.satiety <= 0:
            cprint(f'{self.name} - УМЕРЛА!', color='red')
            return
        if self.happiness <= 10:
            cprint(f'{self.name} - УМЕРЛА от дипресии!', color='red')
            return
        if self.house.dirt_in_the_house >= 80:
            self.happiness -= 10
        if self.satiety <= 10:
            self.eat()
        elif self.happiness <= 20:
            self.buy_fur_coat()
        elif self.house.food_in_the_fridge <= 30:
            self.shopping()
        elif self.house.dirt_in_the_house >= 100:
            self.clean_house()
        elif self.house.food_for_cat <= 10:
            self.by_eat_for_cat()
        else:
            self.satiety -= 10
            print(f'{self.name} сижу нифига не делаю)))')


class Child(Human):

    def act(self):
        if self.satiety <= 0:
            cprint(f'{self.name} - УМЕР', color='red')
            return
        if self.satiety <= 10:
            self.eat()
        else:
            self.sleep()

    def eat(self):
        food = randint(1, 11)
        self.house.food_in_the_fridge -= food
        self.satiety += food
        House.total_food += food
        cprint(f'{self.name} вкусно поел! Всего съел = {food}')

    def sleep(self):
        self.satiety -= 10
        cprint(f'{self.name} поспал')


class Cat:

    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.satiety = 30

    def __str__(self):
        return f'Кот {self.name}: сытость = {self.satiety}'

    def act(self):
        if self.satiety <= 0:
            cprint(f'{self.name} - УМЕР!', color='red')
            return
        choice = randint(1, 3)
        if self.satiety <= 10:
            self.eat()
        elif choice == 1:
            self.sleep()
        else:
            self.soil()

    def eat(self):
        amount_of_cat_food = randint(1, 11)
        self.house.food_for_cat -= amount_of_cat_food
        self.satiety += (amount_of_cat_food * 2)
        print(f'{self.name} поел!')

    def sleep(self):
        self.satiety -= 10
        print(f'{self.name} поспал!')

    def soil(self):  # драть обои
        self.satiety -= 10
        self.house.dirt_in_the_house += 5
        print(f'{self.name} подрал обои!')


home = House()
ihor = Husband(name='Игорь', house=home)
natasha = Wife(name='Наташа', house=home)
roma = Child(name='Рома', house=home)
cat_timka = Cat(name='Тимка', house=home)

for day in range(1, 365):
    cprint(f'================== День {day} ==================', color='red')
    home.dirt_in_the_house += 10
    ihor.act()
    natasha.act()
    roma.act()
    cat_timka.act()
    cprint(ihor, color='cyan')
    cprint(natasha, color='cyan')
    cprint(roma, color='cyan')
    cprint(cat_timka, color='cyan')
    cprint(home, color='green')

cprint(f'Муж заработал всего денег - {Husband.total_money}', color='blue')
cprint(f'Жена купила всего шуб - {Wife.total_fur_coats}', color='blue')
cprint(f'Всего сьели еды - {House.total_food}', color='blue')

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:+++++
#   есть,+++
#   спать,+++
#   драть обои+++
#
# Люди могут:+++
#   гладить кота (растет степень счастья на 5 пунктов)+++
#
# В доме добавляется:
#   еда для кота (в начале - 30)+++
#
# У кота есть имя и степень сытости (в начале - 30)+++
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов+++
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов

#
# class Cat:
#
#     def __init__(self):
#         pass
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass
#
#     def soil(self):
#         pass


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

# class Child:
#
#     def __init__(self):
#         pass
#
#     def __str__(self):
#         return super().__str__()
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass
#
#

######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
