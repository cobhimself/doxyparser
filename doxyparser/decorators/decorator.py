META = '_meta'

class Decorator():
    def __init__(self):
        self._cls = None

    def __call__(self, cls):
        self._cls = cls

        #Make sure our classes have the meta dict
        if getattr(self._cls, META, None) is None:
            setattr(self._cls, META, {})

        self.do()
        return self._cls

    def do(self):
        raise Exception('The do method MUST be implemented!')

    def get_class(self):
        return self._cls

    def get_meta(self, key = None):
        meta = getattr(self._cls, META)

        if None is key:
            return meta

        return meta.get(key)

    def set_meta(self, key, value):
        meta = self.get_meta(self._cls)

        meta[key] = value

    def add_method_to_cls(self, fn_name, getter, doc):
        getter.__doc__ = doc
        setattr(self._cls, fn_name, getter)

    @staticmethod
    def provide(data, key, default):
        if data.get(key) is None:
            data[key] = default

        return data[key]

    def get_xsd_from_cls(self):
        return self._cls.__module__.split('.')[2]