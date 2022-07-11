from random import randint

SKITTLES = 10
FRAMES = 10
_game_result_players = []


def play_game():
    global FRAMES
    first_throw = randint(0, SKITTLES)
    second_throw = randint(0, (SKITTLES - first_throw))
    for throw_number in range(1, 3):
        if throw_number == 1:
            if first_throw == 0:
                _game_result_players.append('-/')
                second_throw = randint(0, SKITTLES)
            elif 1 <= first_throw <= 9:
                _game_result_players.append(str(first_throw))
            else:
                _game_result_players.append('X')
                break
        if throw_number == 2:
            if second_throw == 0:
                _game_result_players.append('-')
                break
            _game_result_players.append(str(second_throw))
    FRAMES -= 1


while FRAMES:
    res = play_game
    res()
print(_game_result_players)
