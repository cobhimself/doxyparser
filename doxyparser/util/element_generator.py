import pathlib
import sys
from xmlschema import XMLSchema
from .generator.element import Element
from .generator.type import Type


class ElementGenerator():
    type_cache = {}
    element_cache = {}
    root_cache = {}

    def __init__(self, xsd):
        root = str(pathlib.Path(__file__).parent.parent)
        xmldir = root + '/../test/_sample_data/_build/php/xml/'
        self._xsd_file = str(pathlib.Path('{}/{}.xsd'.format(xmldir, xsd)).resolve())
        self._xsd = xsd
        self._elements_dir = root + '/{xsd}/elements/'.format(xsd=xsd)
        self._types_dir = root + '/{xsd}/types/'.format(xsd=xsd)
        self._schema = XMLSchema(self._xsd_file)

    def generate(self):
        self._compile_types()
        #self._compile_elements()
        self._write()

    def _compile_types(self):
        #for sim in self._schema.simple_types:
        #    self.type_cache[sim.name] = Type(sim)

        for com in self._schema.complex_types:
            self.type_cache[com.name] = Type(com)

        for root in self._schema.root_elements:
            self.root_cache[root.name] = Element(root, self.type_cache[root.type.name])


    def _compile_elements(self):
        for element_tag, element in self._schema.elements.items():
            node_type = self.type_cache[element.type.name]
            self.element_cache[element_tag] = Element(element, node_type)

    def _generate_types(self):

        for name, node_type in self.type_cache.items():
            attributes = node_type.get_attributes()

    def _write(self):
        #Types
        for name, node_type in self.type_cache.items():
            content = node_type.get_as_class()
            out = self._types_dir + name.lower() + '.py'
            f = open(out, 'w')
            f.write(content)
            f.close()
        #Components


if __name__ == "__main__":
    args = sys.argv
    ElementGenerator(args[1]).generate()