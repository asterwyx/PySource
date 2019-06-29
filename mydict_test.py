class Mydict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattribute__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Mydict' object has no attribute %s" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def __init_subclass__(cls):
        return super().__init_subclass__()