from .buildable import Buildable

class Group(Buildable):
    def __init__(self, definition):
        super().__init__(definition)
        self._elements = None
        self._groups = None

    def get_name(self):
        return self.get_definition().name