# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

class LogParser:

    def __init__(self, file_for_analysis):
        self.file_name = file_for_analysis

    def __iter__(self):
        self.file_to_write = {}
        self.sort_file_to_write = []
        self.read_file()
        self.i = -1
        return self

    def __next__(self):
        self.i += 1
        if self.i < len(self.sort_file_to_write):
            return self.sort_file_to_write[self.i]
        raise StopIteration()

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


grouped_events = LogParser(file_for_analysis='events.txt')
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')
