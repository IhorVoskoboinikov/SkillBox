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

class FindNumberOfLetters:
    alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У',
                'Ф',
                'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и',
                'й',
                'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю',
                'я']

    def __init__(self, file_name):
        self.file_name = file_name
        self.statistic = {}
        self.total_quantity = 0

    def open_file_statistic(self):
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for elem in line:
                    if elem in self.alphabet:
                        if elem in self.statistic:
                            self.statistic[elem] += 1
                        else:
                            self.statistic[elem] = 1


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

    def sorted_statistic(self):
        for letter, quantity in sorted(self.statistic.items()):
            self.total_quantity += quantity
            print(f'|{letter: ^10}|{quantity: ^10}|')


my_statistic = FindNumberOfLetters(file_name='voyna-i-mir.txt')
my_statistic.open_file_statistic()
my_statistic.create_table_header()
my_statistic.sorted_statistic()
my_statistic.create_table_end()


# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
