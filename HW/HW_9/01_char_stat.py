# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
from collections import defaultdict

class FindNumberOfLetters:

    def __init__(self, file_name):
        self.file_name = file_name
        self.total_quantity = 0
        self.statistic = {}
        self.sort_statistic = []
        # self.statistic = defaultdict(int) #  вариант при использовании импорта

    def open_file_statistic(self):
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for elem in line:
                    if elem.isalpha():
                        if elem in self.statistic:
                            self.statistic[elem] += 1
                        else:
                            self.statistic[elem] = 1
            self.sort_statistic = sorted(self.statistic.items())
            # for elem in line: #  вариант если мы используем импорт
            #     if 'а' <= elem.lower() <= 'я':
            #         self.statistic[elem] += 1

    def create_table_header(self):
        plus = '+'
        letter = 'буква'
        ch = 'частота'
        table_header = (f'+{plus:-^21}+\n'
                        f'|{letter: ^10}|{ch: ^10}|\n'
                        f'+{plus:-^21}+')
        print(table_header)

    def create_table_end(self):
        plus = '+'
        total = 'итого'
        table_totals = (f'+{plus:-^21}+\n'
                        f'|{total: ^10}|{self.total_quantity: ^10}|\n'
                        f'+{plus:-^21}+')
        print(table_totals)

    def sort_statistic_for_alphabet(self):  # сортировка по алфавиту по убыванию
        self.total_quantity = 0
        self.create_table_header()
        for letter, quantity in self.sort_statistic:
            self.total_quantity += quantity
            print(f'|{letter: ^10}|{quantity: ^10}|')
        self.create_table_end()

    def sort_ascending(self):  # сортировка по алфавиту по возрастанию
        total_quantity = 0
        self.create_table_header()
        for letter, quantity in reversed(self.sort_statistic):
            total_quantity += quantity
            print(f'|{letter: ^10}|{quantity: ^10}|')
        self.create_table_end()

    def sort_by_frequency_of_use(self):  # сортировка по частоте по убыванию
        self.total_quantity = 0
        self.create_table_header()
        sorted_value = sorted(self.statistic.values())
        new_sort_statistic = {}
        for i in sorted_value:
            for k in self.statistic.keys():
                if self.statistic[k] == i:
                    new_sort_statistic[k] = self.statistic[k]
                    break
        for letter, quantity in reversed(new_sort_statistic.items()):
            self.total_quantity += quantity
            print(f'|{letter: ^10}|{quantity: ^10}|')
        self.create_table_end()


my_statistic = FindNumberOfLetters(file_name='voyna-i-mir.txt')
my_statistic.open_file_statistic()
my_statistic.sort_statistic_for_alphabet()
my_statistic.sort_ascending()
my_statistic.sort_by_frequency_of_use()

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
