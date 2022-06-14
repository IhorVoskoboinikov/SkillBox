from random import randint


class RandIntGenerator:

    def __init__(self, a, b, n):
        self.a = a
        self.b = b
        self.n = n

    def __iter__(self):
        self.n_found = False
        return self

    def __next__(self):
        if self.n_found:
            print(f"Нашли {self.n }")
            raise StopIteration()
        generated = randint(self.a, self.b)
        if generated == self.n:
            self.n_found = True
        return generated


# iterator = RandIntGenerator(a=0, b=10, n=5)
# for number in iterator:
#     print(number)

iterator = RandIntGenerator(a=0, b=10, n=5)
for number in iterator:
    print(number)

for number in iterator:
    print(number)
