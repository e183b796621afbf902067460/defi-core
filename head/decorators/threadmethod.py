from threading import Thread, active_count
from concurrent.futures import Future
from functools import wraps


def threadmethod(fn):

    def futurefunc(func, ft, *args, **kwargs):
        ret = func(*args, **kwargs)
        ft.set_result(ret)

    @wraps(fn)
    def wrapper(*args, **kwargs):
        ft = Future()
        t = Thread(target=futurefunc, args=(fn, ft, *args, *kwargs.values()))
        t.start()
        return ft

    return wrapper
