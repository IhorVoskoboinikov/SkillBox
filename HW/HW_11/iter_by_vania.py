from random import randint


class RandIntGenerator:

    def __init__(self, a, b, n):
        self.a = a
        self.b = b
        self.n = n
        self.i = 0
        self.random_list = []

    def __iter__(self):
        self.i = 0
        self.random_number()
        return self

    def __next__(self):
        if self.random_list[self.i] == self.n:
            print(f"Нашли {self.n}!")
            raise StopIteration()
        next_number = self.random_list[self.i]
        self.i += 1
        return next_number

    def random_number(self):
        self.random_list = []
        while True:
            number = randint(0, 10)
            self.random_list.append(number)
            if number == 5:
                break
        return self.random_list


iterator = RandIntGenerator(a=0, b=10, n=5)
for number in iterator:
    print(number)
