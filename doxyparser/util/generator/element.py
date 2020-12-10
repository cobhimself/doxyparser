from .typeable import Typeable

class Element(Typeable):
    def __init__(self, element, node_type):
        self._attr = {}
        super().__init__(element, type_instance=node_type)

    def get_name(self):
        return self._definition.name

    def get_attributes(self):
        if len(self._attr) == 0:
            from .attribute import Attribute
            for attr_name, attr in self._definition.attributes.items():
                self._attr[attr_name] = Attribute(attr, self)

        return self._attr

    def get_attribute_by_name(self, name):
        return self._attr.get(name, None)
