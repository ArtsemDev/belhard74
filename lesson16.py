from typing import Callable

from httpx import Client, Response, codes
from pydantic import BaseModel


def is_palindrome(text: str) -> bool:
    return text.lower() == text[::-1].lower()


class SingleTone(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls in cls._instances:
            return cls._instances.get(cls)

        instance = super().__call__(*args, **kwargs)
        cls._instances[cls] = instance
        return instance


class A(metaclass=SingleTone):
    ...


from abc import ABC, abstractmethod


class AbstractApiMethod(ABC):

    @property
    @abstractmethod
    def endpoint(self):
        ...

    @property
    @abstractmethod
    def method(self):
        ...


class AbstractApiFactory(ABC):

    @abstractmethod
    def create(self) -> AbstractApiMethod:
        ...


class YandexGetMethod(AbstractApiMethod):

    @property
    def endpoint(self):
        return "/musics"

    @property
    def method(self):
        return "GET"


class YandexAPI(AbstractApiFactory):

    def create(self) -> YandexGetMethod:
        return YandexGetMethod()


class AtlassianAPI:

    def get_issue(self, issue_key) -> dict:
        ...


class AtlassianAPIAdapter(AtlassianAPI):

    def issue(self, issue_key: str) -> BaseModel:
        return BaseModel(**self.get_issue(issue_key=issue_key))


class Folder:
    endpoint = "/folder"
    method = "GET"

    def __init__(self, request: Callable):
        self.request = request

    def __call__(self, name) -> dict:
        response = self.request(
            url="/folder",
            method="GET",
            params={"name": name}
        )
        if codes.is_success(value=response.status_code):
            return response.json()


class YandexDisk:

    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password
        self.client = Client()

    def request(self, url, method, json=None, params=None, **kwargs) -> Response:
        return self.client.request(
            method=method,
            url=url,
            params=params,
            json=json,
            **kwargs
        )

    @property
    def folder(self):
        return Folder(request=self.request)


class Dispatcher:

    def __init__(self):
        self.dispatchers = []
        self.handlers = {}

    def __call__(self, message: str):
        def wrapper(func):
            self.handlers[message] = func
            return func
        return wrapper

    def error(self):
        print("ERROR")

    def include_dispatcher(self, dispatcher: "Dispatcher"):
        self.dispatchers.append(dispatcher)

    def process(self, message):
        for msg, handler in self.handlers.items():
            if message == msg:
                return handler()
        else:
            for dispatcher in self.dispatchers:
                response = dispatcher.process(message=message)
                if response:
                    return response


dp1 = Dispatcher()
dp2 = Dispatcher()
dp1.include_dispatcher(dispatcher=dp2)


@dp1(message="foo")
def foo():
    print("FOO")


@dp2(message="bar")
def bar():
    print("BAR")


@dp1(message="baz")
def baz():
    print("BAZ")


msg = "foo"
dp1.process(message=msg)
