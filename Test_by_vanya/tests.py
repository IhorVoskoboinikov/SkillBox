# -*- coding: utf-8 -*-
import asyncio
import unittest

from test_tasks import parse_matrix
import config


class MyParseMatrix(unittest.TestCase):

    def test_base(self):
        result = asyncio.run(parse_matrix(url=config.SOURCE_URL))
        self.assertEqual(result, config.EXPECTED)

    def test_wrong_type(self):
        types = [int, float, complex, set, list, tuple, bool, None, dict]
        for tp in types:
            result = asyncio.run(parse_matrix(url=tp))
            self.assertEqual(result, None)

    def test_wrong_url(self):
        wrong_url = "wrong.url.com"
        result = asyncio.run(parse_matrix(url=wrong_url))
        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()
