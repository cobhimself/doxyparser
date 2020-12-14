"""
MIT License

Copyright (c) 2020 Collin Brooks

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import pathlib
import sys
import os
from xmlschema import XMLSchema
from doxyparser.util.generator import cache
from .generator.classdef import ElementClassDef, TypeClassDef, GroupClassDef
from .generator.config import Config


class ElementGenerator():
    """Class responsible for generating xsd-based configuration and classes
    """

    def __init__(self, xsd):
        self._root = str(pathlib.Path(__file__).parent.parent)
        self._xmldir = self._root + '/../test/_sample_data/_build/php/xml/'
        config_file = str(pathlib.Path(
            self._root + '/util/generator/config.yml'))
        self._config = Config(config_file)
        self._xsd = xsd
        self._xsd_out_dir = self._root + '/xsd/'
        self._schema = None

    def load_schema(self, xsd):
        """Load the schema for the given xsd file.

        Args:
            xsd (str): The xsd file name without the extension.
        """
        self._schema = XMLSchema(self._get_xsd_file_path(xsd))

    @staticmethod
    def _write(path, content):
        """Write the content to the file at the given path.

        Args:
            path (str): The location where we should write the content.
            content (str): The content to write.
        """
        file = open(path, 'w')
        file.write(content)
        file.close()

    def _get_xsd_file_path(self, xsd):
        """Get the file path for the given xsd file.

        Args:
            xsd (str): The name of the xsd file, without the extension, we
            want to get the path for.

        Returns:
            str: The file path for the xsd file.
        """
        return str(pathlib.Path(f'{self._xmldir}/{xsd}.xsd').resolve())

    def _get_xsd_dir(self):
        """Get the directory of the xsd root folder.

        Returns:
            str: The xsd root folder path.
        """
        return self._root + '/xsd/'

    def _get_dir_for_xsd(self, xsd):
        """Get the directory where we will put files relating to the given
        xsd name.

        Args:
            xsd (str): The name of the xsd without file extension.

        Returns:
            str: The directory where files for this xsd will be placed.
        """
        return self._get_xsd_dir() + f'/{xsd}/'

    def _get_elements_dir(self, xsd):
        """Get the elements directory for the given xsd.

        Args:
            xsd (str): The name of the xsd without file extension.

        Returns:
            str: The directory where elements will be placed for the given
                xsd.
        """
        return self._get_dir_for_xsd(xsd) + 'elements/'

    def _get_types_dir(self, xsd):
        """Get the types directory for the given xsd.

        Args:
            xsd (str): The name of the xsd without file extension.

        Returns:
            str: The directory where types will be placed for the given
                xsd.
        """
        return self._get_dir_for_xsd(xsd) + 'types/'

    def _get_groups_dir(self, xsd):
        """Get the groups directory for the given xsd.

        Args:
            xsd (str): The name of the xsd without file extension.

        Returns:
            str: The directory where groups will be placed for the given
                xsd.
        """
        return self._get_dir_for_xsd(xsd) + 'groups/'

    def generate(self):
        """Generate the classes based on our config.
        """
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
                dirs.append(self._get_xsd_dir())
                dirs.append(self._get_dir_for_xsd(xsd_name))

            self._write_package_folders(dirs)

            # Groups
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

            # Types
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

            # Elements
            for element_name in elements.keys():
                class_def = ElementClassDef(
                    element_name,
                    self._config,
                    self._get_element_definition(element_name)
                )
                ElementGenerator._write(
                    elements_dir +
                    class_def.get_file_name(element_name) + '.py',
                    str(class_def)
                )

    def generate_config(self):
        """Generate the config for our final class generation.
        """
        self.load_schema(self._xsd)
        self._compile_groups()
        self._compile_types()
        self._compile_elements()
        self._write_config()

    def _compile_groups(self):
        """Compile a cache of group data from our schema.
        """
        for group in self._schema.groups.values():
            cache.add_group(group)

    def _compile_types(self):
        """Compile a cache of type data from our schema.
        """
        for com in self._schema.complex_types:
            cache.add_type(com)

    def _compile_elements(self):
        """Compile a cache of global element data from our schema.
        """
        # Global elements
        for element in self._schema.elements.values():
            cache.add_element(element)

    def _get_type(self, type_name):
        """Search the schema for the given type.

        Args:
            type_name (str): The name of the type to get.

        Raises:
            AttributeError: If unable to find the given type.

        Returns:
            XsdType: The type.
        """
        my_type = self._schema.types.get(type_name)
        if my_type is None:
            raise AttributeError(f'Unable to find type with name {type_name}')

        return my_type

    def _get_group(self, group_name):
        """Search the schema for the given group.

        Args:
            group_name (str): The name of the group to get.

        Raises:
            AttributeError: If unable to find the given group.

        Returns:
            XsdGroup: The group.
        """
        my_group = self._schema.groups.get(group_name)
        if my_group is None:
            raise AttributeError(
                f'Unable to find group with name {group_name}'
            )

        return my_group

    def _get_element(self, element_name):
        """Search the schema for the given element.

        Args:
            element_name (str): The name of the element to get.

        Raises:
            AttributeError: If unable to find the given element.

        Returns:
            XsdElement: The element.
        """
        my_element = self._schema.elements.get(element_name)
        if my_element is None:
            raise AttributeError(
                f'Unable to find element with name {element_name}'
            )

        return my_element

    def _get_type_definition(self, type_name):
        """Return the xml definition of the given type.

        Args:
            type_name (str): The type to retrieve the raw xml for.

        Returns:
            str: The xml version of the given type.
        """
        return self._get_type(type_name).tostring()

    def _get_element_definition(self, element_name):
        """Return the xml definition of the given element.

        Args:
            element_name (str): The element to retrieve the raw xml for.

        Returns:
            str: The xml version of the given element.
        """
        return self._get_element(element_name).tostring()

    def _get_group_definition(self, group_name):
        """Return the xml definition of the given group.

        Args:
            group_name (str): The group to retrieve the raw xml for.

        Returns:
            str: The xml version of the given group.
        """
        return self._get_group(group_name).tostring()

    @staticmethod
    def _write_package_folders(dirs):
        """Make sure the given directories exist as well as their __init__.py
        files.

        Args:
            dirs (list): A list of directories to confirm exist.
        """
        for my_dir in dirs:
            os.makedirs(my_dir, exist_ok=True)
            init = pathlib.Path(my_dir + '__init__.py')
            if not init.exists():
                init.touch()

    def _write_config(self):
        """Create and write the configuration.
        """
        # if config is None:
        config = self._config.load()

        # Groups
        for name, group_type in cache.get_group_cache().items():
            config.add_group_config(name, group_type)

        # Types
        for name, node_type in cache.get_type_cache().items():
            config.add_type_config(name, node_type)

        # Elements
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
