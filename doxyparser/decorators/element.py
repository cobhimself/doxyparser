from .decorator import Decorator
from ..loader import Loader

ELEMENTS = 'elements'

class Element(Decorator):
    def __init__(self, tag_name, tag_type):
        super().__init__()
        self._tag_name = tag_name
        self._tag_type = tag_type

    def do(self):
        self._add_tag_element()
        self._add_element_method()

    def _add_tag_element(self):
        # Make sure we have a collection ready
        elements = self.provide(self.get_meta(), ELEMENTS, {})

        # Add the element type data
        self.provide(elements, self._tag_name, {'type': self._tag_type})

    @staticmethod
    def _getter(fn_name, tag_name, tag_type):
        def get_element(self):
            return self.get_child(tag_name, tag_type)
        get_element.__name__ = fn_name

        return get_element

    def _add_element_method(self):
        xsd = self.get_xsd_from_cls()
        name = self._tag_name
        tag_class = Loader.load_tag_class(xsd, name)

        doc = f"""Return child {name} element

        Returns:
            {tag_class}: The model representing the {name}.
        """
        fn_name = f'get_{name}'
        self.add_method_to_cls(
            fn_name,
            self._getter(fn_name, name, tag_class),
            doc
        )
