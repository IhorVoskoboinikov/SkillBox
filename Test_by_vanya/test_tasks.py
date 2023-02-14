# -*- coding: utf-8 -*-
import asyncio
from typing import Optional, List

import aiohttp

import config


async def parsing_data(url: str) -> Optional[List[List[int]]]:
    check_matrix_list = []
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                data = await resp.text()
                for i in data.split("\n"):
                    if i.startswith("|"):
                        check_matrix_list.append(list(map(int, i.split("|")[1:-1])))
            else:
                if resp.status in config.ERROR_DICT:
                    raise Warning(f"Status code - {resp.status}: error - {config.ERROR_DICT[resp.status]}")
                else:
                    raise Warning(f"Status code = {resp.status}: error - {resp}")
            return check_matrix_list


def spiral_order(matrix: List[List[int]]) -> List[int]:
    revers_matrix = []

    for i in matrix[::-1]:
        revers_matrix.append(i[::-1])

    check_number = len(revers_matrix[0]) * len(revers_matrix)

    result_list = []
    index_1, index_2, index_3, index_4 = 0, len(revers_matrix[0]) - 1, len(revers_matrix) - 1, 0

    while len(result_list) < check_number:

        for i in revers_matrix[index_1][index_4:index_2 + 1]:
            result_list.append(i)
        index_1 += 1

        for i in revers_matrix[index_1:index_3 + 1]:
            result_list.append(i[index_2])
        index_2 -= 1

        if index_4 == 0:
            for i in revers_matrix[index_3][index_2::-1]:
                result_list.append(i)
            index_3 -= 1
        else:
            for i in revers_matrix[index_3][index_2:index_4 - 1:-1]:
                result_list.append(i)
            index_3 -= 1

        for i in revers_matrix[index_3:index_1 - 1:-1]:
            result_list.append(i[index_4])
        index_4 += 1

    return result_list


async def parse_matrix(url: str) -> Optional[List[int]]:
    if not isinstance(url, str):
        print(config.WRONG_DATA)
        return
    if not url.startswith('https://'):
        print(config.WRONG_URL)
        return

    matrix = await parsing_data(url=url)

    if not matrix:
        print(config.NO_DATA_IN_MATRIX)
        return

    result = spiral_order(matrix=matrix)

    if result == config.EXPECTED:
        print("The result is correct!")
    return result


if __name__ == "__main__":
    asyncio.run(parse_matrix(url=config.SOURCE_URL))
