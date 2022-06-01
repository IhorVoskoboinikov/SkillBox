class ReadFileParser:

    def __init__(self, file_for_analysis, result_file, aggregation_by):
        self.aggregation_by = aggregation_by
        self.file_name = file_for_analysis
        self.result_file = result_file
        self.file_to_write = {}
        self.sort_file_to_write = []

    def read_file(self):
        with open(self.file_name, 'r', encoding='utf-8') as file:
            self.sort_file_for_time(file)

    def sort_file(self, file):
        for line in file:
            if line.endswith('NOK\n'):
                if line[1:17] in self.file_to_write:
                    self.file_to_write[line[1:17]] += 1
                else:
                    self.file_to_write[line[1:17]] = 1
        self.sort_file_to_write = sorted(self.file_to_write.items())

    def write_file(self):
        if self.sort_file_to_write:
            with open(self.result_file, 'w', encoding='utf-8') as file:
                for i, y in self.sort_file_to_write:
                    file.write('[' + i + ']' + '  -  ' + str(y) + '\n')
        else:
            raise RuntimeError('Нет данных по данному запросу!')

    def sort_file_for_time(self, file):
        for line in file:
            if line.endswith('NOK\n'):
                if self.aggregation_by in line:
                    if line[1:17] in self.file_to_write:
                        self.file_to_write[line[1:17]] += 1
                    else:
                        self.file_to_write[line[1:17]] = 1
        self.sort_file_to_write = sorted(self.file_to_write.items())


parser = ReadFileParser(file_for_analysis='events.txt', result_file='result.txt', aggregation_by='2018-05-10')
parser.read_file()
parser.write_file()
print(parser.file_to_write)
# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
