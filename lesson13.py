# from enum import IntEnum
#
# from sqlalchemy import Column, INT, TIMESTAMP, Enum, ForeignKey, create_engine, select, insert
# from sqlalchemy.orm import DeclarativeBase, sessionmaker, relationship, joinedload
# from sqlalchemy.sql import func
#
#
# class TaskStatus(IntEnum):
#     TODO: int = 1
#     IN_PROGRESS: int = 2
#     DONE: int = 3
#
#
# class Base(DeclarativeBase):
#     ...
#
#
# class Project(Base):
#     __tablename__ = "project"
#
#     id = Column(INT, primary_key=True)
#
#
# class User(Base):
#     __tablename__ = "user"
#
#     id = Column(INT, primary_key=True)
#
#
# class Task(Base):
#     __tablename__ = "task"
#
#     id = Column(INT, primary_key=True)
#     author_id = Column(INT, ForeignKey("user.id"), nullable=False)
#     executor_id = Column(INT, ForeignKey("user.id"), nullable=False)
#     start_date = Column(TIMESTAMP, nullable=False)
#     end_date = Column(TIMESTAMP, nullable=False)
#     status = Column(Enum(TaskStatus), nullable=False, default=TaskStatus.TODO)
#
#
# engine = create_engine("sqlite:///db.db")
#
# stmt = select(Task, User).join(User, Task.executor_id == User.id)
# stmt = stmt.filter(Task.status != TaskStatus.DONE)
# stmt = stmt.filter(Task.end_date < func.now())
#
# session_maker = sessionmaker(bind=engine)
#
# # with session_maker() as session:
# #     objs = session.scalars(select(User)).all()
# #     print(objs)
# #     session.execute(
# #         insert(User).values([{"id": 1}, {"id": 2}, {"id": 3}])
# #     )
# #     session.commit()
# from random import randint
# from threading import *
# from time import sleep
# from queue import Queue, LifoQueue, PriorityQueue
#
#
# print_lock = RLock()
# s = Semaphore(value=3)
# b = Barrier(parties=3)
# e = Event()
# l = local()
# q = PriorityQueue()

# def ping():
#     # b.wait(timeout=1)
#     for _ in range(10):
#         with print_lock:
#             print(current_thread().name)
#         sleep(1)
#
#
# def pong():
#     # b.wait(timeout=1)
#     for _ in range(10):
#         with print_lock:
#             print(current_thread().name)
#         sleep(1)


# threads = [Thread(target=ping if i % 2 else pong) for i in range(10)]
# for thread in threads:
#     thread.start()

# def foo():
#     for _ in range(10):
#         obj = (randint(1, 10), f"{randint(1, 10)}")
#         sleep(0.5)
#         print(f"{obj=}")
#         q.put(obj)
#
#
# def bar():
#     for _ in range(10):
#         sleep(1)
#         print(q.get())
#
#
# t1 = Thread(target=foo)
# t2 = Thread(target=bar)
# t1.start()
# t2.start()
# from multiprocessing import Process
#
#
# def bar():
#     print("BAR")
#
#
# def foo():
#     p = Process(target=bar)
#     p.start()
#
#
# if __name__ == '__main__':
#     # foo()
#     p = Process(target=foo)
#     p.start()
from asyncio import create_task, run, current_task, sleep


async def foo():
    for _ in range(10):
        print(current_task().get_name())


async def bar():
    tasks = [create_task(foo()) for _ in range(10)]
    for task in tasks:
        await task


class AsyncIterator:

    def __aiter__(self):
        return self

    async def __anext__(self):
        return "async"

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb): ...


# async def main():
#     async with AsyncIterator() as ai:
#         ...
# async for i in AsyncIterator():
#     print(i)


def wrapper(func):
    async def wrapped(*args, **kwargs):
        return await func(*args, **kwargs)

    return wrapped


from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


# async_engine = create_async_engine("postgresql+asyncpg://admin:admin:0.0.0.0:5432/admin")
async_engine = create_async_engine("sqlite+aiosqlite:///db.db")
async_session_maker = async_sessionmaker(bind=async_engine)


# async def main():
#     async with async_session_maker() as session:
#         session.add()
#         await session.commit()
#         session.execute()
#         session.scalars()
#         session.scalar()
