from xml.etree.ElementTree import tostring
import textwrap
from ..wrap import wrap
from .element import Element
from .attribute import Attribute
from .super import Super

class Type(Super):

    head = textwrap.dedent("""
    from ...node import Node

    {attr_decorators}
    {elem_decorators}
    class {name}(Node):
        \"\"\"Model representation of a doxygen {name}

        XSD for this type:

        {definition}
        \"\"\"
    """).lstrip()

    def __init__(self, element):
        super().__init__(element)
        self._attr = {}
        self._elem = {}

    def get_attributes(self):
        if len(self._attr) == 0:
            for attr_name, attr in self._definition.attributes.items():
                self._attr[attr_name] = Attribute(attr)

        return self._attr

    def get_elements(self):
        if len(self._elem) == 0:
            for elem in self._definition.content.iter_elements():
                self._elem[elem.name] = Element(elem, elem.type)

        return self._elem

    def get_as_class(self):
        name = self._definition.name

        attr_decorators = [
            a.get_decorator()
            for a in self.get_attributes().values()
        ]

        elem_decorators = [
            e.get_decorator()
            for e in self.get_elements().values()
        ]

        definition = tostring(
            self._definition.schema_elem,
            encoding='unicode',
            method='xml'
        )

        head = self.head.format(
            name=name,
            attr_decorators=wrap("\n".join(attr_decorators), '', ''),
            elem_decorators="\n".join(elem_decorators),
            definition=wrap(definition).strip()
        )

        return head