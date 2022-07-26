import datetime
import json
from pprint import pprint

from termcolor import cprint

with open('rpg.json', 'r') as file_with_data:
    game_map = json.load(file_with_data)  # преобразование в словарь
    # json_data = json.dumps(self.game_data)
    # pprint(type(game_map))


class Game:
    def __init__(self, location_path):
        self.location_path = location_path
        self.experience = 0
        self.remaining_time = 1234567890.0987654321
        self.start_game_time = datetime.datetime.now()
        self.locations = list(self.location_path.keys())
        self.current_location = None
        self.next_location = []
        self.monsters_in_location = []

    # print(f"Data - {start_game_time.strftime('%d.%m.%Y!')}, time - {start_game_time.strftime('%H:%M:%S')}")

    def game_step(self):
        print(self.locations)
        print(type(self.location_path))
        current_location = [self.location_path]
        for location_name in self.locations:
            for location_object in current_location:
                if not isinstance(location_object, dict):
                    continue  # монстр
                elif list(location_object.keys())[0] == location_name:
                    current_location = location_object[location_name]
                    break
            else:
                raise RuntimeError("Location path is wrong!")

        self.current_location = str(self.locations[-1])

        for elem in current_location:
            if isinstance(elem, dict):
                self.next_location.append(list(elem.keys())[0])
                continue
            self.monsters_in_location.append(elem)

    def player_choose(self):
        n_monster = len(self.monsters_in_location)
        n_location = len(self.next_location)
        print(f"Вы находитесь в {''.join(self.current_location)}\n"
              f"У вас {self.experience} опыта и {self.remaining_time} секунд \n"
              f"Прошло уже {self.remaining_time}\n"
              f"Внутри вы видите:")
        for num, monster in enumerate(self.monsters_in_location):
            print(f"{num + 1} -- Монстра {monster}")
        for num, loc in enumerate(self.next_location):
            print(f"{n_monster + (num + 1)} -- Вход в локацию {loc}")
        print(f"Выберите действие:")
        for num, monster in enumerate(self.monsters_in_location):
            print(f"{num + 1} -- Атаковать монстра {monster}")
        for num, loc in enumerate(self.next_location):
            print(f"{n_monster + (num + 1)} -- Перейти в локацию {loc}")
        player_choose = input(f'{n_monster + n_location + 1} -- Выход\n:')
        if int(player_choose) == (n_monster + n_location + 1):
            print("Вы покинули игру!")
            self.remaining_time = 0
        elif int(player_choose) <= n_monster:
            self.monster_attack(player_choose)
        else:
            self.move_to_another_location(player_choose, n_monster)

    def monster_attack(self, player_choose):
        player_choose = int(player_choose)
        monster_name = self.monsters_in_location[(player_choose - 1)]
        if len(self.locations) <= 1: #  место зависания!!!!
            self.location_path[self.locations[0]].remove(monster_name)
        else:
            self.location_path[self.locations[0]][self.locations[1]].remove(monster_name)
        self.next_location.clear()
        self.monsters_in_location.clear()

    def move_to_another_location(self, player_choose, n_monster):
        player_choose = int(player_choose)
        location_name = self.next_location[(player_choose - n_monster - 1)]
        self.locations.append(location_name)
        self.next_location.clear()


game = Game(location_path=game_map)
while game.remaining_time > 0:
    cprint("================================", color='red')
    game.game_step()
    game.player_choose()
