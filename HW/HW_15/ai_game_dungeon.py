import datetime
import json
import csv
from termcolor import cprint, colored

with open('rpg.json', 'r') as file_with_data:
    game_map = json.load(file_with_data)

log_data = []
next_location = []
time_in_the_game = 0


def ai_game(game_map, experience=0, remaining_time=1234567890.0987654321):
    current_location = ''.join(list(game_map.keys()))
    print(current_location)
    for location, location_object in game_map.items():
        print(location_object)
        for object in location_object:
            if not isinstance(object, dict):
                exp = int(object[(object.find('exp') + 3):(object.find('tm') - 1)])
                spent_time_monster = float(object[(object.find('tm') + 2):])
                remaining_time -= spent_time_monster
                experience += exp
                del (game_map[current_location][0])
                print("OK")
                continue
            ai_game(game_map=object)


ai = ai_game(game_map=game_map)
