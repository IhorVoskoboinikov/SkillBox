# -*- coding: utf-8 -*-
import unittest
import asyncio

import config

from main import parse_matrix, get_parsed_data, get_spiral_order

EXPECTED = [
    160, 150, 140, 130,
    90, 50, 10, 20,
    30, 40, 80, 120,
    110, 100, 60, 70,
]


class MyParseMatrix(unittest.TestCase):

    def test_base_run_parse_matrix(self):
        result = asyncio.run(parse_matrix(url=config.SOURCE_URL))
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
        wrong_matrix = [[1, 2, 3, 4], [5, 6, 7]]
        result = get_spiral_order(matrix=wrong_matrix)
        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()
