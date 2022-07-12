from random import randint


class Bowling:

    def __init__(self, player_name):
        self.player_name = player_name
        self.SKITTLES = 10
        self.FRAMES = 10
        self.game_result_player = []
        self.final_result = None

    def __str__(self):
        return f'{self.player_name} закончил игру с результатом {self.final_result}'

    def play_game(self):
        while self.FRAMES:
            first_throw = randint(0, self.SKITTLES)
            second_throw = randint(0, (self.SKITTLES - first_throw))
            for throw_number in range(1, 3):
                if throw_number == 1:
                    if first_throw == 0:
                        self.game_result_player.append('-')
                        second_throw = randint(0, self.SKITTLES)
                    elif 1 <= first_throw <= 9:
                        self.game_result_player.append(str(first_throw))
                    else:
                        self.game_result_player.append('X')
                        break
                if throw_number == 2:
                    if second_throw == 0:
                        self.game_result_player.append('-')
                        break
                    if second_throw == 10 or (first_throw + second_throw) == 10:
                        self.game_result_player.append('/')
                        break
                    self.game_result_player.append(str(second_throw))
            self.FRAMES -= 1
        self.final_result = ''.join(self.game_result_player)


ihor = Bowling(player_name='Ihor')
ihor.play_game()
# print(ihor)
print(ihor.game_result_player)
print(ihor.final_result)
