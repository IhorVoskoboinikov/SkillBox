import threading
import os
import itertools


class ExchangeTrading(threading.Thread):

    def __init__(self, directory, file, lock, tiker_volatility,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_name = file
        self.directory = directory
        self.lock = lock
        self.tiker_volatility = tiker_volatility


    def run(self):
        with open(os.path.join(self.directory, self.file_name), 'r') as file_name_to_check:
            prices_in_file = list()
            for line in itertools.islice(file_name_to_check, 1, None):
                if line.endswith('\n'):
                    line = line[:-1]
                ticers = line.split(',')
                if len(ticers) != 4:
                    raise ValueError('Не все поля заполнены')
                name_tiker, transaction_time, price, quantuty = ticers
                price = float(price)
                prices_in_file.append(price)
            average_price = (max(prices_in_file) + min(prices_in_file) / 2)
            volatility = ((max(prices_in_file) - min(prices_in_file)) / average_price) * 100
            with self.lock:
                self.tiker_volatility[name_tiker] = round(volatility, 2)


def calculation_output(sorted_list_max, sorted_list_min, sorted_volatility_zero):
    print('Максимальная волатильность:')
    for i, y in sorted_list_max:
        q = y + " - " + str(i) + '%'
        print(f'{q: ^25}')
    print('Минимальная волатильность:')
    for i, y in sorted_list_min:
        q = y + " - " + str(i) + '%'
        print(f'{q: ^25}')
    print(f"Нулевая волатильность:\n{', '.join(sorted_volatility_zero)}")


def calculating_the_min_zero_max_values(tiker_volatility):
    for name_tiker, volatility in tiker_volatility.items():
        if volatility == 0:
            sorted_volatility_zero.append(name_tiker)
        else:
            sorted_volatility[name_tiker] = volatility
        sorted_tickers = sorted([(volatility, tiker_name) for tiker_name, volatility in sorted_volatility.items()])
        global sorted_list_max, sorted_list_min
        sorted_list_max = [x for x in sorted_tickers[-1:-4:-1]]
        sorted_list_min = [x for x in sorted_tickers[2::-1]]


tiker_volatility = {}
sorted_volatility = {}
sorted_volatility_zero = []
sorted_list_max = []
sorted_list_min = []


def main():
    lock = threading.Lock()
    tickers = [ExchangeTrading(file=filename, directory='trades', lock=lock, tiker_volatility=tiker_volatility) for filename in os.listdir('trades')]

    for ticker in tickers:
        ticker.start()
    for ticker in tickers:
        ticker.join()
    calculating_the_min_zero_max_values(tiker_volatility=tiker_volatility)
    calculation_output(sorted_list_max=sorted_list_max, sorted_list_min=sorted_list_min,
                       sorted_volatility_zero=sorted_volatility_zero)


if __name__ == '__main__':
    main()