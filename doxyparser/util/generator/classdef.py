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

This module contains helpers for creating python class definitions for the
generated doxyparser xsd library.
"""
import re
from textwrap import dedent
import inflect
from ..wrap import wrap
from .config import SIMPLE, BOOLS, COMPLEX, PLACEHOLDER, ANY


class ClassDef():
    """
    Class used to construct a class to be generated.
    """

    HEAD_COMMENT = """
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

    This class has been auto-generated. To add/modify functionality, extend it.
    See util/generator/element_generator.py"""

    def __init__(self, name, config, definition):
        self._name = name
        self._config = config
        self._definition = definition
        self._import_lines = []
        self._decorators = []
        self._doc = ''
        self._supers = []

    def get_config(self):
        """Get the configuration data to generate classes from.

        Returns:
            Config: The config object
        """
        return self._config

    def get_definition(self):
        """Get the definition of the element represented by this class.

        Returns:
            str: The xml representation of the element
        """
        return self._definition

    def get_name(self):
        """Get the name of the element this class represents.

        Returns:
            str
        """
        return self._name

    def determine_extends(self, relative_path, supers=None):
        """Determine what class (or classes) this class should extend based
        upon the list of super class names.

        Args:
            relative_path (str): The relative path to prepend to the super class' name.
            supers (list): The list of super class names this class should extend.
        """
        if supers is not None and len(supers) > 0:
            for sup in supers:
                class_name = self.get_class_name(sup)
                self.add_import(
                    f'from {relative_path}{self.get_file_name(sup)} import {class_name}')
                self.extends(class_name)
        else:
            self.add_import('from ....node import Node')
            self.extends('Node')

    def determine_decorator_include(self):
        """Determine the different includes necessary for the decorators this
        class uses.
        """
        decorators = self._decorators
        seen = []
        regex = r"@(.*)\("

        for decorator in decorators:
            matches = re.search(regex, decorator)
            if matches:
                match = matches.group(1)
                if match not in seen:
                    seen.append(match)

        if len(seen) > 0:
            self.add_import('from ....decorators import ' + ', '.join(seen))

    @staticmethod
    def get_file_name(name):
        """Get the file name of this class.

        Args:
            name (str): The name of this class to create a file name for.

        Returns:
            str: The file name this class should have.
        """
        return ''.join(['_'+x.lower() if x.isupper() else x for x in name]).strip('_')

    def add_import(self, import_line):
        """Add an import to this class.

        Args:
            import_line (str): An import line to add to this class.
        """
        self._import_lines.append(import_line)

    def get_imports(self):
        """Get the imports this class definition has.

        Returns:
            str: A line separated list of imports.
        """
        return "\n".join(self._import_lines)

    def extends(self, name):
        """Add a class for this class to extend.

        Args:
            name (str): The name of the class this class should extend.
        """
        self._supers.append(name)

    def add_decorator(self, decorator):
        """Add a class decorator.

        Args:
            decorator (str): The decorator to add.
        """
        self._decorators.append(decorator)

    def get_decorators(self):
        """Get the final decorators output.

        Returns:
            str: A line separated string of storted decorator strings.
        """
        return "\n".join(sorted(self._decorators))

    def set_class_doc(self, doc):
        """Set the documentation the class should use.

        Args:
            doc (str): The documentation
        """
        self._doc = doc

    def get_module_doc(self):
        """Get the documentation the module should use.

        Returns:
            str: The documentation
        """
        return wrap('"""' + dedent(self.HEAD_COMMENT) + "\n" + '"""')

    def get_class_doc(self):
        """Get the documentation the class should use.

        Returns:
            str: The documentation
        """
        return wrap('"""' + self._doc + "\n" + '"""', '    ', '    ')

    @staticmethod
    def get_class_name(name):
        """Return the class name version of the given name.

        Args:
            name (str): The name to obtain the class name for.

        Returns:
            str: The class name
        """
        return name[0].upper() + name[1:]

    def get_extends(self):
        """Get a string representation of the classes this class should
            extend.

        Returns:
            str: The string of classes this class extends.
        """
        return ', '.join(self._supers)

    def build(self):
        """Build the class.

        This method must be defined by classes which extend this class.

        Raises:
            Exception: If a chile build method is not implemented.
        """
        raise Exception('Child classes must implement the build method!')

    def __str__(self):
        """Get the final string representation of this class definition.

        Returns:
            str: The final representation of the class.
        """
        self.build()
        self.determine_decorator_include()
        out = self.get_module_doc() + "\n"
        out += self.get_imports() + "\n\n"
        out += self.get_decorators() + "\n"
        out += f"class {self.get_class_name(self._name)}({self.get_extends()}):\n"
        out += self.get_class_doc()
        # final new line
        out += "\n"

        return out

    def add_attributes_to_class(self, attributes):
        """Add the given attributes to the decorators for this class.

        Args:
            attributes (dict): The attribute configuration.
        """
        for category, category_config in attributes.items():
            for attr_name in category_config:
                if category == SIMPLE:
                    self.add_decorator(f"@attr('{attr_name}')")
                elif category == BOOLS:
                    self.add_decorator(f"@boolattr('{attr_name}')")

    def add_elements_to_class(self, elements):
        """Add the given elements to the decorators for this class.

        Args:
            elements (dict): The element configuration.

        Raises:
            Exception: If we come across an element category we haven't
                prepared for.
        """
        # Order by category
        categories = sorted(elements)
        config = self.get_config()
        for category in categories:
            category_config = elements.get(category)
            # The items in these categories are just element names, not types
            if category in [ANY, SIMPLE]:
                for elem_name in category_config:
                    self.add_decorator(
                        f"@element('{elem_name}', '{category}')")
            elif category == PLACEHOLDER:
                if len(category_config) > 0:
                    decorator = "@placeholders([\n"
                    decorator += ",\n".join(
                        [f"    '{p}'" for p in category_config])
                    decorator += "\n])"
                    self.add_decorator(decorator)
            else:
                for elem_name, type_name in category_config.items():
                    if category == COMPLEX:
                        if config.type_has_enum_attributes(type_name):
                            self.add_collection_decorators(
                                elem_name, type_name)
                        else:
                            self.add_decorator(
                                f"@element('{elem_name}', '{type_name}')")
                    else:
                        raise Exception(
                            f'Unknown element config category {category}')

    def add_collection_decorators(self, elem_name, type_name):
        """Add collection decorators for the given element and type name.

        Args:
            elem_name (str): The name of the element
            type_name (str): The name of its type.
        """
        enum_attrs = self.get_config().get_type_enum_attributes(type_name)
        for attr, enums in enum_attrs.items():
            collection = f"@collection('{elem_name}', '/[@{attr}={{}}]', {{\n"
            for enum in enums:
                plural_key = inflect.engine().plural(enum.replace('-', '_'))
                collection += f"    '{plural_key}': '{enum}',\n"
            collection += "})"
            self.add_decorator(collection)


class TypeClassDef(ClassDef):
    """Class representing a Type class.
    """

    def build(self):
        config = self.get_config()
        type_name = self.get_name()
        child_groups = config.get_type_groups(type_name)
        self.determine_extends('..groups.', child_groups)
        doc = f'Model representation of a doxygen {type_name} type.' + "\n\n"
        doc += "Type XSD:\n\n"
        doc += self.get_definition()
        self.set_class_doc(doc)

        self.add_attributes_to_class(config.get_type_attributes(type_name))
        self.add_elements_to_class(config.get_type_elements(type_name))

        return self


class ElementClassDef(ClassDef):
    """Class representing an Element class.
    """

    def build(self):
        config = self.get_config()
        element_name = self.get_name()
        self.determine_extends(
            '..types.', [config.get_element_type(element_name)])
        doc = f'Model representation of a doxygen {element_name} element.' + "\n\n"
        doc += "Type XSD:\n\n"
        doc += self.get_definition()
        self.set_class_doc(doc)


class GroupClassDef(ClassDef):
    """Class representing a Group class.
    """

    def build(self):
        config = self.get_config()
        group_name = self.get_name()
        child_groups = config.get_group_groups(group_name)
        self.determine_extends('.', child_groups)
        doc = f'Model representation of a doxygen {group_name} group.' + "\n\n"
        doc += "Type XSD:\n\n"
        doc += self.get_definition()
        self.set_class_doc(doc)
        self.add_elements_to_class(config.get_group_elements(group_name))
