# # Абстракция
# # Наследование
#
# class User:
#
#     def __init__(self, first_name: str, email: str) -> None:
#         self.first_name = first_name.title()
#         self.email = email.lower()
#
#     def __str__(self) -> str:
#         return f"User first_name={self.first_name} email={self.email}"
#
#     def b(self, arg: int):
#         ...
#
#
# class A:
#
#     def __str__(self):
#         return "A"
#
#     def __len__(self):
#         return 5
#
#     def b(self, arg: str):
#         ...
#
#
# class Manager(A, User):
#
#     def work(self):
#         print("Work...")
#
#
# vasya = Manager(first_name="vasya", email="vasya@gmail.com")
# print(Manager.mro())
# # vasya.work()
#
#
# class B:
#     ...
#
#
# class C:
#
#     def __init__(self, b: B):
#         self.obj = b
#
# # Полиморфизм
#
#

class A:
    i: int = 0

    def __init__(self, name: str):
        self.name = name

    def foo(self):
        return self.name.upper()


class B(A):
    _i: int = 5

    def __init__(self, name: str, email: str):
        A.__init__(self=self, name=name)
        # super().__init__(name)
        self.email = email

    def foo(self):
        result = super().foo()
        return result * 2

    def __get(self, pk: int):
        return {1: "Hello", 2: "World", 3: "Python"}[pk]

    def get(self, pk: int | str):
        pk = int(pk)
        try:
            return self.__get(pk=pk)
        except KeyError:
            return None


# Инкапсуляция

# b = B(name="vasya", email="vasya@gmail.com")
# print(b.get("67"))
# print(b._B__get(3))  # noqa


class DebtCard:

    def __init__(self, number: str):
        self.__number = number

    # NEW
    @property
    def number(self):
        return self.__number[-4:]

    @number.setter
    def number(self, value: str):
        if len(value) != 16 or not value.isdigit():
            raise ValueError
        self.__number = value

    # OLD
    def get_number(self):
        return self.__number[-4:]

    def set_number(self, value: str):
        if len(value) != 16 or not value.isdigit():
            raise ValueError
        self.__number = value


# card = DebtCard(number="1234567887653456")
# print(card.number)
# card.number = "2345678641234629"
# print(card.number)


class User:
    __slots__ = ("first_name", "last_name")

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, value: str):
        self.first_name = value.split()[0]
        self.last_name = value.split()[1]


class Manager(User):
    __slots__ = ()


# vasya = Manager(first_name="Vasya", last_name="Pupkin")
# vasya.email = "vasya@gmail.com"
# print(vasya.email)


user = {
    "name": "Vasya",
    "email": "vasya@gmail.com"
}


# class User:
#     __slots__ = ("__name", "__email")
#
#     def __init__(self, name: str, email: str) -> None:
#         self.__email = email
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @property
#     def email(self):
#         return self.__email


from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    name: str
    email: str


from abc import ABC, abstractmethod


class AbstractView(ABC):

    @abstractmethod
    def get(self, request):
        ...

    @abstractmethod
    def post(self, request):
        ...

    @classmethod
    @abstractmethod
    def dispatch(cls, request):
        ...


class ListView(AbstractView):

    def get(self, request):
        pass

    def post(self, request):
        pass

    @classmethod
    def dispatch(cls, request):
        pass


# SOLID
# S - Single responsibility principle
# O - Open/Close principle
# L - Liskov substitution principle
# I - Interface segregation principle
# D - Dependency inversion principle


class AbstractPhone(ABC):

    @abstractmethod
    def call(self):
        ...


class SMSMixin:

    def sms(self):
        ...


class MobilePhone(SMSMixin, AbstractPhone):
    def call(self):
        pass

    def sms(self):
        pass


class StaticPhone(AbstractPhone):
    def call(self):
        pass


class AbstractMusic(ABC):

    @abstractmethod
    def get_music_by_name(self, name):
        ...


class YandexMusic(AbstractMusic):

    def get_music_by_name(self, name):
        print("LOGICA")


class Music(AbstractMusic):

    def __init__(self, music: YandexMusic):
        self.music = music

    def get_music_by_name(self, name):
        print("LOGICA")
        self.music.get_music_by_name(name=name)


class Engine:

    def __init__(self, volume, type_):
        self.volume = volume
        self.type = type_


class Car:

    def __init__(
            self,
            manufactory: str,
            engine: Engine
    ) -> None:
        self.manufactory = manufactory
        self.engine = engine


engine = Engine(volume="2500", type_="Gas")
car = Car(manufactory="Bowarskoe Musornoe Wedro", engine=engine)
mercedes = Car(manufactory="Mercedes", engine=engine)
