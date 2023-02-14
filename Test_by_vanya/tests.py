# -*- coding: utf-8 -*-


import unittest

from test_tasks import test_parse_matrix, SOURCE_URL, EXPECTED


class MyParseMatrix(unittest.TestCase):

    def test_base(self):
        result = test_parse_matrix(SOURCE_URL)
        self.assertEqual(result, EXPECTED)


if __name__ == '__main__':
    unittest.main()
