from random import randint


class RandIntGenerator:

    def __init__(self, a, b, n):
        self.a = a
        self.b = b
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        while self.n:
            random_number = randint(self.a, self.b)
            if random_number == self.n:
                self.n = False
                return random_number
            return random_number
        print(f"Нашли!")
        raise StopIteration()


iterator = RandIntGenerator(a=0, b=200, n=5)
for number in iterator:
    print(number)
