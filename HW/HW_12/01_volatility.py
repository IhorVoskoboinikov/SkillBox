# -*- coding: utf-8 -*-


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от средней цены за торговую сессию:
#   средняя цена = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / средняя цена) * 100%
# Например для бумаги №1:
#   average_price = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / average_price) * 100 = 8.7%
# Для бумаги №2:
#   average_price = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / average_price) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
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
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base_source/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
import zipfile
import os
import itertools


class ExchangeTrading:

    def __init__(self, file):
        self.file_name = file
        self.tiker_volatility = {}
        self.tiker_volatility_zero = []
        self.sorted_dict_max = {}
        self.sorted_dict_min = {}

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for file_name in zfile.namelist():
            zfile.extract(file_name)
        self.file_name = file_name

    def run(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        for filename in os.listdir(self.file_name):
            # print(f"{'*' * 30}Читаем файл - {filename}")
            with open(os.path.join(self.file_name, filename), 'r') as file_name_to_check:
                self.general_calculations(file_name_to_check)
        self.calculating_the_min_and_max_values()
        self.calculation_output()

    def calculation_output(self):
        print('Максимальная волатильность:')
        for i, y in self.sorted_dict_max.items():
            q = i + " - " + str(y) + '%'
            print(f'{q: ^25}')
        print('Минимальная волатильность:')
        for i, y in self.sorted_dict_min.items():
            q = i + " - " + str(y) + '%'
            print(f'{q: ^25}')
        print(f"Нулевая волатильность:\n{', '.join(self.tiker_volatility_zero)}")

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
        if volatility == 0:
            self.tiker_volatility_zero.append(name_tiker)
        else:
            self.tiker_volatility[name_tiker] = round(volatility, 2)

    def calculating_the_min_and_max_values(self):
        sorted_values = sorted(self.tiker_volatility.values())
        max_values = sorted_values[-1:-4:-1]
        min_values = sorted_values[0:4]
        # print(min_values)
        for i in max_values:
            for k in self.tiker_volatility.keys():
                if self.tiker_volatility[k] == i:
                    self.sorted_dict_max[k] = self.tiker_volatility[k]
                    break
        for i in min_values:
            for k in self.tiker_volatility.keys():
                if self.tiker_volatility[k] == i:
                    self.sorted_dict_min[k] = self.tiker_volatility[k]
                    break


ticker = ExchangeTrading(file='trades')
ticker.run()

# написать код в однопоточном/однопроцессорном стиле
