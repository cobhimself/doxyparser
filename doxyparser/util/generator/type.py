from xml.etree.ElementTree import tostring
from xmlschema.validators import XsdGroup
import textwrap
from ..wrap import wrap, wrapxml
from .super import Super

class Type(Super):

    def __init__(self, element):
        super().__init__(element)
        self._attr = {}
        self._elem = {}

    def get_name(self):
        return self._definition.name

    def get_content(self):
        return self._definition.content

    def is_element_only(self):
        return self.get_content().is_element_only()

    def is_multiple(self):
        return self.get_content().is_multiple()

    def is_simple(self):
        #if not self._definition.is_simple():
        #    content = self.get_content()
        #    if isinstance(content, XsdGroup):
        #        return content.is_single()

        return self._definition.is_simple()

    def is_text_only(self):
        return self._definition.has_simple_content()

    def allows_elements_and_text(self):
        return self.get_content().has_mixed_content()

    def get_attributes(self):
        if len(self._attr) == 0:
            from .attribute import Attribute
            for attr_name, attr in self._definition.attributes.items():
                self._attr[attr_name] = Attribute(attr)

        return self._attr

    def get_elements(self):
        if len(self._elem) == 0:
            from .element import Element
            for elem in self._definition.content.iter_elements():
                self._elem[elem.name] = Element(elem, Type(elem.type))

        return self._elem

    def get_as_class(self):
        name = self._definition.name

        #Create our attr decorators
        attr_decorators = [
            a.get_decorator()
            for a in self.get_attributes().values()
        ]

        #Create our element decorators
        elem_decorators = [
            e.get_decorator()
            for e in self.get_elements().values()
        ]

        #Create our decorators import string
        decorators = []

        if len(attr_decorators) > 0:
            decorators.append('attr')

        needs_collection = False
        needs_element = False

        for elem_dec in elem_decorators:
            if elem_dec.startswith('@collection'):
                needs_collection = True
            elif elem_dec.startswith('@element'):
                needs_element = True

            if needs_collection and needs_element:
                break

        if needs_collection:
            decorators.append('collection')

        if needs_element:
            decorators.append('element')

        code = 'from ...node import Node'

        if len(decorators) > 0:
            code += "\nfrom ...decorators import " + ", ".join(decorators)

        code += "\n\n"

        if len(attr_decorators) > 0:
            code += "\n".join(attr_decorators) + "\n"


        if len(elem_decorators) > 0:
            code += "\n".join(elem_decorators) + "\n"

        code += f'class {name}(Node):' + "\n"
        class_comment = '"""' + "\n"
        class_comment += f"Model representation of a doxygen {name}\n\n"
        class_comment += "XSD for this type:\n\n"
        class_comment += wrapxml(self._definition.schema_elem) + "\n"
        class_comment += '"""'

        code += wrap(class_comment, '    ', '    ')

        #final new line
        code += "\n"

        return code