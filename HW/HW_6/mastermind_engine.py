from random import randint

MAX_NUMBER_SIZE = 4

_guess_number = []  # угадываемое число


def think_of_a_number():  # загадать число
    _guess_number.append(randint(1, 9))
    for i in range(1, MAX_NUMBER_SIZE):
        _guess_number.append(randint(0, 9))


def check_number(player_response):  # проверить число
    bulls_cows = {'bulls': 0, 'cows': 0}
    player_response_set = set(player_response)
    for player_digit, digit in zip(player_response, _guess_number):
        if str(digit) == player_digit:
            bulls_cows['bulls'] += 1
        elif digit in player_response_set:
            bulls_cows['cows'] += 1

    return bulls_cows


def validate_number(player_response):
    return len(player_response) == 4

# if __name__ == "__main__":
#     print(len(player_input))
# think_of_a_number()
# print(_guess_number.values())
# print(check_number(player_response=player_input))
