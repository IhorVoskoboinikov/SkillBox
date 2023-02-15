# -*- coding: utf-8 -*-

SOURCE_URL = 'https://raw.githubusercontent.com/koury/pymx/main/source.txt'
WRONG_URL = "Wrong url! Request must start with 'https://' and be string!"
WRONG_DATA_IN_MATRIX = "No data in matrix or matrix is not square or wrong matrix!"

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

STATUS_OK = 200
