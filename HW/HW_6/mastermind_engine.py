from random import randint

MAX_NUMBER_SIZE = 4

_guess_number = {}  # угадываемое число


def think_of_a_number():  # загадать число
    global _guess_number
    _guess_number = {}
    for i in range(0, MAX_NUMBER_SIZE):
        _guess_number[i] = randint(1, 9)
    return _guess_number.values()


def check_number(player_response):  # проверить число
    bulls_cows = {}
    count_bulls = 0
    count_cows = 0
    for key, value in _guess_number.items():
        if str(value) == player_response[key]:
            count_bulls += 1
            bulls_cows['bulls'] = count_bulls
            # print(key + 1, "Нашли быка")
        elif player_response.count(str(value)):
            count_cows += 1
            bulls_cows['cows'] = count_cows
            # print(key + 1, "Нашли корову")

    return bulls_cows

# if __name__ == "__main__":
#     print(len(player_input))
    # think_of_a_number()
    # print(_guess_number.values())
    # print(check_number(player_response=player_input))
