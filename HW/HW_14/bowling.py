from bouling_engine import Bowling


def get_score(game_result):
    list_result = []
    n = 2
    list_result.append(int((game_result.count('X')) * 20))
    list_without_strike = game_result.replace('X', '')
    calculation_list = [list_without_strike[i:i + n] for i in range(0, len(list_without_strike), n)]
    for i in calculation_list:
        if '/' in i:
            list_result.append(15)
        elif '-' in i:
            y = i.replace('-', '')
            list_result.append(int(y))
        else:
            list_result.append(int(i[0]) + int(i[1]))
        print(i)
    print(list_result)
    print(sum(list_result))


ihor = Bowling(player_name='Ihor')
ihor.play_game()
print(ihor)
result = ihor.final_result
get_score(game_result=result)
