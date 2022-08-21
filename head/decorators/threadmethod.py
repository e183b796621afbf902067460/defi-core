from threading import Thread
from concurrent.futures import Future


def threadmethod(fn):

    def futurefunc(func, future, *args, **kwargs):
        ret = func(*args, **kwargs)
        future.set_result(ret)

    def wrapper(*args, **kwargs):
        future = Future()
        Thread(target=futurefunc, args=(fn, future, *args, kwargs)).start()
        return future

    return wrapper
