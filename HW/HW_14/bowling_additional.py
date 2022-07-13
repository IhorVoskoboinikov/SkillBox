from bouling_engine import Bowling


def get_score(game_result):
    i = 0
    n = len(game_result)
    result = 0
    multiplier = 1

    while i < n:
        curr_char = game_result[i]
        if curr_char == 'X':
            result += multiplier * 20
            multiplier = 2
            i += 1
            continue

        next_char = game_result[i + 1]

        if next_char == '/':
            result += multiplier * 15
        else:
            result += 0 if curr_char == '-' else (multiplier * int(curr_char))
            result += 0 if next_char == '-' else (multiplier * int(next_char))
        multiplier = 1
        i += 2
    return result


ihor = Bowling(player_name='Ihor')
ihor.play_game()
print(ihor)
result = ihor.final_result
print(get_score(game_result=result))
