# a = 5
# is_human = False
# objs = []
#
# if not objs:
#     ...
#
# if not is_human:
#     ...
#
# if a > 0:
#     print("a is positive")
# elif a == 0:
#     print("a is zero")
# else:
#     print("a is negative")

# a = 5
#
# is_even = "No" if a % 2 else "Zero" if a == 0 else "Yes"
#
# if a % 2:
#     is_even = "No"
# elif a == 0:
#     is_even = "Zero"
# else:
#     is_even = "Yes"


# a = 1234
#
# if isinstance(a, str) and a.isdigit():
#     ...

# not (cond1 or cond2) and cond3

# x = True
# y = False
# z = False
# if not x or y:
#     print(1)
# elif not x or not y and z:
#     print(2)
# elif not x or y or not y and x:
#     print(3)
# else:
#     print(4)


# print(isinstance(12.34, (int, float)))
# print(isinstance(12.34, int | float))  # python 3.10+

# a = 6
# # print(isinstance(a, int))
# if isinstance(a, int) and not isinstance(a, bool):
#     print("a is int, a is not bool")
# print(issubclass(bool, int))

# a = 5
# if type(a) is int or type(a) is float:  # bad practice
#     ...
#
# if isinstance(a, (int, float)):
#     ...


# city = None
# user = {}
# user["city"] = city or "Mogilev"
# print(user)
# text = "Hello World"
# numbers = [2, 4, 6, 8, 10]
# data = {"key1": "value1", "key2": "value2"}
# for i in data.items():
#     print(i)

# for i in enumerate(text, start=2):
#     print(i)
# e = range(2, 10, 2)
# for i in e:
#     print(i)
#
# for j in e:
#     print(j)

# for i in range(100):
#     if i % 3 == 0:
#         continue
#     print(i)

# for i in range(10):
#     if i == 10:
#         break
#     print(i)
# else:
#     print("Finish!")

# i = 0
# while i < 10:
#     i += 1
#     print(i)

#  спрашивать у пользователя данные с клавиатуры до тех пор,
#  пока он не строку состоящую из чисел
# a = input("Enter number: ")
# while not a.isdigit():
#     a = input("Are you stupid? Try again: ")


# data = {"key1": "value1", "key2": "value2"}
#
# objs = ["AB", "CD2", "EF34", "GH"]
#
# for i, *k in objs:
#     print(i, k)

# for key, value in data.items():
#     print(key, value)


# words = ["Hello", "Python", "World"]
# for word in words:
#     for letter in word:
#         print(letter)

# for _ in range(10):  # best practice
#     print("Hello")

#  пользователь вводит строку, используя цикл For, заполнить список
#  символами из строки но в верхнем регистре

# text = input()
# objs2 = [i.upper() for i in text if i.isalpha()]
#
# objs = []
# for i in text:
#     if i.isalpha():
#         objs.append(i.upper())


# numbers = [4, -2, 3, -5, 6, 7, 8, -10, 12, 13, -15, 34, 65]
# result2 = [(number / 2) if number % 2 else (number * 2) for number in numbers if number > 0]
# result = []
# for number in numbers:
#     if number > 0:
#         if number % 2:
#             result.append(number / 2)
#         else:
#             result.append(number * 2)

# objs = [[1, 2], [3, 4], [5, 6]]
# for obj in objs:
#     obj.append(sum(obj))
# print(objs)

# try:
#     a = int(input())
#     b = int(input())
#     c = a / b
# except ValueError as e:
#     print(e)
# except Exception as e:
#     print(e)
# else:
#     print("not exception")
# finally:
#     print("always")

# try:
#     a = int(input())
# finally:
#     print("always")


# raise ValueError("some text")
#
# status_codes = {
#     200: "OK",
#     201: "CREATED",
#     202: "ACCEPTED"
# }
# status = 200
# print(status_codes.get(status, "ERROR"))
#
# if status == 200:
#     print("OK")
# elif status == 201:
#     print("CREATE")
# elif status == 202:
#     print("CREATED")
# else:
#     print("ERROR")

# a = None
# match a:
#     case int(a) | float(a):
#         print("int or float")
#     case str(a):
#         print("str")
#     case _:
#         print("other number")

# color = (255, 0, 0, 25.5)
# match color:
#     case (int(r), int(g), int(b)):
#         print("RGB")
#         print(r, g, b)
#     case (int(r), int(g), int(b), int(a) | float(a)):
#         print("RGBA")
#         print(r, g, b, a)
#     case _:
#         print("invalid")

# data = {i: {"name": input("name %s: " % i), "email": input(f"email {i}: ")} for i in range(3)}
# print(data)
#
# data2 = {}
# for i in range(3):
#     data2[i] = {
#         "name": input(),
#         "email": input()
#     }
# text = input()
# counter = {i: text.count(i) for i in text}

# N = 34
# 2 4 6 8 10
# 12 14 16 18 20
# 32 34
# first_number = float(input())
# action = input()  # + - * /
# second_number = float(input())

# *** Пользователь вводит химическую формулу (элементы однобуквенныe и формула без скобок)
#  input: C2H5OH
#  output: {"C": 2, "H": 6, "O": 1}
