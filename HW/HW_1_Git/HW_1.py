import os

import platform
import sys

info = f" Os sis \n {platform.uname()},\n Python {sys.version},\n {platform.architecture()}"

print(info)

with open("os_info.txt", "w") as ff:
    ff.write(info)
