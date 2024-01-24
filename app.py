def foo():
    return foo()


class Singleton(object):
    __slots__ = ("__instance", )
