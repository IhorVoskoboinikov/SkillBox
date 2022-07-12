from bouling_engine import Bowling


def get_score(game_result):
    result = 0

    if game_result.endswith('XX'):
        game_result = game_result[:-2]
        result += 40
    if game_result.endswith('X'):
        game_result = game_result[:-1]
        result += 20

    i = 0
    n = len(game_result)

    while i < n:
        char_1 = game_result[i]
        char_2 = game_result[i + 1]

        if char_1 == 'X' and char_2 == 'X':
            if game_result[i + 3] == '/':
                result += (20 + (20 * 2) + (15 * 2))
                i += 4
                continue
        if char_1 == 'X' and char_2 == 'X':
            char_3 = 0 if game_result[i + 2] == '-' else int(game_result[i + 2])
            char_4 = 0 if game_result[i + 3] == '-' else int(game_result[i + 3])
            result += (20 + (20 * 2) + ((char_3 + char_4) * 2))
            i += 4
            continue

        if char_1 == 'X':
            char_3 = game_result[i + 2]
            if char_3 == '/':
                result += (20 + (15 * 2))
                i += 3
                continue

        if char_1 == 'X':
            char_2 = 0 if char_2 == '-' else int(char_2)
            char_3 = 0 if game_result[i + 2] == '-' else int(game_result[i + 2])
            result += (20 + (char_2 + char_3) * 2)
            i += 3
            continue

        if char_2 == '/':
            result += 15
        else:
            result += 0 if char_1 == '-' else int(char_1)
            result += 0 if char_2 == '-' else int(char_2)

        i += 2
        print(result)
    print(result)


ihor = Bowling(player_name='Ihor')
ihor.play_game()
print(ihor)
result = ihor.final_result
get_score(game_result=result)
print(ihor)
