# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
import threading
import zipfile
import os
import itertools


class ExchangeTrading(threading.Thread):

    def __init__(self, file, folder, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.folder = folder
        self.file_name = file
        self.tiker_volatility = {}
        self.sorted_volatility_zero = []
        self.sorted_list_max = []
        self.sorted_list_min = []

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for file_name in zfile.namelist():
            zfile.extract(file_name)
        self.file_name = file_name

    def run(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        # for file_name in os.listdir(self.folder):
        # while self.file_name:
        print(f"{'*' * 30}Читаем файл - {self.file_name}")
        with open(os.path.join(self.folder, self.file_name), 'r') as file_name_to_check:
            self.general_calculations(file_name_to_check)
        self.calculating_the_min_and_max_values()
        self.sorted_volatility_zero = sorted(self.sorted_volatility_zero)
        self.calculation_output()

    def calculation_output(self):
        print('Максимальная волатильность:')
        for i, y in self.sorted_list_max:
            q = y + " - " + str(i) + '%'
            print(f'{q: ^25}')
        print('Минимальная волатильность:')
        for i, y in self.sorted_list_min:
            q = y + " - " + str(i) + '%'
            print(f'{q: ^25}')
        print(f"Нулевая волатильность:\n{', '.join(self.sorted_volatility_zero)}")

    def general_calculations(self, file_name_to_check):
        prices_in_file = list()
        for line in itertools.islice(file_name_to_check, 1, None):
            # print(line)
            if line.endswith('\n'):
                line = line[:-1]
            ticers = line.split(',')
            if len(ticers) != 4:
                raise ValueError('Не все поля заполнены')
            name_tiker, transaction_time, price, quantuty = ticers
            price = float(price)
            # print(price)
            prices_in_file.append(price)
        average_price = (max(prices_in_file) + min(prices_in_file) / 2)
        volatility = ((max(prices_in_file) - min(prices_in_file)) / average_price) * 100
        self.calculating_zero_values(name_tiker, volatility)

    def calculating_zero_values(self, name_tiker, volatility):
        if volatility == 0:
            self.sorted_volatility_zero.append(name_tiker)
        else:
            self.tiker_volatility[name_tiker] = round(volatility, 2)

    def calculating_the_min_and_max_values(self):
        sorted_tickers = sorted([(volatility, tiker_name) for tiker_name, volatility in self.tiker_volatility.items()])
        self.sorted_list_max = [x for x in sorted_tickers[-1:-4:-1]]
        self.sorted_list_min = [x for x in sorted_tickers[2::-1]]


# ticker = ExchangeTrading(file='trades')
# ticker.run()

def main():
    # tickers = [ExchangeTrading(file=filename) for filename in os.listdir('trades')]
    tickers = [ExchangeTrading(file=filename, folder='trades') for filename in os.listdir('trades')]
    print(tickers)

    for ticker in tickers:
        ticker.start()
    for ticker in tickers:
        ticker.join()


if __name__ == '__main__':
    main()
