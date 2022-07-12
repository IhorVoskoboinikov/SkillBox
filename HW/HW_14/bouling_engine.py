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
        for frame_i in range(self.FRAMES):
            first_throw = randint(0, self.SKITTLES)
            second_throw = randint(0, (self.SKITTLES - first_throw))
            for throw_index, throw in enumerate([first_throw, second_throw]):
                if throw == 0:
                    self.game_result_player.append('-')
                if throw == 10:
                    if throw_index == 0:
                        self.game_result_player.append('X')
                        break
                    else:
                        self.game_result_player.append('/')
                if 1 <= throw <= 9:
                    if throw_index == 1 and first_throw + second_throw == 10:
                        self.game_result_player.append('/')
                    else:
                        self.game_result_player.append(str(throw))
        self.final_result = ''.join(self.game_result_player)


ihor = Bowling(player_name='Ihor')
ihor.play_game()
print(ihor)
# print(ihor.game_result_player)
# print(ihor.final_result)
