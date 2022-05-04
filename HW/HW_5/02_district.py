# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

'''Вариант №1. Мой'''

from district.central_street.house1 import room1 as dcs_h1_r1
from district.central_street.house1 import room2 as dcs_h1_r2

from district.central_street.house2 import room1 as dcs_h2_r1
from district.central_street.house2 import room2 as dcs_h2_r2

from district.soviet_street.house1 import room1 as dss_h1_r1
from district.soviet_street.house1 import room2 as dss_h1_r2

from district.soviet_street.house1 import room1 as dss_h2_r1
from district.soviet_street.house1 import room2 as dss_h2_r2

# people = dcs_h1_r1.folks +\
#          dcs_h1_r2.folks +\
#          dcs_h2_r1.folks +\
#          dcs_h2_r2.folks +\
#          dss_h1_r1.folks +\
#          dss_h1_r2.folks +\
#          dss_h2_r1.folks +\
#          dss_h2_r2.folks
#
# print(f"В районе живут: {','.join(people)}")
# ============================================================================
"""Вариант №2. мой"""
people = str(dcs_h1_r1.folks +
             dcs_h1_r2.folks +
             dcs_h2_r1.folks +
             dcs_h2_r2.folks +
             dss_h1_r1.folks +
             dss_h1_r2.folks +
             dss_h2_r1.folks +
             dss_h2_r2.folks)

sheet_of_signs = ["'", "[", "]"]

for i in sheet_of_signs:
    people = people.replace(i, "")

print("В районе живет:", people)

"""Вариант решения от Вани"""
# result = ‘’
# for i, string in enumerate(strings_list):
#     result += string
#     if i < len(strings_list) - 1:  # если не последняя итерация
#         result += ‘,’
