def bun(stage):
    if stage == 1:
        print("Берем одну булочку и режим ее на две половины, берем одну половину")
    else:
        print("Финальный штрих - накрываем второй половиной булочки\nЧисбургер готов!!!")


def cutlet():
    print("Добавляем котлету сверху")


def cucumber():
    print("Добавляем нарезаный слайсами огурец (3-4 шт)")


def tomato():
    print("Добавляем нарезаный слайсами помидор (1-2 шт)")


def mayonnaise():
    print("Добавляем майонез")


def cheese():
    print("Добавляем ломтик сыра")


def cooking_a_cheeseburger():
    bun(stage=1)
    mayonnaise()
    cucumber()
    tomato()
    cutlet()
    cheese()
    bun(stage=2)
