from bouling_engine import Bowling

errors = {
    'TypeError': 'Полученный данные не строка.Вы ввели - ',
    'IndexError': 'Длинна строки данных должна быть от 10 до 20 символов. Длинна вашей строки = ',
    'ValueError': "Не правильный данные. Допустимые значения: от '1' до '9', 'X', '-', '/'. Не правильные значение -"
}


def data_validation(game_result):
    wrong_values = []
    if not isinstance(game_result, str):
        raise TypeError(f"{errors['TypeError']} {type(game_result)}")
    elif not (10 <= len(game_result) <= 20):
        raise IndexError(f"{errors['IndexError']} {len(game_result)}")
    for i in game_result:
        if i in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '/', 'X']:
            continue
        else:
            wrong_values.append(i)
    if wrong_values:
        raise ValueError(f"{errors['ValueError']} {','.join(wrong_values)}")
    return game_result


def get_score(game_result):
    try:
        data_validation(game_result)
    except Exception as exc:
        print(type(exc), exc)
        return

    i = 0
    n = len(game_result)
    result = 0
    multiplier = 1

    while i < n:
        curr_char = game_result[i]
        try:
            if curr_char == '/':
                raise ValueError(f'Первный бросок не может быть - {curr_char} ')
        except Exception as exc:
            print(type(exc), exc)
            break
        if curr_char == 'X':
            result += multiplier * 20
            multiplier = 2
            i += 1
            continue

        try:
            next_char = game_result[i + 1]
        except IndexError as exc:
            print(type(exc), 'Нет такого индекса (броска)!')
            break

        if next_char == '/':
            result += multiplier * 15
        else:
            result += 0 if curr_char == '-' else (multiplier * int(curr_char))
            result += 0 if next_char == '-' else (multiplier * int(next_char))
        multiplier = 1
        i += 2
    return result


if __name__ == "__main__":
    ihor = Bowling(player_name='Ihor')
    ihor.play_game()
    result = ihor.final_result
    get_score(game_result=result)
