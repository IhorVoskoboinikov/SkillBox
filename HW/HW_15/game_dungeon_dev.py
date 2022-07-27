import datetime
import json
import csv
from termcolor import cprint, colored

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
        self.current_location_name = None
        self.log_data = []
        self.next_location = []
        self.monsters_in_location = []
        self.time_in_the_game = 0

    def game_step(self):
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

        self.current_location = current_location
        self.current_location_name = self.locations[-1]

        for elem in current_location:
            if isinstance(elem, dict):
                self.next_location.append(list(elem.keys())[0])
                continue
            self.monsters_in_location.append(elem)

    def player_choose(self):
        n_monster = len(self.monsters_in_location)
        n_location = len(self.next_location)
        cprint(f"Вы находитесь в {''.join(self.current_location_name)}\n"
               f"У вас {self.experience} опыта и {self.remaining_time} секунд \n"
               f"Уже прошло времени - {self.time_in_the_game}", color='green')
        cprint(f"Внутри вы видите:", color='blue')
        for num, monster in enumerate(self.monsters_in_location):
            print(f"{num + 1} -- Монстра {monster}")
        for num, loc in enumerate(self.next_location):
            print(f"{n_monster + (num + 1)} -- Вход в локацию {loc}")
        cprint(f"Выберите действие:", color='blue')
        for num, monster in enumerate(self.monsters_in_location):
            print(f"{num + 1} -- Атаковать монстра {monster}")
        for num, loc in enumerate(self.next_location):
            print(f"{n_monster + (num + 1)} -- Перейти в локацию {loc}")
        cprint(f'{n_monster + n_location + 1} -- Выход')
        player_choose = input(colored('Сделайте ваш выбор:', color='blue'))
        try:
            if int(player_choose) == (n_monster + n_location + 1) or self.experience >= 280:
                cprint(f"Вы завершили игру с результатом:\n"
                       f" - опыт = {self.experience}\n"
                       f" - остаток времени = {self.remaining_time}", color='green')
                self.remaining_time = 0
            elif int(player_choose) <= n_monster:
                self.monster_attack(player_choose)
            else:
                self.move_to_another_location(player_choose, n_monster)
        except IndexError:
            self.next_location.clear()
            self.monsters_in_location.clear()
            cprint("Не правильный ввод! Повторите попытку!", color='red')

    def monster_attack(self, player_choose):
        player_choose = int(player_choose)
        monster_name = self.monsters_in_location[(player_choose - 1)]
        exp = int(monster_name[(monster_name.find('exp') + 3):(monster_name.find('tm') - 1)])
        spent_time_monster = float(monster_name[(monster_name.find('tm') + 2):])
        self.experience += exp
        self.remaining_time -= spent_time_monster
        self.time_in_the_game += spent_time_monster
        self.current_location.remove(monster_name)
        self.monsters_in_location.remove(monster_name)
        self.next_location.clear()
        self.monsters_in_location.clear()

    def move_to_another_location(self, player_choose, n_monster):
        self.start_game_time = datetime.datetime.now()
        player_choose = int(player_choose)
        if not n_monster:
            n_monster = 0
        location_name = self.next_location[(player_choose - n_monster - 1)]
        spent_time = float(location_name[(location_name.find('tm') + 2):])
        self.remaining_time -= spent_time
        self.time_in_the_game += spent_time
        self.locations.append(location_name)
        self.next_location.clear()
        self.monsters_in_location.clear()
        self.start_game_time = datetime.datetime.now()
        log_time = f"{self.start_game_time.strftime('%d.%m.%Y')} {self.start_game_time.strftime('%H:%M:%S')}"
        self.log_data.append([self.current_location_name, self.experience, log_time])


field_names = ['current_location', 'current_experience', 'current_date']
game = Game(location_path=game_map)
while game.remaining_time > 0:
    cprint("================================", color='red')
    game.game_step()
    game.player_choose()
# for i in game.log_data:
#     print(i)
#
with open('dungeon.csv', 'w', newline='') as write_log_csv:
    writer = csv.writer(write_log_csv)
    writer.writerow(field_names)
    for row in game.log_data:
        writer.writerow(row)


