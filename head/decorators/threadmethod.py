from threading import Thread, active_count
from concurrent.futures import Future


def threadmethod(fn):

    def futurefunc(func, ft, *args, **kwargs):
        ret = func(*args, **kwargs)
        ft.set_result(ret)

    def wrapper(*args, **kwargs):
        ft = Future()
        t = Thread(target=futurefunc, args=(fn, ft, *args, *kwargs.values()))
        t.start()
        return ft

    return wrapper
