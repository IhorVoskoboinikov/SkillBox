# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

class ReadFileParser:

    def __init__(self, file_for_analysis, result_file):
        self.file_name = file_for_analysis
        self.result_file = result_file
        self.file_to_write = {}
        self.sort_file_to_write = []

    def read_file(self):
        with open(self.file_name, 'r', encoding='utf-8') as file:
            self.sort_file(file)

    def sort_file(self, file):
        for line in file:
            if line.endswith('NOK\n'):
                if line[1:17] in self.file_to_write:
                    self.file_to_write[line[1:17]] += 1
                else:
                    self.file_to_write[line[1:17]] = 1
        self.sort_file_to_write = sorted(self.file_to_write.items())

    def write_file(self):
        with open(self.result_file, 'w', encoding='utf-8') as file:
            for i, y in self.sort_file_to_write:
                file.write('[' + i + ']' + '  -  ' + str(y) + '\n')


parser = ReadFileParser(file_for_analysis='events.txt', result_file='result.txt')
parser.read_file()
parser.write_file()
print(parser.file_to_write)
# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
