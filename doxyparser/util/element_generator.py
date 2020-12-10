import pathlib
import sys
from xmlschema import XMLSchema
import os
from doxyparser.util.generator import cache
from doxyparser.util.generator.classdef import ElementClassDef, TypeClassDef, GroupClassDef
from doxyparser.util.generator.config import Config

class ElementGenerator():

    def __init__(self, xsd):
        self._root = str(pathlib.Path(__file__).parent.parent)
        self._xmldir = self._root + '/../test/_sample_data/_build/php/xml/'
        self._config = Config(
            str(pathlib.Path(self._root + '/util/generator/config.yml')),
            xsd
        )
        self._xsd = xsd
        self._schema = None

    def load_schema(self, xsd):
        self._schema = XMLSchema(self._get_xsd_file_path(xsd))

    @staticmethod
    def _write(path, content):
        f = open(path, 'w')
        f.write(content)
        f.close()

    def _get_xsd_file_path(self, xsd):
        return str(pathlib.Path(f'{self._xmldir}/{xsd}.xsd').resolve())

    def _get_xsd_dir(self, xsd):
        return self._root + f'/{xsd}/'

    def _get_elements_dir(self, xsd):
        return self._root + f'/{xsd}/elements/'

    def _get_types_dir(self, xsd):
        return self._root + f'/{xsd}/types/'

    def _get_groups_dir(self, xsd):
        return self._root + f'/{xsd}/groups/'

    def generate(self):
        self._write_elements()

    def generate_config(self):
        self.load_schema(self._xsd)
        self._compile_groups()
        self._compile_types()
        self._compile_elements()
        self._write_config()

    def _compile_groups(self):
        for group in self._schema.groups.values():
            cache.add_group(group)

    def _compile_types(self):
        for com in self._schema.complex_types:
            cache.add_type(com)

    def _compile_elements(self):
        # Global elements
        for element in self._schema.elements.values():
            cache.add_element(element)

    def _get_type(self, type_name):
        my_type = self._schema.types.get(type_name)
        if my_type is None:
            raise AttributeError(f'Unable to find type with name {type_name}')

        return my_type

    def _get_group(self, group_name):
        my_group = self._schema.groups.get(group_name)
        if my_group is None:
            raise AttributeError(f'Unable to find group with name {group_name}')

        return my_group

    def _get_element(self, element_name):
        my_element = self._schema.elements.get(element_name)
        if my_element is None:
            raise AttributeError(f'Unable to find element with name {element_name}')

        return my_element

    def _get_type_definition(self, type_name):
        return self._get_type(type_name).tostring()

    def _get_element_definition(self, element_name):
        return self._get_element(element_name).tostring()

    def _get_group_definition(self, group_name):
        return self._get_group(group_name).tostring()

    def _write_package_folders(self, dirs):
        for d in dirs:
            os.makedirs(d, exist_ok=True)
            init = pathlib.Path(d + '__init__.py')
            if not init.exists():
                init.touch()

    def _write_elements(self):
        config = self._config.load()
        for xsd_name in config.get_xsd_names():
            self.load_schema(xsd_name)
            config.set_xsd(xsd_name)
            groups_dir = self._get_groups_dir(xsd_name)
            types_dir = self._get_types_dir(xsd_name)
            elements_dir = self._get_elements_dir(xsd_name)

            dirs = []

            groups = config.get_groups()
            if len(groups) > 0:
                dirs.append(groups_dir)

            types = config.get_types()
            if len(types) > 0:
                dirs.append(types_dir)

            elements = config.get_elements()
            if len(elements) > 0:
                dirs.append(elements_dir)

            if len(dirs) > 0:
                dirs.append(self._get_xsd_dir(xsd_name))

            self._write_package_folders(dirs)

            #Groups
            for group_name in groups.keys():
                class_def = GroupClassDef(
                    group_name,
                    self._config,
                    self._get_group_definition(group_name)
                )
                self._write(
                    groups_dir + class_def.get_file_name(group_name) + '.py',
                    str(class_def)
                )

            #Types
            for type_name in types.keys():
                class_def = TypeClassDef(
                    type_name,
                    self._config,
                    self._get_type_definition(type_name)
                )
                self._write(
                    types_dir + class_def.get_file_name(type_name) + '.py',
                    str(class_def)
                )

            #Elements
            for element_name in elements.keys():
                class_def = ElementClassDef(
                    element_name,
                    self._config,
                    self._get_element_definition(element_name)
                )
                ElementGenerator._write(
                    elements_dir + class_def.get_file_name(element_name) + '.py',
                    str(class_def)
                )

    def _write_config(self):
        #if config is None:
        config = self._config.load()

        #Groups
        for name, group_type in cache.get_group_cache().items():
            config.add_group_config(name, group_type)

        #Types
        for name, node_type in cache.get_type_cache().items():
            config.add_type_config(name, node_type)

        #Elements
        for element in cache.get_element_cache():
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
