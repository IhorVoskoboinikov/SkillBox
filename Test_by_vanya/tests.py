# -*- coding: utf-8 -*-
import unittest
import asyncio

from main import parse_matrix, get_parsed_data, get_spiral_order

SOURCE_URL = 'https://raw.githubusercontent.com/koury/pymx/main/source.txt'
EXPECTED = [
    160, 150, 140, 130,
    90, 50, 10, 20,
    30, 40, 80, 120,
    110, 100, 60, 70,
]
RESULT_FIVE_FIVE = [
    25, 24, 23, 22, 21,
    16, 11, 6, 1, 2,
    3, 4, 5, 10, 15,
    20, 19, 18, 17, 12,
    7, 8, 9, 14, 13
]
RESULT_TEN_TEN = [
    100, 99, 98, 97, 96, 95, 94, 93, 92, 91,
    81, 71, 61, 51, 41, 31, 21, 11, 1, 2,
    3, 4, 5, 6, 7, 8, 9, 10, 20, 30,
    40, 50, 60, 70, 80, 90, 89, 88, 87, 86,
    85, 84, 83, 82, 72, 62, 52, 42, 32, 22,
    12, 13, 14, 15, 16, 17, 18, 19, 29, 39,
    49, 59, 69, 79, 78, 77, 76, 75, 74, 73,
    63, 53, 43, 33, 23, 24, 25, 26, 27, 28,
    38, 48, 58, 68, 67, 66, 65, 64, 54, 44,
    34, 35, 36, 37, 47, 57, 56, 55, 45, 46
]


class MyParseMatrix(unittest.TestCase):

    def test_base_run_parse_matrix(self):
        result = asyncio.run(parse_matrix(url=SOURCE_URL))
        self.assertEqual(result, EXPECTED)

    def test_wrong_type_in_get_parsed_data(self):
        types = [int, float, complex, set, list, tuple, bool, None, dict]
        for t_p in types:
            result = asyncio.run(get_parsed_data(url=t_p))
            self.assertEqual(result, None)

    def test_wrong_url_in_get_parsed_data(self):
        wrong_url = "wrong.url.com"
        result = asyncio.run(get_parsed_data(url=wrong_url))
        self.assertEqual(result, None)

    def test_no_matrix_in_get_spiral_order(self):
        no_matrix = []
        result = get_spiral_order(matrix=no_matrix)
        self.assertEqual(result, None)

    def test_not_square_matrix_in_get_spiral_order(self):
        wrong_matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]
        result = get_spiral_order(matrix=wrong_matrix)
        self.assertEqual(result, None)

    def test_wrong_data_in_matrix_in_get_spiral_order(self):
        wrong_matrix = [[1, 2, 3, 4], [5, 6, 7], [9, 10, 11, 12, 13, 14]]
        result = get_spiral_order(matrix=wrong_matrix)
        self.assertEqual(result, None)

    def test_matrix_five_five(self):
        matrix = [[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10],
                  [11, 12, 13, 14, 15],
                  [16, 17, 18, 19, 20],
                  [21, 22, 23, 24, 25]]
        result = get_spiral_order(matrix=matrix)
        self.assertEqual(result, RESULT_FIVE_FIVE)

    def test_matrix_ten_ten(self):
        matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                  [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
                  [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
                  [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
                  [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
                  [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
                  [61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
                  [71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
                  [81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
                  [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]]
        result = get_spiral_order(matrix=matrix)
        self.assertEqual(result, RESULT_TEN_TEN)


if __name__ == '__main__':
    unittest.main()
