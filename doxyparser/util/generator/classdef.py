from ..wrap import wrap
from textwrap import dedent
from doxyparser.util.generator.config import SIMPLE, BOOLS, COMPLEX, PLACEHOLDER, ANY
import inflect

class ClassDef():

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
        return self._config

    def get_definition(self):
        return self._definition

    def get_name(self):
        return self._name

    def determine_extends(self, relative_path, supers):
        if len(supers) > 0:
            for sup in supers:
                class_name = self.get_class_name(sup)
                self.add_import(f'from {relative_path}{self.get_file_name(sup)} import {class_name}')
                self.extends(class_name)
        else:
            self.add_import('from ...node import Node')
            self.extends('Node')

    @staticmethod
    def get_file_name(name):
        return ''.join(['_'+x.lower() if x.isupper() else x for x in name]).strip('_')

    def add_import(self, import_line):
        self._import_lines.append(import_line)

    def get_imports(self):
        return "\n".join(self._import_lines)

    def extends(self, name):
        self._supers.append(name)

    def add_decorator(self, decorator):
        self._decorators.append(decorator)

    def get_decorators(self):
        return "\n".join(sorted(self._decorators))

    def set_class_doc(self, doc):
        self._doc = doc

    def get_module_doc(self):
        return wrap('"""' + dedent(self.HEAD_COMMENT) + "\n" + '"""')

    def get_class_doc(self):
        return wrap('"""' + self._doc + "\n" + '"""', '    ', '    ')

    @staticmethod
    def get_class_name(name):
        return name[0].upper() + name[1:]

    def get_extends(self):
        return ', '.join(self._supers)

    def build(self):
        raise Exception('Child classes must implement the build method!')

    def __str__(self):
        self.build()
        out = self.get_module_doc() + "\n"
        out += self.get_imports() + "\n\n"
        out += self.get_decorators() + "\n"
        out += f"class {self.get_class_name(self._name)}({self.get_extends()}):\n"
        out += self.get_class_doc()
        #final new line
        out += "\n"

        return out

    def add_attributes_to_class(self, attributes):
        for category, category_config in attributes.items():
            for attr_name in category_config:
                if category == SIMPLE:
                    self.add_decorator(f"@attr('{attr_name}')")
                elif category == BOOLS:
                    self.add_decorator(f"@boolattr('{attr_name}')")

    def add_elements_to_class(self, elements):
        # Order by category
        categories = sorted(elements)
        placeholders = []
        config = self.get_config()
        for category in categories:
            category_config = elements.get(category)
            # The items in these categories are just element names, not types
            if category in [ANY, SIMPLE]:
                for elem_name in category_config:
                    self.add_decorator(f"@element('{elem_name}', '{category}')")
            elif category == PLACEHOLDER:
                placeholders = category_config
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
                                self.add_decorator(collection)
                        else:
                            self.add_decorator(f"@element('{elem_name}', '{elem_type_name}')")
                    else:
                        raise Exception(f'Unknown element config category {category}')

        if len(placeholders) > 0:
            decorator = "@placeholders([\n"
            decorator += ",\n".join([f"    '{p}'" for p in placeholders])
            decorator += "\n])"
            self.add_decorator(decorator)

class TypeClassDef(ClassDef):
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
    def build(self):
        config = self.get_config()
        element_name = self.get_name()
        self.determine_extends('..types.', [config.get_element_type(element_name)])
        doc = f'Model representation of a doxygen {element_name} element.' + "\n\n"
        doc += "Type XSD:\n\n"
        doc += self.get_definition()
        self.set_class_doc(doc)

class GroupClassDef(ClassDef):
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
