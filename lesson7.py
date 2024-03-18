"""Модуль содержащий код 7 занятия"""

from typing import Any


# users = {
#     1: {"name": "Name-1", "email": "email1"},
#     2: {"name": "Name-2", "email": ""},
#     3: {"name": "Name-3", "email": None},
#     4: {"name": "Name-4"},
# }
# # user_names_without_email = list(filter(lambda x: not x.get("email"), users.values()))
# # print(user_names_without_email)
# for user in users.values():  # type: dict
#     if not user.get("email"):
#         print(user.get("name"))


class User:
    """Класс представления информации о пользователе"""

    tablename = "user"

    @classmethod
    def change_tablename(cls, new_tablename):
        cls.tablename = new_tablename

    @staticmethod
    def multiply(a, b):
        return a * b

    def __init__(self, first_name, email, password, age):
        self.age = age
        self.password = password
        self.name = first_name
        self.email = email
        self.is_active = False
        # self.i = -1

    # def __iter__(self):
    #     self.i = -1
    #     return self
    #
    # def __next__(self):
    #     if self.i < len(self.password) - 1:
    #         self.i += 1
    #         return self.password[self.i]
    #     raise StopIteration

    def __str__(self):
        return f"name={self.name} email={self.email} is_active={self.is_active}"

    def __getitem__(self, item):
        return self.password[item]

    def __len__(self):
        return len(self.password)

    # def __bool__(self):
    #     return self.is_active

    def __int__(self):
        return self.age

    def __lt__(self, other):
        if isinstance(other, User):
            return self.age < other.age
        elif isinstance(other, (int, float)):
            return self.age < other
        raise TypeError(
            f"'<' not supported between instances of 'User' and '{type(other).__name__}'"
        )

    def __ge__(self, other):
        return not self < other

    def __add__(self, other):
        if isinstance(other, User):
            return self.age + other.age
        elif isinstance(other, (int, float)):
            return self.age + other
        raise TypeError(
            f"'+' not supported between instances of 'User' and '{type(other).__name__}'"
        )

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        if isinstance(other, User):
            self.age += other.age
            return self
        elif isinstance(other, (int, float)):
            self.age += other
            return self
        raise TypeError(
            f"'+=' not supported between instances of 'User' and '{type(other).__name__}'"
        )

    def set_name(self, new_name: str):
        self.name = new_name


# User.tablename = "admin"
# print(User.tablename)
# user1 = User(first_name="vasya", email="vasya@gmail.com", password="VeryStrongPassword1!", age=12)
# print(User.__class__)
# user1.__class__.tablename = "admin"
# print(User.tablename)
# print(user1.tablename)
# user1.tablename = "admin"
# print(user1.tablename)
# print(User.tablename)
# user2 = User(first_name="petya", email="petya@mail.ru", password="Qwerty1!", age=18)
# print(len(user1))
# user1 += 12
# print(user1.age)
# print(user1 + user2)
# print(user1.__add__(other=user2))
# print(User.__add__(self=user1, other=user2))
# print(user1[2])
# for j in user1:
#     print(j)


class Product:
    __slots__ = (
        "title",
        "description",
        "price",
    )

    def __init__(self, title: str, description: str, price: int | float) -> None:
        self.title = title
        self.description = description
        self.price = price

    def change_product_price(self, percent):
        self.price = self.price * (1 + percent)

    def __call__(self, *args, **kwargs):
        pass

    def __getitem__(self, item):
        pass

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass

    def __contains__(self, item):
        pass

    def __missing__(self, key):
        pass

    def __len__(self):
        return 1

    # def __getitem__(self, item):
    #     print(item)
    #     print(type(item))


product = Product(title="Laptop", description="Powerful!", price=1500)
# product.image = "/var/images/laptop.png"
# print(product.__dict__)
# print(product.image)
# product.change_product_price(percent=0.05)
# print(product.price)
# change_product_price(product=product, percent=0.05)
# change_product_price(product=product, percent=-0.05)
# print(product)
# a = slice(1, 10, 2)
# print("Hello world python"[a])


# print(print.__doc__)


def multiply(a: int, b: int) -> int:
    """Произведение 2 целых чисел

    :param a: Первый множитель
    :type a: int
    :param b: Второй множитель
    :type b: int
    :return: Результат произведения
    :rtype: int
    :raise TypeError: если один из множителей не число
    """
    return a * b


# print(multiply.__doc__)
class A:

    def __init__(self, b: bool) -> None:
        self.b = b
        self.c = True


numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# n = -2
# print(numbers[-n:])
# print(numbers[-n:] + numbers[:-n])


def rotate(objs: list[Any], n: int) -> list[Any]:
    """Rotate list

    :param objs: list for rotate
    :param n: step
    :return: rotated list
    """
    for _ in range(abs(n)):
        if n > 0:
            objs.insert(0, objs.pop(-1))
        else:
            objs.append(objs.pop(0))
    return objs
