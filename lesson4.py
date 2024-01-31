# objs = [1, 3, 2, 4, "Hello", "World", True, None]
# text = "Hello"
# a = list(text)
# print(a)

# objs[0:3] = "First"
# print(objs)

# zeros = [i for i in range(0, 100)]
# print(zeros)
# text = "Hello"
# objs = [2, 4, 6, 8, 6, 10, 6, text]
# objs.remove(6)
# print(objs)
# objs2 = objs[1:3]
# del objs[1:3]
# print(objs)
# print(objs2)
# print(objs[-1] is text)
# del objs[1:3]
# print(objs)
# a = objs.pop(5)
# print(objs)
# print(a)
# from sys import getrefcount
# a = []
# a.append(a)
# print(getrefcount(a))


# a = [1, 2, 3, 4]
# a.append(5)
# a.insert(0, 0)
# print(a)
# a.extend([5, 6, 7])
# a += [5, 6, 7]
# print(a)
# b = a + a
# print(b)
# a = [3, 3, 4, 2, 4, 2]
# print(a.count(3))
# a = [4, 5, 2, 4, 3, -123, -56, 23, 4, ]
# a.sort(key=abs)
# print(a)

# words = ["apple", "Hello", "python", "Age", "len"]
# words.sort(key=str.lower)
# print(words)
# words.sort(key=len, reverse=True)
# print(words)

# sorted_words = sorted(words, key=str.lower, reverse=True)
# print(words)
# print(sorted_words)

# a = [1, 2, 3, 4, 5]
# a.reverse()
# print(a)
# b = a[::-1]
# print(a)
# print(b)


# a = [1, 2, 3, 4, []]
# c = a.copy()
# c[-1].append(0)
# print(a)
# print(c)
# b.append(5)
# print(a)


# a = [1, 2, 3, [7, 8, "Hello", 9], 4, 5, 6]
# print(a[3][2][1])


# a = (1, )
# print(a)
# a = []
# b = (1, 2, 3, 4, a, 5, 6, 7)
# a.append("World")
# b[4].append("Hello")
# print(b)


# a = {6, 5, 6, 5, 4, 3, 2, 4, 5, 7, 8, 9, -10, 20}
# print(a)

# a = set("Hello")
# print(a)
# a = {8, 3, 1}
# b = {6, 7, 8, 3}
# print(a.issuperset(b))
# print(a >= b)
# print(a == b)
# c = a.union(b, [0, 8, 1, ], ("Hello", "World"))
# print(a | b | {5, 6, 5, 3,})
# print(a.difference(b))
# print(a.intersection(b))
# print(a & b)
# print(a.symmetric_difference(b))
# print(a ^ b)

# a = frozenset([1, 2, 3, 4, 5])
# print(a)
# allowed_http_methods = {"GET", "POST"}
# user_request = "PUT"
# print(user_request in allowed_http_methods)

# a = {1, 2, 3}
# print(type(a))

# data = {
#     "first_name": "Alex",
#     "age": 34,
#     "is_human": True,
#     "languages": ["ru", "en"],
# }
# data["first_name"] = "Max"
# print("age" in data)

# data = dict([("name", "Alex"), ("age", 34), ("lang", [])])
# print(data)
# data = dict.fromkeys(["name", "age", "city"], "Н/У")
# data["is_human"] = "Minsk"
# print(data)


# data = {
#     "first_name": "Alex",
#     "age": 34,
#     "is_human": True,
#     "languages": ["ru", "en"],
# }
# print(data.setdefault("city", "Minsk"))
# print(data)
# del data["is_human"]
# print(data.pop("city", None))
# print(data.popitem())
# print(list(data))
# print(data.values())
# print(data.items())
# data.update({"first_name": "Max", "city": "Minsk"})
# print(data)
# data2 = {"first_name": "Max", "city": "Minsk"}
# data3 = {**data, **data2}
# data3 = data | data2
# print(data3)

# a, b = {"name": "alex", "age": 34}.items()
# print(a)
# print(b)
# data = {"sep": "-", "end": " FINISH!"}
# print(1, 2, 3, 4, 5, **data)


# a, _, c, d, *_ = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
# print(_)

# a = 5
# print(b := 4)
# print(b)

# a = [1, 2, 3, 4]
# print(*a)
# b = [*a, *(5, 6, 7, 8)]
# print(b)

# from collections import *


# words = ["Hello", "World", "Hello", "Python"]
# c = Counter(words)
# b = Counter(["Hello", "World", "Python", "World", "Pycharm"])
# print(c)
# print(b)
# # c.subtract(b)
# print(c - b)


# data = defaultdict(int)
# data["a"] += 5
# print(data)
# User = namedtuple("User", ["name", "age", "city"])
# vasya = User(name="Vasya", age=34, city="Minsk")
# petya = User(name="Petya", age=32, city="Gomel")
# print(vasya.name)
# print(petya.name)
# print(vasya._asdict())


# numbers = deque([1, 2, 3, 4, 5])
# numbers.rotate(-2)
# print(numbers)

# a = {1: 1, 2: 2, 3: 3}
# b = {3: 4, 4: 5, 5: 6}
# chain = ChainMap(a, b)
# # print(chain.parents[3])
# chain["text"] = "Hello"
# print(chain)

# a = [1, 2, 3]
# b = [1, 2, 3, 4]
# print(a < b)
