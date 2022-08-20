def yieldmethod(func):
    def wrapper(self, *args, **kwargs):
        for elem in func(self, *args, **kwargs):
            if elem:
                return elem
    return wrapper
