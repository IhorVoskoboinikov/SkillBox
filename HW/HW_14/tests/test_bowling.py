import unittest

from HW_14.bowling_additional import get_score


class BowlingTest(unittest.TestCase):

    def test_for_numbers(self):
        self.result = get_score(game_result='25')
        self.assertEqual(self.result, 7)

    def test_for_number_and_miss(self):
        self.result = get_score(game_result='2-')
        self.assertEqual(self.result, 2)

    def test_for_miss_and_number(self):
        self.result = get_score(game_result='-5')
        self.assertEqual(self.result, 5)

    def test_for_miss_and_spare(self):
        self.result = get_score(game_result='-/')
        self.assertEqual(self.result, 15)

    def test_for_number_and_spare(self):
        self.result = get_score(game_result='5/')
        self.assertEqual(self.result, 15)

    def test_for_strike_and_numbers(self):
        self.result = get_score(game_result='X23')
        self.assertEqual(self.result, 30)

    def test_for_strike_and_miss_number(self):
        self.result = get_score(game_result='X-3')
        self.assertEqual(self.result, 26)

    def test_for_strike_number_and_miss(self):
        self.result = get_score(game_result='X2-')
        self.assertEqual(self.result, 24)

    def test_for_strike_miss_and_miss(self):
        self.result = get_score(game_result='X--')
        self.assertEqual(self.result, 20)

    def test_for_strike_miss_and_spare(self):
        self.result = get_score(game_result='X-/')
        self.assertEqual(self.result, 50)

    def test_for_strike_number_and_spare(self):
        self.result = get_score(game_result='X5/')
        self.assertEqual(self.result, 50)

    def test_for_double_strike_and_numbers(self):
        self.result = get_score(game_result='XX26')
        self.assertEqual(self.result, 76)

    def test_for_double_strike_miss_and_miss(self):
        self.result = get_score(game_result='XX--')
        self.assertEqual(self.result, 60)

    def test_for_double_strike_number_and_miss(self):
        self.result = get_score(game_result='XX2-')
        self.assertEqual(self.result, 64)

    def test_for_double_strike_miss_and_number(self):
        self.result = get_score(game_result='XX-6')
        self.assertEqual(self.result, 72)

    def test_for_double_strike_and_number_and_spare(self):
        self.result = get_score(game_result='XX2/')
        self.assertEqual(self.result, 90)

    def test_for_double_strike_and_miss_and_spare(self):
        self.result = get_score(game_result='XX-/')
        self.assertEqual(self.result, 90)


if __name__ == '__main__':
    unittest.main()
