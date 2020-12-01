import pathlib
import sys
from xmlschema import XMLSchema
import os
from doxyparser.util.generator.type import Type
from doxyparser.util.generator.element import Element


class ElementGenerator():
    type_cache = {}
    element_cache = {}

    def __init__(self, xsd):
        root = str(pathlib.Path(__file__).parent.parent)
        xmldir = root + '/../test/_sample_data/_build/php/xml/'
        self._xsd_file = str(pathlib.Path(f'{xmldir}/{xsd}.xsd').resolve())
        self._xsd = xsd
        self._elements_dir = root + f'/{xsd}/elements/'
        self._types_dir = root + f'/{xsd}/types/'
        self._schema = XMLSchema(self._xsd_file)

    def generate(self):
        self._compile_types()
        self._compile_elements()
        self._write()

    def _compile_types(self):
        for com in self._schema.complex_types:
            self.type_cache[com.name] = Type(com)

    def _compile_elements(self):
        # Global elements
        for element_tag, element in self._schema.elements.items():
            node_type = self.type_cache[element.type.name]
            self.element_cache[element_tag] = Element(element, node_type)

        # Elements in types
        for node_type in self.type_cache.values():
            for element_tag, element in node_type.get_elements().items():
                if not element.is_text_only():
                    self.element_cache[element_tag] = element

    def _write(self):
        #Types
        for name, node_type in self.type_cache.items():
            content = node_type.get_as_class()
            os.makedirs(self._types_dir, exist_ok=True)
            out = self._types_dir + name.lower() + '.py'
            f = open(out, 'w')
            f.write(content)
            f.close()

        #Elements
        for name, element in self.element_cache.items():
            content = element.get_as_class()
            os.makedirs(self._elements_dir, exist_ok=True)
            out = self._elements_dir + name.lower() + '.py'
            f = open(out, 'w')
            f.write(content)
            f.close()


if __name__ == "__main__":
    args = sys.argv
    ElementGenerator(args[1]).generate()