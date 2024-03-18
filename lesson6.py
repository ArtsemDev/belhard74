# # def length(a, b):
# #     count = 0
# #     for _ in a:
# #         count += 1
# #     return count
# #
# #
# # # text = "Hello world"
# # # text2 = "Python"
# # # c = length(b=text2, a=text)
# #
# #
# # def foo(a=42, b=None):
# #     print(a)
# #
# #
# # def bar(a, b=None):
# #     if b is None:
# #         b = []
# #     b.append(a)
# #     print(b)
# #
# #
# # def baz(*args):
# #     print(args)
# #
# #
# # # baz(4, 6, 8, 10, 12, 14, 16, 18, 20)
# #
# #
# # def foo2(**kwargs):
# #     print(kwargs)
# #
# #
# # # foo2(a=1, b=2, c=3)
# #
# #
# # def bar2(a, b, *args, c=3, d=None, **kwargs):
# #     print(a)
# #     print(b)
# #     print(c)
# #     print(d)
# #     print(args)
# #     print(kwargs)
# #
# #
# # # bar2(1, 2, 3, 4, 5, 6, 7, c=8, d=9, e=10)
# #
# #
# # def baz2(e, *, a, b, c, d):
# #     print(a)
# #     print(b)
# #     print(c)
# #     print(d)
# #     print(e)
# #
# #
# # # baz2(0, a=1, b=2, c=3, d=4)
# #
# # # a = 5
# # #
# # #
# # # def foo3():
# # #     a = 10
# # #
# # #     def wrapper():
# # #         nonlocal a
# # #         print(a)
#
#
# # def key(a):
# #     if isinstance(a, (int, float)):
# #         return a
# #     elif isinstance(a, str):
# #         return int(a)
#
#
# # objs = [3, 5, "4", 6, "-23", -45, ]
# # # key = lambda a: a if isinstance(a, (int, float)) else int(a)  # bad practice
# # # print(key("99"))
# # objs.sort(key=lambda x: x if isinstance(x, (int, float)) else int(x))
# # print(objs)
#
#
# def foo(a: list, *args: str | int, **kwargs: int) -> tuple[bool, bool]:
#     print(a)
#     print(args)
#     print(kwargs)
#     return True, False
#
#
# # numbers: list[int] = [1, 2, 3, 4]
# #
# # data: dict[str, dict[str, str]] = {
# #     "name": {"": ""}
# # }
#
#
# def bar(objs: list):
#     for obj in objs:  # type: int
#         print(obj)
#
#
# # print(bar.__annotations__)
# # print(bar.__name__)
# # print(bar.__code__)
# # print(bar.__builtins__)
# # print(bar.__dict__)
#
# def func(a, b):
#     return int(a) * int(b)
#
#
# # numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
# # numbers2 = ["11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
# # m = map(func, numbers, numbers[:-2])
# # for i in m:
# #     print(i)
# # print(next(m))
# # print("sleep")
# # print(next(m))
# # print("sleep")
# # numbers = [int(i) for i in numbers]
# # print(numbers)
# # for i, el in enumerate(numbers):
# #     numbers[i] = int(el)
# # print(numbers)
#
# # objs = [2, 4, -5, 6, -23, 5, 3, -5, 7, 54, 7]
# # f = filter(lambda x: x > 0, objs)
# # for i in f:
# #     print(i)
#
#
# # text = "Hello world"
# # objs = [True, False, None]
# # s = (4, 7, 2, 5)
# # z = zip(text, objs, s, strict=True)
# # for i in z:
# #     print(i)
#
# # from itertools import zip_longest
#
#
# # a = zip_longest(text, objs, s, fillvalue="Н/У")
# # for i in a:
# #     print(i)


# def my_range(start, stop, step):
#     for i in range(start, stop, step):
#         yield i
#
#
# a = my_range(1, 10, 2)
# text = "Hello"
# b = (i for i in text)
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(a))
# print("sleep")
# print(next(a))
# print("sleep")
# print(next(a))
# print("sleep")

# vasyapupkin@gmail.com


def ping():
    for _ in range(10):
        yield "PING"


def pong():
    for _ in range(10):
        print("PONG")
        yield from ping()


# p = pong()
# for i in p:
#     print(i)


def infinity_ping():
    while ...:
        yield "PONG"


# for i in infinity_ping():
#     print(i)

# from sys import setrecursionlimit, getrecursionlimit
#
# print(getrecursionlimit())
# setrecursionlimit(2000)
# print(getrecursionlimit())

numbers = [1, 2, 3, [1, 2, 3, [1, 2, 3], [1, 2, 3], 4, 5, 6], 4, 5, 6]


def recursive_multiply(objs: list[int | list]) -> int:
    c = 1
    for obj in objs:
        if isinstance(obj, int | float):
            c *= obj
        elif isinstance(obj, list | tuple):
            c *= recursive_multiply(obj)
    return c


# print(recursive_multiply(numbers))


# def foo(a):
#     while a:
#         if a == 1:
#             foo(0)


# foo(1)


# def decorator(a):
#     def wrapper(b):
#         return a * b
#
#     return wrapper


def decorator(func):
    def wrapper(*args, **kwargs):
        print("pre process")
        result = func(*args, **kwargs)
        print("post process")
        return result

    return wrapper


@decorator
def foo(a, b):
    return a * b


# print(foo(4, 5))
# decorated_foo = decorator(foo)


def logging(filename):
    def _logging(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, "a", encoding="utf-8") as file:
                file.write(f"{func.__name__}: {args=} {kwargs=}: {result}\n")
            return result

        return wrapper

    return _logging


@logging(filename="multiply.log")
def multiply(*args):
    c = 1
    for arg in args:
        c *= arg
    return c


@logging(filename="summ.log")
def summ(*args):
    s = 0
    for arg in args:
        s += arg
    return s


print(multiply(2, 4, 6))
print(summ(1, 3, 5))
