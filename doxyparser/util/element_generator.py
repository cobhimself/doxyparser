import pathlib
import sys
from xmlschema import XMLSchema
import os
import inflect
from doxyparser.util.generator.type import Type, SIMPLE, ENUMS, BOOLS, COMPLEX, PLACEHOLDER, ANY
from doxyparser.util.generator.element import Element
from doxyparser.util.generator.classdef import ClassDef
from doxyparser.util.generator.config import Config

class ElementGenerator():
    type_cache = {}
    element_cache = []

    def __init__(self, xsd):
        self._root = str(pathlib.Path(__file__).parent.parent)
        self._xmldir = self._root + '/../test/_sample_data/_build/php/xml/'
        self._config = Config(
            str(pathlib.Path(self._root + '/util/generator/config.yml')),
            xsd
        )
        self._xsd = xsd
        self._schema = XMLSchema(self._get_xsd_file_path(xsd))

    @staticmethod
    def _write(path, content):
        f = open(path, 'w')
        f.write(content)
        f.close()

    def _get_xsd_file_path(self, xsd):
        return str(pathlib.Path(f'{self._xmldir}/{xsd}.xsd').resolve())

    def _get_elements_dir(self, xsd):
        return self._root + f'/{xsd}/elements/'

    def _get_types_dir(self, xsd):
        return self._root + f'/{xsd}/types/'

    def generate(self):
        self._write_elements()

    def generate_config(self):
        self._compile_types()
        self._compile_elements()
        self._write_config()

    def _compile_types(self):
        for com in self._schema.complex_types:
            self.type_cache[com.name] = Type(com)

    def _compile_elements(self):
        # Global elements
        for element in self._schema.elements.values():
            node_type = self.type_cache[element.type.name]
            self.element_cache.append(Element(element, node_type))

    def _get_type(self, type_name):

        my_type = self._schema.types.get(type_name)
        if my_type is None:
            raise AttributeError(f'Unable to find type with name {type_name}')

        return my_type

    def _get_type_definition(self, type_name):
        my_type = self._get_type(type_name)
        return my_type.tostring()

    def _get_type_as_class(self, type_name):
        config = self._config
        new_class = ClassDef(self._xsd)
        new_class.add_import('from ...node import Node')
        new_class.extends('Node')
        doc = f'Model representation of a doxygen {type_name} type.' + "\n\n"
        doc += "Type XSD:\n\n"
        doc += self._get_type_definition(type_name)
        new_class.set_class_doc(doc)

        #Attributes
        attributes = config.get_type_attributes(type_name)
        for category, category_config in attributes.items():
            for attr_name in category_config:
                if category is SIMPLE:
                    new_class.add_decorator(f"@attr('{attr_name}'')")
                elif category is BOOLS:
                    new_class.add_decorator(f"@bool('{attr_name}''")

        #Elements
        elements = config.get_type_elements(type_name)
        # Order by category
        categories = sorted(elements)
        for category in categories:
            category_config = elements.get(category)
            # The items in these categories are just element names, not types
            if category in [ANY, PLACEHOLDER, SIMPLE]:
                for elem_name in category_config:
                    new_class.add_decorator(f"@element('{elem_name}', '{category}')")
            else:
                for elem_name, elem_type_name in category_config.items():
                    if category == COMPLEX:
                        if config.type_has_enum_attributes(elem_type_name):
                            enum_attrs = config.get_type_enum_attributes(elem_type_name)
                            for attr, enums in enum_attrs.items():
                                collection = f"@collection('{elem_name}', '/[@{attr}={{}}]', {{\n"
                                for enum in enums:
                                    collection += f"    '{inflect.engine().plural(enum.replace('-', '_'))}': '{enum}',\n"
                                collection += "})"
                                new_class.add_decorator(collection)
                        else:
                            new_class.add_decorator(f"@element('{elem_name}', '{elem_type_name}')")
                    else:
                        raise Exception(f'Unknown element config category {category}')

        return new_class


    def _get_element_as_class(self, xsd_name, element_name):
        pass

    def _write_elements(self):
        config = self._config.load()
        for xsd_name in config.get_xsd_names():
            types_dir = self._get_types_dir(xsd_name)
            elements_dir = self._get_elements_dir(xsd_name)

            os.makedirs(types_dir, exist_ok=True)
            os.makedirs(elements_dir, exist_ok=True)

            #Types
            for type_name in config.get_types().keys():
                ElementGenerator._write(
                    types_dir + type_name + '.py',
                    str(self._get_type_as_class(type_name))
                )

            #Elements
            for element_name in config.get_elements().keys():
                ElementGenerator._write(
                    elements_dir + element_name + '.py',
                    str(self._get_element_as_class(xsd_name, element_name))
                )

    def _write_config(self):
        #if config is None:
        config = self._config.load()

        #Types
        for name, node_type in self.type_cache.items():
            config.add_type_config(name, node_type)

        #Elements
        for element in self.element_cache:
            name = element.get_name()
            config.add_element_config(name, element.get_type_local_name())

        self._config.save()

if __name__ == "__main__":
    args = sys.argv
    generator = ElementGenerator(args[1])
    operation = args[2]

    if operation == 'config':
        generator.generate_config()
    elif operation == 'elements':
        generator.generate()
    else:
        print('Unknown operation!')
