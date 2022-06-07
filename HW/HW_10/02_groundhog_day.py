# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

from random import randint

from termcolor import cprint

ENLIGHTENMENT_CARMA_LEVEL = 777


class IamGodError(BaseException):
    pass


class DrunkError(BaseException):
    pass


class CarCrashError(BaseException):
    pass


class GluttonyError(BaseException):
    pass


class DepressionError(BaseException):
    pass


class SuicideError(BaseException):
    pass


def one_day():
    global _karma
    choice = randint(1, 7)
    _karma += choice
    cprint('Игорь прожил еще один день', color='green')
    raise_choice = randint(1, 13)
    if raise_choice == 1:
        raise raise_list[randint(0, 5)]
    return _karma


raise_list = [IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError]
day = 0
_karma = 0

while _karma < ENLIGHTENMENT_CARMA_LEVEL:
    try:
        day += 1
        print(f'----------День № {day}-------------')
        one_day()
        cprint(f'Карма на сегодня = {_karma}', color='yellow')
    except IamGodError:
        cprint('Сегодня я бог', color='red')
    except DrunkError:
        cprint('Сегодня я бухаю', color='red')
    except CarCrashError:
        cprint('Сегодня я разбил машину', color='red')
    except GluttonyError:
        cprint('Сегодня я объедаюсь', color='red')
    except DepressionError:
        cprint('Сегодня я в Депрессии', color='red')
    except SuicideError:
        cprint('Сегодня я совершил самоубийство', color='red')
