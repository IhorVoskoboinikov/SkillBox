# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join


from district.central_street.house1 import room1 as dcs_h1_r1
from district.central_street.house1 import room2 as dcs_h1_r2

from district.central_street.house2 import room1 as dcs_h2_r1
from district.central_street.house2 import room2 as dcs_h2_r2

from district.soviet_street.house1 import room1 as dss_h1_r1
from district.soviet_street.house1 import room2 as dss_h1_r2

from district.soviet_street.house1 import room1 as dss_h2_r1
from district.soviet_street.house1 import room2 as dss_h2_r2

print(f"В районе живут:, {','.join(dcs_h1_r1.folks)},{','.join(dcs_h1_r2.folks)},{','.join(dcs_h2_r1.folks)},{','.join(dcs_h2_r2.folks)},"
      f"{','.join(dss_h1_r1.folks)},{','.join(dss_h1_r2.folks)},{','.join(dss_h2_r1.folks)},{','.join(dss_h2_r2.folks)},")


# people_in_the_area = []
# people_in_the_area = [
#                       dcs_h1_r1.folks +
#                       dcs_h1_r2.folks +
#                       dcs_h2_r1.folks +
#                       dcs_h2_r2.folks +
#                       dss_h1_r1.folks +
#                       dss_h1_r2.folks +
#                       dss_h2_r1.folks +
#                       dss_h2_r2.folks]



# people_in_the_area.append(dcs_h1_r1.folks)
# people_in_the_area.append(dcs_h1_r2.folks)
#
# people_in_the_area.append(dcs_h2_r1.folks)
# people_in_the_area.append(dcs_h2_r2.folks)
#
# people_in_the_area.append(dss_h1_r1.folks)
# people_in_the_area.append(dss_h1_r2.folks)
#
# people_in_the_area.append(dss_h2_r1.folks)
# people_in_the_area.append(dss_h2_r2.folks)
#
#
#
#
# print(f"В районе живут:{','.join(str(people_in_the_area))}")




