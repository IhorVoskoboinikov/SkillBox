# -*- coding: utf-8 -*-
import asyncio
import aiohttp

SOURCE_URL = 'https://raw.githubusercontent.com/koury/pymx/main/source.txt'
EXPECTED = [
    160, 150, 140, 130,
    90, 50, 10, 20,
    30, 40, 80, 120,
    110, 100, 60, 70,
]

ERROR_DICT = {
    206: "Partial Content",
    301: "Moved Permanently",
    302: "Moved Temporarily",
    304: "Not Modified",
    400: "Bad Request",
    403: "Forbidden",
    404: "Not Found",
    408: "Request Timeout ",
    429: "Too Many Requests ",
    500: "Internal Server Error",
    522: "Connection Timed Out",
    524: "A Timeout Occurred",
}


async def parse_matrix(url):
    if not isinstance(url, str):
        print(f"Wrong data type, not a string")
        return
    if not url.startswith('https://'):
        print(f"Wrong url! Request must start with 'https://'")
        return
    matrix = []
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                data = await resp.text()
                for i in data.split("\n"):
                    if i.startswith("|"):
                        matrix.append(list(map(int, i.split("|")[1:-1])))
            else:
                if resp.status in ERROR_DICT:
                    raise Warning(f"Status code - {resp.status}: Error - {ERROR_DICT[resp.status]}")
                else:
                    raise Warning(f"Status code = {resp.status}, error - {resp}")

    revers_matrix = []
    for i in matrix[::-1]:
        revers_matrix.append(i[::-1])

    check_number = len(revers_matrix[0]) * len(revers_matrix)

    result = []
    index_1, index_2, index_3, index_4 = 0, len(revers_matrix[0]) - 1, len(revers_matrix) - 1, 0

    while len(result) < check_number:
        # линия 1
        for i in revers_matrix[index_1][index_4:index_2 + 1]:
            result.append(i)
        index_1 += 1
        # линия 2
        for i in revers_matrix[index_1:index_3 + 1]:
            result.append(i[index_2])
        index_2 -= 1
        # линия 3
        if index_4 == 0:
            for i in revers_matrix[index_3][index_2::-1]:
                result.append(i)
            index_3 -= 1
        else:
            for i in revers_matrix[index_3][index_2:index_4 - 1:-1]:
                result.append(i)
            index_3 -= 1
        # # линия 4
        for i in revers_matrix[index_3:index_1 - 1:-1]:
            result.append(i[index_4])
        index_4 += 1

    return result


def test_parse_matrix():
    asyncio.run(parse_matrix(url="25"))

    # else:
    #     print(asyncio.run(parse_matrix(url=SOURCE_URL)))


test_parse_matrix()
