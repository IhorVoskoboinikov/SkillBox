import datetime
import json
from pprint import pprint

with open('rpg.json', 'r') as file_with_data:
    game_map = json.load(file_with_data)  # преобразование в словарь
    # json_data = json.dumps(self.game_data)
    # pprint(type(game_map))


class Game:
    def __init__(self):
        self.location_path = game_map
        self.experience = 0
        self.remaining_time = 1234567890.0987654321
        self.start_game_time = datetime.datetime.now()
        self.locations = list(game_map.keys())
        self.current_location = None
        self.next_location = []
        self.monsters_in_location = []

    def __str__(self):
        return f"Вы находитесь в {self.locations}"

    # print(f"Data - {start_game_time.strftime('%d.%m.%Y!')}, time - {start_game_time.strftime('%H:%M:%S')}")

    def game_step(self):
        current_location = [game_map]
        object_in_location = []

        for location_name in self.locations:
            for location_object in current_location:
                if not isinstance(location_object, dict):
                    continue  # монстр
                elif list(location_object.keys())[0] == location_name:
                    current_location = location_object[location_name]
                    break
            else:
                raise RuntimeError("Location path is wrong!")

        current_location_name = self.locations[-1]
        print(current_location_name)
        for elem in current_location:
            if isinstance(elem, dict):
                object_in_location.append(list(elem.keys())[0])
                continue
            object_in_location.append(elem)
        print(object_in_location)


game = Game()
game.game_step()
