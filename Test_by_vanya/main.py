# -*- coding: utf-8 -*-
import asyncio
from typing import Optional, List

import aiohttp

import config
import tests


async def get_parsed_data(url: str) -> Optional[List[List[int]]]:
    if not isinstance(url, str) or not url.startswith('https://'):
        return None

    check_matrix_list = []

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == config.STATUS_OK:
                data = await resp.text()

                for i in data.split("\n"):
                    if i.startswith("|"):
                        check_matrix_list.append(list(map(int, i.split("|")[1:-1])))
            else:
                raise Warning(f"Status code - {resp.status}: error - {config.ERROR_DICT.get(resp.status, resp)}")

    return check_matrix_list


def get_spiral_order(matrix: List[List[int]]) -> Optional[List[int]]:
    if not matrix or len(matrix[0]) != len(matrix):
        return None

    for i in matrix:
        if len(i) != len(matrix):
            return None

    check_number = len(matrix[0]) * len(matrix)

    revers_matrix = []

    for i in matrix[::-1]:
        revers_matrix.append(i[::-1])

    index_1 = 0
    index_2 = len(revers_matrix[0]) - 1
    index_3 = len(revers_matrix) - 1
    index_4 = 0

    result_list = []

    while len(result_list) < check_number:
        # line 1
        for i in revers_matrix[index_1][index_4:index_2 + 1]:
            result_list.append(i)
        index_1 += 1
        if len(result_list) >= check_number:
            break
        # line 2
        for i in revers_matrix[index_1:index_3 + 1]:
            result_list.append(i[index_2])
        index_2 -= 1
        if len(result_list) >= check_number:
            break
        # line 3
        if index_4 == 0:
            for i in revers_matrix[index_3][index_2::-1]:
                result_list.append(i)
            index_3 -= 1
        else:
            for i in revers_matrix[index_3][index_2:index_4 - 1:-1]:
                result_list.append(i)
            index_3 -= 1
        if len(result_list) >= check_number:
            break
        # # line 4
        for i in revers_matrix[index_3:index_1 - 1:-1]:
            result_list.append(i[index_4])
        index_4 += 1

    return result_list


async def parse_matrix(url: str) -> Optional[List[int]]:
    matrix = await get_parsed_data(url=url)
    if matrix is None:
        print(config.WRONG_URL)
        return None

    result = get_spiral_order(matrix=matrix)

    if result is None:
        print(config.WRONG_DATA_IN_MATRIX)
        return None

    return result


if __name__ == "__main__":
    asyncio.run(parse_matrix(url=tests.SOURCE_URL))
