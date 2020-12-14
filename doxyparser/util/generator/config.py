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
from yaml import load, dump

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

EXT = '.xsd'
XSD = 'xsd'
ATTRIBUTES = 'attributes'
ELEMENTS = 'elements'
GROUPS = 'groups'
TYPES = 'types'
ENUMS = 'enums'
PLACEHOLDER = 'placeholder'
ANY = 'any'
BOOLS = 'bools'
SIMPLE = 'simple'
COMPLEX = 'complex'
TYPE = 'type'
ENUMS = 'enums'


class Config():
    """Class which aids in the reading and writing of class generation for
    xsd-based classes.
    """

    def __init__(self, path):
        self._path = path
        self._config = None
        self._xsd = None

    def set_xsd(self, xsd):
        """Set the xsd name the config is to work with.

        Args:
            xsd (str): The name of the source xsd file without the extension.
        """
        self._provide(self._config[XSD], xsd, {})
        self._xsd = xsd

    def load(self):
        """Load the configuration found at the given path.

        Returns:
            self
        """
        if self._config is None:
            # Load the current configuration
            if pathlib.Path(self._path).exists():
                config_file = open(self._path, 'r')
                self._config = load(config_file, Loader=Loader)
                config_file.close()

            self._config = {} if self._config is None else self._config

        return self

    def save(self):
        """Save the configuration data to the configuration file.

        Returns:
            self
        """
        header = "#This file was autogenerated. See element_generator.py\n"
        config_file = open(self._path, 'w')
        config_file.write(header)
        dump(self._config, config_file)
        config_file.close()

        return self

    @staticmethod
    def _provide(data, key, default):
        """Provide the given data dictionary with a default value for the
        given key if no data exists at the key.

        Args:
            data (dict): A dictionary to provision
            key (str): The key where data should be provisioned.
            default (mixed): Whatever value the given key should have within
                 the data.

        Returns:
            dict: The provisioned dictionary.
        """
        if data.get(key) is None:
            data[key] = default

        return data

    def set_path(self, value, *path_parts):
        """Set the given value at the path rooted at the current xsd config
        level.

        This method makes it easy to travel into the configuration dictionary
        and provision each of the levels with preliminary data so the final
        level can have the given value data.

        This method returns the value given so, if the value is a dict or
        list, additional data can be placed within.

        Args:
            value (mixed): The value to place at the given path in the
                configuration dictionary.

        Returns:
            mixed: the given value
        """
        path_parts = list(path_parts)
        config = self.get_xsd_config()
        cur_config = config
        last_part = path_parts.pop()
        for part in path_parts:
            self._provide(cur_config, part, {})
            cur_config = cur_config[part]

        cur_config[last_part] = value

        return cur_config[last_part]

    def get_config(self, require_xsd=True):
        """Get the configuration for the current xsd.

        Raises:
            Exception: Raised if the current xsd has not been set.

        Returns:
            dict: The config dictionary rooted at the data within the XSD
                key.
        """
        self.load()
        self._provide(self._config, XSD, {})

        if require_xsd:
            if self._xsd is None:
                raise Exception('Unable to get configuration without setting xsd!')


        return self._config.get(XSD)

    def get_xsd_config(self):
        """Get the configuration for the current xsd.

        Returns:
            dict: the data for the current xsd
        """
        key = self._xsd
        config = self.get_config()

        self._provide(config, key, {})
        return config[key]

    def get_xsd_files(self):
        """Get a list of xsd files our config file knows about.

        Returns:
            list: The list of xsd files our config knows about.
        """
        return [file + EXT for file in self.get_xsd_names()]

    def get_xsd_names(self):
        """Get a list of xsd file names our config file knows about.

        Returns:
            list: The list of xsd files our config knows about without the
                file extension.
        """
        return self.get_config(False).keys()

    def get_types(self):
        """Get the TYPES for the current xsd.

        Returns:
            dict: Types keyed by type name with their data as values.
        """
        return self.get_xsd_config().get(TYPES, {})

    def get_groups(self):
        """Get the GROUPS for the current xsd.

        Returns:
            dict: Groups keyed by group name with their data as values.
        """
        return self.get_xsd_config().get(GROUPS, {})

    def get_elements(self):
        """Get the ELEMENTS for the current xsd.

        Returns:
            dict: Elements keyed by element name with their types as values.
        """
        return self.get_xsd_config().get(ELEMENTS, {})

    def get_element_type(self, element_name):
        """Get the type name for the element with the given name.

        Args:
            element_name (str): The element's name

        Returns:
            str|None: The type name if the element is known, None otherwise.
        """
        return self.get_elements().get(element_name)

    def get_type_config(self, type_name):
        """Get the type configuration for the type with the given name.

        Args:
            type_name (str): The type's name

        Returns:
            dict|None: The type's data if the type is known, None otherwise.
        """
        return self.get_types().get(type_name)

    def get_group_config(self, group_name):
        """Get the group configuration for the group with the given name.

        Args:
            group_name (str): The group's name

        Returns:
            dict: The group's data.
        """
        return self.get_groups().get(group_name, {})

    def get_group_groups(self, group_name):
        """Get the list of groups associated with the named group.

        Args:
            group_name (str): The name of the group to obtain child group
                names for.

        Returns:
            list: A list of child group names
        """
        return self.get_group_config(group_name).get(GROUPS, [])

    def get_type_groups(self, type_name):
        """Get the list of groups associated with the named type.

        Args:
            type_name (str): The name of the type to obtain child group
                names for.

        Returns:
            list: A list of child group names
        """
        return self.get_type_config(type_name).get(GROUPS, [])

    def get_type_attributes(self, type_name):
        """Return attribute data for the type with the given name.

        Args:
            type_name (str): The type to get attribute data for.

        Returns:
            dict: Attribute data for the given type name.
        """
        return self.get_type_config(type_name).get(ATTRIBUTES, {})

    def get_type_elements(self, type_name):
        """Return element data for the type with the given name.

        Args:
            type_name (str): The type to get element data for.

        Returns:
            dict: Element data for the given type name.
        """
        return self.get_type_config(type_name).get(ELEMENTS, {})

    def get_group_elements(self, group_name):
        """Return element data for the group with the given name.

        Args:
            group_name (str): The group to get element data for.

        Returns:
            dict: Element data for the given group name.
        """
        return self.get_group_config(group_name).get(ELEMENTS, {})

    def get_element_config(self, element_name):
        """Return element configuration for the element with the given name.

        Args:
            element_name (str): The element to get config data for.

        Returns:
            dict: Element configuration for the given element name.
        """
        return self.get_elements().get(element_name)

    def type_has_enum_attributes(self, type_name):
        """Determine whether or not the type with the given name has
        attributes with enum data.

        Args:
            type_name (str): The type to check.

        Returns:
            bool: True if the type has attributes with enum data. False
                otherwise.
        """
        return ENUMS in self.get_type_attributes(type_name).keys()

    def get_type_enum_attributes(self, type_name):
        """Get the list of attributes of this type which have enum data.

        Args:
            type_name (str): The name of the type to obtain enum attributes
                for.

        Returns:
            dict: A dictionary of attribute name keys with enum list values.
        """
        return self.get_type_attributes(type_name).get(ENUMS, {})

    def add_group_config(self, name, group):
        """Add group configuration to the xsd config

        Args:
            name (str): The name of the group
            group (Group): The group to add configuration details for
        """
        group_info = {}
        group_info[ELEMENTS] = self.get_element_info(group.get_elements())
        groups = group.get_groups()
        if len(groups) > 0:
            group_info[GROUPS] = [key for key in groups.keys()]

        self.set_path(group_info, GROUPS, name)

    def add_type_config(self, name, node_type):
        """Add type configuration to the xsd config

        Args:
            name (str): The name of the type
            node_type (Type): The type to add configuration details for
        """
        type_config = self.set_path({}, TYPES, name)
        attr_info = self.get_attr_info(node_type)
        elem_info = self.get_element_info(node_type.get_elements())
        group_info = self.get_group_info(node_type)

        if len(attr_info) > 0:
            type_config[ATTRIBUTES] = attr_info
        if len(elem_info) > 0:
            type_config[ELEMENTS] = elem_info
        if len(group_info) > 0:
            type_config[GROUPS] = group_info

    @staticmethod
    def get_group_info(node_type):
        """Compile doxyparser-specific information about the groups in
        the given node type.

        Args:
            node_type (Type): The Type to return information for

        Raises:
            Exception: If multiple groups exist in the Type, we don't support
                it yet.

        Returns:
            list: A list of group names in this Type
        """
        info = []
        groups = node_type.get_groups()

        if len(groups) > 1:
            raise Exception(
                'Multiple groups in a single node not supported yet!')

        for group in groups.values():
            info.append(group.get_name())

        return info

    def get_attr_info(self, node_type):
        """Compile doxyparser-specific information about the attributes in
        the given node type.

        Args:
            node_type (Type): The type to obtain attribute information about

        Returns:
            dict: Dict of doxyparser-specific data to aid in the generation
                of python classes for this type.
        """
        info = {}

        # Go through each attribute and see if they are special
        for attr in node_type.get_attributes().values():
            # Can't do anything with an "any" attribute
            if attr.is_any_attribute():
                continue

            if attr.is_any_type():
                self._provide(info, ANY, [])
                info[ANY].append(attr.get_name())
                continue

            # Doxygen has a DoxBool type that is either 'yes' or 'no'. We can
            # make it so we have methods that will return a boolean value based
            # on these two options.
            if attr.is_dox_bool():
                self._provide(info, BOOLS, [])

                info[BOOLS].append(attr.get_name())
                continue

            # For attributes that have to be within a list of enumerated
            # values, we can make methods that search for these known values
            if attr.is_enum():
                self._provide(info, ENUMS, {})
                info[ENUMS][attr.get_name()] = attr.get_enum_values()

                continue

            # catchall
            self._provide(info, SIMPLE, [])
            info[SIMPLE].append(attr.get_name())

        return info

    def get_element_info(self, elements):
        """Compile doxyparser-specific information about the elements.

        Returns:
            dict: Dict of doxyparser-specific data to aid in the generation
                of python classes for this type.
        """
        info = {}

        for elem in elements.values():

            if elem.is_placeholder():
                self._provide(info, PLACEHOLDER, [])
                info[PLACEHOLDER].append(elem.get_name())
            elif elem.is_any_type():
                self._provide(info, ANY, [])
                info[ANY].append(elem.get_name())
            elif elem.is_simple():
                self._provide(info, SIMPLE, [])
                info[SIMPLE].append(elem.get_name())
            elif elem.is_complex():
                self._provide(info, COMPLEX, {})
                info[COMPLEX][elem.get_name()] = elem.get_type_name()
            else:
                info[elem.get_name()] = {
                    TYPE: elem.get_type_name()
                }

        return info

    def add_element_config(self, name, type_name):
        """Add element configuration.

        Args:
            name (str): The name of the element
            type_name (str): The type of the element
        """
        self.set_path(type_name, ELEMENTS, name)
