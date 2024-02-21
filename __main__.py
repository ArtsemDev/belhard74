from itertools import *
from os import system

# for i in count(1, 2):
#     print(i)

# for i in cycle("Hello"):
#     print(i)

# for i in repeat("Hello", 5):
#     print(i)


# for i in combinations("ABCD", 2):
#     print(i)

# for i in combinations_with_replacement("ABCD", 2):
#     print(i)

# for i in permutations("ABCD", 2):
#     print(i)

# for i in product("ABCD", "EFGH", "KLMN"):
#     print(i)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(*takewhile(lambda x: x < 5, numbers))
# print(*dropwhile(lambda x: x < 5, numbers))

# names = ["Petya", "Vasya", "Maria", "Max"]
# flags = [True, None, 1]
# print(*compress(names, flags))

# text = "Hello world"
# for i in islice(text, 1, 10, 2):
#     print(i)
# from os import *
# from pathlib import *

# print(*walk("."))
# BASE_DIR = Path(__file__).resolve().parent
# file_path = BASE_DIR / "input.txt"

# from sys import *


# system("shutdown -r")

from datetime import *


# print(datetime.now(tz=UTC).strftime("%B, %d %Y, %H:%M"))
# print(datetime.strptime("February, 21 2024, 17:32", "%B, %d %Y, %H:%M"))
# print(date)
# print(time)
# print(timedelta)

# date1 = datetime(year=2020, month=5, day=4)
# now = date1.now()
# print(now - date1)

# delta = timedelta()

from enum import IntEnum


class Role(IntEnum):
    USER = 1
    MANAGER = 2
    ADMIN = 3
    SUPERUSER = 4


# user = {
#     "name": "Vasya",
#     "role": 3
# }

# if user.get("role") == Role.ADMIN:
#     ...
# from argparse import ArgumentParser
#
#
# parser = ArgumentParser()
# parser.add_argument("-p", '--port', type=int)
# parser.add_argument("-d", "--debug", action="store_true")
#
# print(parser.parse_args())
# from logging import *
#
# basicConfig(
#     level=INFO,
#     format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s"
# )
# info("INFO")
# warning("WARNING")
# error("ERROR")
