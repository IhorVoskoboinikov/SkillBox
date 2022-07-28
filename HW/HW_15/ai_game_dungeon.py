import json
from termcolor import cprint, colored

with open('rpg.json', 'r') as file_with_data:
    game_map = json.load(file_with_data)

experience = 0
remaining_time = 1234567890.0987654321


def ai_game(game_map):
    global remaining_time, experience
    for location, location_object in game_map.items():
        location = ''.join(location)
        cprint(location, color='green')
        for objects in location_object:
            if not isinstance(objects, dict):
                if (remaining_time > 0) and (experience < 280):
                    print(objects)
                    exp = int(objects[(objects.find('exp') + 3):(objects.find('tm') - 1)])
                    spent_time_monster = float(objects[(objects.find('tm') + 2):])
                    remaining_time -= spent_time_monster
                    experience += exp
                    print(f'Exp - {experience}, time - {remaining_time}')
                    del objects
                    continue
                else:
                    print(f"Game over! EXP = {experience}, TIME = {remaining_time}")
                    break
            location_name = ''.join(list(objects.keys()))
            print(location_name)
            spent_time = float(location_name[(location_name.find('tm') + 2):])
            remaining_time -= spent_time
            cprint(objects, color='red')
            # if (remaining_time > 0) and (experience < 280):
            ai_game(game_map=objects)
            # else:
            #     print(f"Game over! EXP = {experience}, TIME = {remaining_time}")


ai_game(game_map=game_map)
