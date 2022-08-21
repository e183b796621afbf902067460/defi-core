from threading import Thread
from concurrent.futures import Future


def threadmethod(fn):

    def futurefunc(func, ft, *args, **kwargs):
        ret = func(*args, **kwargs)
        ft.set_result(ret)

    def wrapper(*args, **kwargs):
        ft = Future()
        Thread(target=futurefunc, args=(fn, ft, *args, kwargs)).start()
        return ft

    return wrapper
