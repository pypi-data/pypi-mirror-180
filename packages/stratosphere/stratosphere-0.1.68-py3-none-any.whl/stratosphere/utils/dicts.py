import itertools


class ObjectDictionary(dict):
    def __init__(self, *args, **kwargs):
        if args == (None,) and kwargs == {}:
            super().__init__()
        else:
            super().__init__(*args, **kwargs)

    def __reduce__(self):
        return self.__class__, (dict(self),)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key)

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError:
            raise AttributeError(key)


def product_dict(**kwargs):
    keys = kwargs.keys()
    vals = kwargs.values()
    for instance in itertools.product(*vals):
        yield dict(zip(keys, instance))
