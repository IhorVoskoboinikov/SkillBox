# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

# TODO здесь ваш код

educational_grant = 10000
expenses = 12000
month = 0
difference = expenses - educational_grant
help_parent = 0

while month < 10:
    percent = difference * 0.03
    # print("Процент - ", percent)
    difference = difference + percent
    month += 1
    # print("Тело + % - ", difference)
    help_parent += difference
print("Помощь от родителей - ", round(help_parent))
# else:
#     print(round(2000 + difference))
