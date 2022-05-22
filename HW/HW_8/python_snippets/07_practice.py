# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint


# Реализуем модель доставки грузов

# Дорога - хранит расстояния между обьектами
# Склад - хранит груз и управляет очередями грузовиков

# Базовый класс - Машина,
# имеет
#   кол-во топлива
# может
#   заправляться

# Грузовик (производный от Машина)
# имеет
#   емкость кузова, скорость движения, расход топлива за час поездки
# может
#   стоят под погрузкой/разгрузкой
#   ехать со скоростью

# Погрузчик (производный от Машина)
# имеет
#   скорость погрузки, расход топлива в час при работе
# может
#   загружать/разгружать грузовик
#   ждать грузовик


class Road:
    def __init__(self, start, end, distance):
        self.start = start
        self.end = end
        self.distance = distance


class Werehouse:

    def __init__(self, name, content=0):
        self.name = name
        self.content = content
        self.road_out = None
        self.queue_in = []
        self.queue_out = []

    def __str__(self):
        return f'Склад - {self.name} , Груз - {self.content}'

    def set_road_out(self, road):
        self.road_out = road

    def truck_arrived(self, truck):
        self.queue_in.append(truck)
        truck.place = self
        print(f'{self.name}, прибыл грузовик - {truck}')

    def get_next_truck(self):
        if self.queue_in:
            truck = self.queue_in.pop()
            return truck

    def truck_ready(self, truck):
        self.queue_out.append(truck)
        print(f'{self.name}, грузовик готов - {truck}')

    def act(self):
        while self.queue_out:
            truck = self.queue_out.pop()
            truck.go_to(road=self.road_out)


class Wehicle:
    fuel_rate = 0
    total_fuel = 0

    def __init__(self, model):
        self.model = model
        self.fuel = 0

    def __str__(self):
        return f'{self.model}, топлива = {self.fuel}'

    def tank_up(self):
        self.fuel += 1000
        Wehicle.total_fuel += 1000
        print(f'{self.model}, заправился')

    def act(self):
        if self.fuel <= 10:
            self.tank_up()
            return False
        return True


class Truck(Wehicle):
    fuel_rate = 50
    dead_time = 0

    def __init__(self, model, body_space=1000):
        super().__init__(model=model)
        self.body_space = body_space
        self.cargo = 0
        self.velocity = 100
        self.place = None
        self.distance_to_target = 0

    def __str__(self):
        res = super().__str__()
        return res + f' груза = {self.cargo}'

    def ride(self):
        self.fuel -= self.fuel_rate
        if self.distance_to_target > self.velocity:
            self.distance_to_target -= self.velocity
            print(f'Еду по дороге - {self.model}, осталось =  {self.distance_to_target}')
        else:
            self.place.end.truck_arrived(self)
            print(f'{self.model} приехал')

    def go_to(self, road):
        self.distance_to_target = road.distance
        self.place = road
        print(f'Еду по дороге {self.model}')

    def act(self):
        if super().act():
            if isinstance(self.place, Road):
                self.ride()
            else:
                Truck.dead_time += 1

class BigTruck(Truck):
    fuel_rate = 100


class Autoloader(Wehicle):
    fuel_rate = 30
    dead_time = 0


    def __init__(self, model, bucket_capacity=100, warehouse=None, role='loader'):
        super().__init__(model=model)
        self.bucket_capacity = bucket_capacity
        self.warehouse = warehouse
        self.role = role
        self.truck = None

    def __str__(self):
        res = super().__str__()
        return res + f' Грузим = {self.truck}'

    def act(self):
        if super().act():
            if self.truck is None:
                self.truck = self.warehouse.get_next_truck()
                if self.truck is None:
                    print(f'{self.model} нет грузовиков для работы')
                    Autoloader.dead_time += 1
                else:
                    print(f'{self.model} взял в работу - {self.truck}')
            elif self.role == 'loader':
                self.load()
            else:
                self.unload()

    def load(self):
        if self.warehouse.content == 0:
            print(f'{self.model} на складе ничего не было')
            if self.truck:
                self.warehouse.truck_ready(self.truck)
                self.truck = None
            return
        self.fuel -= self.fuel_rate
        truck_cargo_rest = self.truck.body_space - self.truck.cargo
        if truck_cargo_rest >= self.bucket_capacity:
            cargo = self.bucket_capacity
        else:
            cargo = truck_cargo_rest
        if self.warehouse.content < cargo:
            cargo = self.warehouse.content
        self.warehouse.content -= cargo
        self.truck.cargo += cargo

        print(f'{self.model} грузил - {self.truck}')
        if self.truck.cargo == self.truck.body_space:
            self.warehouse.truck_ready(self.truck)
            self.truck = None

    def unload(self):
        self.fuel -= self.fuel_rate
        if self.truck.cargo >= self.bucket_capacity:
            self.truck.cargo -= self.bucket_capacity
            self.warehouse.content += self.bucket_capacity
        else:
            self.truck.cargo -= self.truck.cargo
            self.warehouse.content += self.truck.cargo
            print(f'{self.model} разгружал - {self.truck}')
        if self.truck.cargo == 0:
            self.warehouse.truck_ready(self.truck)
            self.truck = None


TOTAL_CARGO = 100000

moskow = Werehouse(name='Москва', content=TOTAL_CARGO)
piter = Werehouse(name='Питер', content=0)

moskov_piter = Road(start=moskow, end=piter, distance=715)
piter_moskow = Road(start=piter, end=moskow, distance=780)

moskow.set_road_out(road=moskov_piter)
piter.set_road_out(road=piter_moskow)

loader_1 = Autoloader(model='Bobcat', bucket_capacity=1000, warehouse=moskow, role='loader')
loader_2 = Autoloader(model='LongKing', bucket_capacity=500, warehouse=piter, role='unloader')

trucks = []
for number in range(1, 6):
    truck = Truck(model=f'Камаз # {number}', body_space=5000)
    moskow.truck_arrived(truck)
    trucks.append(truck)

for number in range(1, 6):
    truck = BigTruck(model=f'DAF # {number}', body_space=10000)
    moskow.truck_arrived(truck)
    trucks.append(truck)


hour = 0

while piter.content < TOTAL_CARGO:
    hour += 1
    cprint(f'Время = {hour} час(ов)------------------', color='green')
    for truck in trucks:
        truck.act()
    loader_1.act()
    loader_2.act()
    moskow.act()
    piter.act()
    for truck in trucks:
        cprint(truck, color='red')
    cprint(loader_1, color='yellow')
    cprint(loader_2, color='yellow')
    cprint(moskow, color='grey')
    cprint(piter, color='grey')

cprint(f'Всего затраченно топлива {Wehicle.total_fuel}', color="green")
cprint(f'Общий простой грузовиков {Truck.dead_time}', color="green")
cprint(f'Общий простой автопогрузчиков {Autoloader.dead_time}', color="green")