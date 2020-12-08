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
        self._xsd = xsd
        self._config = None

    def load(self):
        if self._config is None:
            # Load the current configuration
            if pathlib.Path(self._path).exists():
                config_file = open(self._path, 'r')
                self._config = load(config_file, Loader=Loader)
                config_file.close()

            self._config = {} if self._config is None else self._config
            self._provide(self._config, XSD, {})
            self._provide(self._config[XSD], self._xsd, {})

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
        self.load()
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

    def get_elements(self):
        return self.get_xsd_config().get(ELEMENTS, {})

    def get_type_config(self, type_name):
        return self.get_types().get(type_name)

    def get_type_attributes(self, type_name):
        return self.get_type_config(type_name).get(ATTRIBUTES, {})

    def get_type_elements(self, type_name):
        return self.get_type_config(type_name).get(ELEMENTS, {})

    def get_element_config(self, element_name):
        return self.get_elements().get(element_name)

    def type_has_enum_attributes(self, type_name):
        return ENUMS in self.get_type_attributes(type_name).keys()

    def get_type_enum_attributes(self, type_name):
        if not self.type_has_enum_attributes(type_name):
            raise AttributeError(f'Given type {type_name} does not have an {ENUMS} attribute!')

        return self.get_type_attributes(type_name)[ENUMS]

    def add_type_config(self, name, attr_info, elem_info):
        type_config = self.set_path({}, TYPES, name)
        if len(attr_info) > 0:
            type_config[ATTRIBUTES] = attr_info
        if len(elem_info) > 0:
            type_config[ELEMENTS] = elem_info

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
                if info.get(ANY) is None:
                    info[ANY] = []

                info[ANY].append(attr.get_name())
                continue

            # Doxygen has a DoxBool type that is either 'yes' or 'no'. We can
            # make it so we have methods that will return a boolean value based
            # on these two options.
            if attr.is_dox_bool():
                if info.get(BOOLS) is None:
                    info[BOOLS] = []

                info[BOOLS].append(attr.get_name())
                continue

            # For attributes that have to be within a list of enumerated
            # values, we can make methods that search for these known values
            if attr.is_enum():
                if info.get(ENUMS) is None:
                    info[ENUMS] = {}

                info[ENUMS][attr.get_name()] = attr.get_enum_values()

                continue
            elif attr.is_simple():
                if info.get(SIMPLE) is None:
                    info[SIMPLE] = {}
                info[SIMPLE] = attr.get_name()

        return info

    def get_element_info(self, node_type):
        """Compile doxyparser-specific information about the elements in this
        type.

        Returns:
            dict: Dict of doxyparser-specific data to aid in the generation
                of python classes for this type.
        """
        info = {}

        for elem in node_type.get_elements().values():

            if elem.is_placeholder():
                if info.get(PLACEHOLDER) is None:
                    info[PLACEHOLDER] = []
                info[PLACEHOLDER].append(elem.get_name())
            elif elem.is_any_type():
                if info.get(ANY) is None:
                    info[ANY] = []
                info[ANY].append(elem.get_name())
            elif elem.is_simple():
                if info.get(SIMPLE) is None:
                    info[SIMPLE] = []
                info[SIMPLE].append(elem.get_name())
            elif elem.is_complex():
                if info.get(COMPLEX) is None:
                    info[COMPLEX] = {}
                info[COMPLEX][elem.get_name()] = elem.get_type_name()
            else:
                info[elem.get_name()] = {
                    TYPE: elem.get_type_name()
                }

        return info

    def add_element_config(self, name, type_name):
        self.set_path(type_name, ELEMENTS, name)
