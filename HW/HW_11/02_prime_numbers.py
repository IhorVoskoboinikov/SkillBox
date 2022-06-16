# -*- coding: utf-8 -*-
from random import randint


# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик

#
# class PrimeNumbers:
#
#     def __init__(self, n):
#         self.n = n
#         self.i = 0
#         self.prime_numbers = []
#
#     def __iter__(self):
#         self.i = 0
#         self.get_prime_numbers()
#         return self
#
#     def __next__(self):
#         if self.i >= len(self.prime_numbers):
#             raise StopIteration()
#         next_prime = self.prime_numbers[self.i]
#         self.i += 1
#         return next_prime
#
#     def get_prime_numbers(self):
#         self.prime_numbers = []
#         for number in range(2, self.n + 1):
#             for prime in self.prime_numbers:
#                 if number % prime == 0:
#                     break
#             else:
#                 self.prime_numbers.append(number)
#         return self.prime_numbers
#
#
# prime_number_iterator = PrimeNumbers(n=10000)
# for number in prime_number_iterator:
#     print(number)


# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


# def prime_numbers_generator(n):
#     prime_numbers = []
#     for number in range(2, n + 1):
#         for prime in prime_numbers:
#             if number % prime == 0:
#                 break
#         else:
#             prime_numbers.append(number)
#             yield number
#
#
# print(prime_numbers_generator(n=100))
# for number in prime_numbers_generator(n=100):
#     print(number)

# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.

def lucky_number(numbers):
    for number in numbers:
        number = str(number)
        n = len(number)
        a = sum(map(int, number[:n // 2]))
        b = sum(map(int, number[n // 2 + n % 2:]))
        if n < 2:
            continue
        if a == b:
            print(number)
    else:
        print('Счастливые номера закончились')


# Первичный результат для четных:
# a = sum(int(x) for x in number[0:(int((len(number))/2))])
# b = sum(int(x) for x in number[(int((len(number))/2)):])
# Первичный результат для нечетных:
# a = sum(int(x) for x in number[0:(int((len(number))/2))])
# b = sum(int(x) for x in number[(int((len(number))/2)+1):])

def polysyndromic_number(numbers):
    # print(numbers)
    for number in numbers:
        number = str(number)
        n = len(number)
        if len(number) < 2:
            continue
        if number[0:(n//2)] == number[-1:((n//2)-1):-1]:
            print(number)
    else:
        print('Палиндромные номера закончились')

# test = [i for i in range(1, 10000)]
l_n = get_prime_numbers(n=10000)
p_n = get_prime_numbers(n=10000)
lucky_number(l_n)
polysyndromic_number(p_n)

