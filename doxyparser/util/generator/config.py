from yaml import load, dump
import pathlib


try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

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

    def __init__(self, path, xsd):
        self._path = path
        self._config = None
        self._xsd = None

    def set_xsd(self, xsd):
        self._xsd = xsd

    def load(self):
        if self._config is None:
            # Load the current configuration
            if pathlib.Path(self._path).exists():
                config_file = open(self._path, 'r')
                self._config = load(config_file, Loader=Loader)
                config_file.close()

            self._config = {} if self._config is None else self._config

        return self

    def save(self):
        config_file = open(self._path, 'w')
        dump(self._config, config_file)
        config_file.close()

    def _provide(self, d, key, default):
        if d.get(key) is None:
            d[key] = default

        return d

    def set_path(self, value, *args):
        args = list(args)
        config = self._config[XSD][self._xsd]
        cur_config = config
        last_part = args.pop()
        for part in args:
            self._provide(cur_config, part, {})
            cur_config = cur_config[part]

        cur_config[last_part] = value

        return cur_config[last_part]

    def get_config(self):
        if self._xsd is None:
            raise Exception('Unable to get configuration without setting xsd!')

        self.load()
        self._provide(self._config, XSD, {})
        self._provide(self._config[XSD], self._xsd, {})

        xsd_config = self._config.get(XSD)
        if xsd_config is None:
            raise AttributeError(f'Cannot find {XSD} root in {self._path}')

        return xsd_config

    def get_xsd_config(self):
        key = self._xsd
        config = self.get_config()

        self._provide(config, key, {})
        return config[key]

    def get_xsd_files(self):
        return self.get_config().keys()

    def get_xsd_names(self):
        return self._config.get(XSD).keys()

    def get_types(self):
        return self.get_xsd_config().get(TYPES, {})

    def get_groups(self):
        return self.get_xsd_config().get(GROUPS, {})

    def get_elements(self):
        return self.get_xsd_config().get(ELEMENTS, {})

    def get_element_type(self, element_name):
        return self.get_elements().get(element_name)

    def get_type_config(self, type_name):
        return self.get_types().get(type_name)

    def get_group_config(self, group_name):
        return self.get_groups().get(group_name)

    def get_group_groups(self, group_name):
        return self.get_group_config(group_name).get(GROUPS, {})

    def get_type_groups(self, type_name):
        return self.get_type_config(type_name).get(GROUPS, {})

    def get_type_attributes(self, type_name):
        return self.get_type_config(type_name).get(ATTRIBUTES, {})

    def get_type_elements(self, type_name):
        return self.get_type_config(type_name).get(ELEMENTS, {})

    def get_group_elements(self, group_name):
        return self.get_group_config(group_name).get(ELEMENTS, {})

    def get_element_config(self, element_name):
        return self.get_elements().get(element_name)

    def type_has_enum_attributes(self, type_name):
        return ENUMS in self.get_type_attributes(type_name).keys()

    def get_type_enum_attributes(self, type_name):
        if not self.type_has_enum_attributes(type_name):
            raise AttributeError(f'Given type {type_name} does not have an {ENUMS} attribute!')

        return self.get_type_attributes(type_name)[ENUMS]

    def add_group_config(self, name, group):
        """Add group configuration to the xsd config

        Args:
            name (str): The name of the group
            group (Group): The group to add configuration details for
        """
        group_info = {}
        group_info[ELEMENTS] = self.get_element_info(group.get_elements())
        groups = [g for g in group.get_groups()]
        if len(groups) > 0:
            group_info[GROUPS] = groups

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

    def get_group_info(self, node_type):
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
            raise Exception('Multiple groups in a single node not supported yet!')

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

            #catchall
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
        self.set_path(type_name, ELEMENTS, name)
